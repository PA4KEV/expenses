import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "exp_db",
        user = "root",
        password = "password",
        database = "expenditures",
    )
         