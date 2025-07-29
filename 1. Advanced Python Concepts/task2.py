import mysql.connector
import os
from dotenv import load_dotenv
# 1. Advanced Python Concepts

# Practice Task : 2 | Create a custom context manager to manage database connections.
load_dotenv()
config = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
    "port": os.getenv("MYSQL_PORT")
}

class MySqlConnection:
    """Custom class with context manager for mysql database."""
    def __init__(self, config):
        self.config = config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

with MySqlConnection(config=config) as cursor:
    cursor.execute("SELECT * FROM bookapp_booklist;")
    data = cursor.fetchall()
    print(data)