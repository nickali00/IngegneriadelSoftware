# db_connection.py
import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='user',
            password='userpassword',
            database='universita_db'
        )

        if conn.is_connected():
            return conn

    except Error as e:
        print("Errore durante la connessione al database:", e)
        return None
