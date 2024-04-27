"""
This file contains functions to open a db connection and select data based on various conditions
"""
from db.driver import DBConnection
import pandas as pd

class Select:
    def __init__(self, table_name, conn=None):
        self.table_name = table_name 
        self.conn = conn # this is a postgres connection object       
    
    def get_by_columns(self, *columns) -> str:
        """
        This is a helper function to get specific columns or all the columns if none is passed
        """
        prefix = 'SELECT'
        suffix = f'FROM {self.table_name}'
       
        if not columns:
            condition = ' * '
        else:
            condition = ','.join(columns)
            
        select_query = ' '.join([prefix, condition, suffix])

        return select_query
    
    def read_sql(self, query) -> pd.DataFrame:
        """
        This uses the pandas library to read records as a pandas table
        """
        try:
            df = pd.read_sql(query, conn=self.conn)
        except Exception as e:
            raise ConnectionError("Unable to query the database into a dataframe")
