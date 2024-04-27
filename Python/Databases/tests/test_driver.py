from .helper import get_db_connection
from db.select import Select

def test_connect():
    """
    This is to test if the connection was successful
    """
    db = get_db_connection()
    
    # starting a connection
    db.connect()

    # closing a connection
    db.close()

def test_select_query():
    """
    This is a test for select query from the database
    """
    
    db = get_db_connection()

    db.connect()

    table_name = 'demo."Account"'

    select = Select(table_name, db.conn)

    stmt = select.get_by_columns()

    db.execute(stmt)

    data = db.fetch_result()

    assert len(data) == 2 # this should include the columns and one single row

    assert data[0] == ["id", "first_name", "last_name", "email", "mobile"] # this the list of columns in the table

    assert data[1] == [1, 'riaz', 'munshi', 'riaz.2012@gmail.com', 7164319964]

    db.close()