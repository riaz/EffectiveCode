import psycopg2
from typing import Any, List
import pandas as pd

class DBConnection:
    def __init__(self, hostname, user, database, port=5432, password=None):
        """
        This is construction for the db
        """
        self.hostname = hostname
        self.database = database
        self.port = port
        self.user = user
        self.password = password

    def connect(self) -> None:
        """
            connect to the database
        """
        try:
            self.conn = psycopg2.connect(database=self.database,
                                    user = self.user,
                                    host = self.hostname,
                                    password = self.password,
                                    port = self.port)
            self.cur = self.conn.cursor()
        except Exception as e:
           raise ConnectionError("Unable to connect to the DB")
    
    def close(self) -> None:
        """
        This method closes the db connection
        """
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            raise ConnectionError("No DB connection exists")
        
    def commit(self) -> None:
        """
        This is a wrapper around DB commit 
        """
        try:
            self.conn.commit()
        except Exception as e:
            raise ConnectionError("Unable to commit to DB")

    def execute(self, statement: str) -> None:
        try:
            self.cur.execute(statement)
            # TODO: print the table values
        except Exception as e:
            raise ConnectionError(f"Unable to execute the query {statement}")
        
    def fetch_result(self) -> List[List[Any]]:
        """
        This function returns the result from the database as a list
        """
        try:
            rows = self.cur.fetchall()
            column_names = [desc[0] for desc in self.cur.description]
            out = []
            out.append(column_names) # persisting the columns as the first row of the data
            for row in rows: 
                out.append(list(row))                
            return out
        except ValueError as e:
            raise ValueError("No rows to fetch")
        except ConnectionError as ce:
            raise ConnectionError("Unable to connect to database to fetch values")