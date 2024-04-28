import random 

from .faker import FakeData
from .helper import get_db_connection

def test_generate_row():

    db = get_db_connection()

    db.connect()

    schema_name = "demo"
    table_name = "Account"

    f = FakeData(table_name, schema_name, db)

    row = f.generate_row()

    assert len(row) == 5

    db.close()


def test_generate_rows():

    db = get_db_connection()

    db.connect()

    schema_name = "demo"
    table_name = "Account"

    f = FakeData(table_name, schema_name, db)

    row_cnt = f.randomNumber(1,100)

    rows = f.generate_rows(row_cnt)

    assert len(rows) == row_cnt
    assert len(rows[0]) == 5

    db.close()