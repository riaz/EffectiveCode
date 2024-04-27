"""
This file contains functions to open a db connection and select data based on various conditions
"""
from .schema import DBSchema
from .const import DB_SCHEMA

from typing import Optional, List
from db.driver import DBConnection

import pandas as pd

class Select:
    def __init__(self, table_name, schema, conn: DBConnection):
        self.table_name = table_name 
        self.schema = schema
        self.db_conn = conn # this is a postgres connection object   


    def get_schema(self) -> List[DBSchema]:    
        """
        Generate a select query for the table
        return as a list of dataclass DBSchema
        """
        where_dict = {
            "table_name" : self.table_name,
            "table_schema" : self.schema
        }
        columns = ["column_name", "data_type", "is_nullable", "character_maximum_length", "udt_name"]

        query = self.get_by_columns(is_schema=True, columns=columns, where=where_dict)

        self.db_conn.execute(query)

        schema_rows = self.db_conn.fetch_result()

        res : List[DBSchema] = []

        for value in schema_rows[1:]:
            res.append(DBSchema(*value))
        
        return res


    def get_by_columns(self, is_schema=False, columns: Optional[List[str]]=None, **where) -> str:
        """
        This is a helper function to get specific columns or all the columns if none is passed
        """
        prefix = 'SELECT'
        
        if is_schema: # we are tring to fetch metadata for tables
            suffix = f'FROM {DB_SCHEMA}'
        else:
            suffix = f'FROM {self.schema}.\"{self.table_name}\"'

        # TODO: this should be more sophisticated over time
        where_clause = []
        if where:            
            for key, val in where['where'].items():
                where_clause.append(f"{key} = '{val}'")
            
        
        if not columns:
            condition = ' * '
        else:
            condition = ','.join(columns)
            
        if where_clause:
            #print(where_clause, where)
            where_suffix = ' AND '.join(where_clause)
            #where_suffix= 'WHERE ' + ' '.join(where_clause)
            select_query = ' '.join([prefix, condition, suffix, 'WHERE', where_suffix])
        else:
            select_query = ' '.join([prefix, condition, suffix])

        return select_query
    
    
    
    def read_sql(self, query) -> pd.DataFrame:
        """
        This uses the pandas library to read records as a pandas table
        TODO: purge this
        """
        try:
            df = pd.read_sql(query, con=self.db_conn.conn)
        except Exception as e:
            raise ConnectionError("Unable to query the database into a dataframe")
