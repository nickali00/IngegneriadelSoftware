import mysql.connector
from mysql.connector import Error

# Funzione per connettersi al database
def connect_to_db():
    try:
        # Connessione al database MySQL in esecuzione in Docker
        conn = mysql.connector.connect(
            host='localhost',  # L'host è 'localhost' se stai eseguendo Docker sulla stessa macchina
            port=3306,  # La porta mappata nel docker-compose.yml
            user='user',  # Nome utente (modifica con il tuo utente se necessario)
            password='userpassword',  # Password dell'utente (modifica con la tua password)
            database='universita_db'  # Nome del database (modifica con il tuo nome del database)
        )

        if conn.is_connected():
            print("Connessione al database MySQL avvenuta con successo!")

            # Crea un cursore per eseguire le query
            cursor = conn.cursor()

            # Esegui una query di esempio per recuperare i dati
            cursor.execute('SELECT DATABASE()')  # Recupera il nome del database corrente
            db_name = cursor.fetchone()
            print(f"Connesso al database: {db_name[0]}")

            # Chiudi il cursore
            cursor.close()

    except Error as e:
        print("Errore durante la connessione al database:", e)

    finally:
        if conn.is_connected():
            # Chiudi la connessione
            conn.close()
            print("Connessione al database chiusa.")

# Chiama la funzione per connetterti al database
connect_to_db()
