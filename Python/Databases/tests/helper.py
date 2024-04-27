from db.driver import DBConnection

def get_db_connection():
    hostname = "localhost"
    user = "riaz"
    database = "riaz"
    password = ""
    port = 5432

    db = DBConnection(hostname, user, database, port, password)

    return db