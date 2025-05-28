import mysql.connector
from mysql.connector import Error
import os
def get_db_config():
    """Retrieve database configuration from environment variables."""
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "root"),
        "port": os.getenv("DB_PORT", "3306"),
        "password": os.getenv("DB_PASSWORD", ""),
        "database": os.getenv("DB_NAME", "consulta_inmuebles")
    }
def get_connection():
    """Create a database connection."""
    config = get_db_config()
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    """Close the database connection."""
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
    else:
        print("No active MySQL connection to close")