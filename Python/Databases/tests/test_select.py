"""
We will test creation of select queries by column names and also fetch response as pandas table
We will also test extensively this cycle
    - create a temp table with a fixed schema
    - use the helper functions to generate data for the table
    - fetch the data by columns
    - remove the table and delete the data
"""

from .helper import get_db_connection
from db.select import Select

def test_select_init():
    """
    We will test creation of db and select obj and read the contents of the table as a pandas table
    """
    db = get_db_connection()
    
    # starting a connection
    db.connect()

    schema_name = "demo"
    table_name = "Account"

    select = Select(table_name, schema_name, db)

    query = select.get_by_columns(columns=["first_name", "last_name"])

    db.execute(query)

    out = db.fetch_result()

    assert len(out[0]) == 2

    assert out[0] == ["first_name", "last_name"]
    
    # closing a connection
    db.close()


def test_get_schema():
    """
    This is a test if the schema of a target table is returned.
    """
    db = get_db_connection()

    # starting a connection
    db.connect()

    schema_name = "demo"
    table_name = "Account"

    select = Select(table_name, schema_name, db)

    schema = select.get_schema()

    assert len(schema) == 5

    db.close()