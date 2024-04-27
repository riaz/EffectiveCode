from db.driver import DBConnection
from db.select import Select


def get_db_connection():
    hostname = "localhost"
    user = "riaz"
    database = "riaz"
    password = ""
    port = 5432

    db = DBConnection(hostname, user, database, port, password)

    return db

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

    db.fetch_result()

    db.close()