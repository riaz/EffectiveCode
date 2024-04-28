
import random
from typing import Any, List

from faker import Faker
from db.select import Select
from db.driver import DBConnection


"""
The purpose of this file is to randomly generate data for tables in databases
Ideally we would want to be smart about the data that we ingest and map the fake data
accordingly.

Note: This library should strictly make use of db metadata to generate data, and shouldn't include
api's to make queries or joins
"""

class FakeData:
    def __init__(self, table_name, schema, conn: DBConnection = None):
        """
        table_name  - is the name of the table we are generating the fake data for
        conn - is the handler for the database connection for getting schema etc.
        """
        self.conn = conn
        self.table_name = table_name
        self.schema = schema
        self.schema_def = Select(table_name, schema, conn).get_schema()

    def generate_row(self) -> List[Any]:
        res = []
        fake = Faker()
        
        for row in self.schema_def:
            if row.udt_name in ['int8']:
                res.append(fake.phone_number())
            elif row.udt_name in ['varchar']:
                res.append(fake.first_name())
            else:
                res.append(fake.last_name())
        return res

    def generate_rows(self, n=20) -> List[List[Any]]:
        out = []
        for _ in range(n):
            out.append(self.generate_row())
        return out
    
    def randomNumber(self, start, end) -> int:
        return random.choice(range(start, end))
