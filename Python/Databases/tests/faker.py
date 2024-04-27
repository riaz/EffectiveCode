from faker import Faker
import random

"""
The purpose of this file is to randomly generate data for tables in databases
Ideally we would want to be smart about the data that we ingest and map the fake data
accordingly.

Note: This library should strictly make use of db metadata to generate data, and shouldn't include
api's to make queries or joins
"""

class FakeData:
    def __init__(self, table_name, schema, conn: None):
        """
        table_name  - is the name of the table we are generating the fake data for
        conn - is the handler for the database connection for getting schema etc.
        """
        self.table_name = table_name
        self.schema = schema
        self.conn = conn


    def generate_row():
        pass

    def generate_rows():
        pass



