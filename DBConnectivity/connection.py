import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Establish a database connection and return the connection object."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Tanisha3541',
            database='Infosys',
            port = 3306
        )
        if connection.is_connected():
            print("Connection to the database was successful.")
            return connection
    except Error as e:
        print(f"Error while connecting to database: {e}")
        return None

get_db_connection()