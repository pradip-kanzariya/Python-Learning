import mysql.connector
# 1. Advanced Python Concepts

# Practice Task : 2 | Create a custom context manager to manage database connections.
config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "bookstore",
    "port": 3306
}

class MySqlConnection:
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