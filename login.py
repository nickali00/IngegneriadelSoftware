# login.py
import tkinter as tk
from tkinter import messagebox
from connessione import connect_to_db
from HomeAmministratore import HomeAmministratore
from Amministratore import Amministratore
from HomeStudente import HomeStudente
from Studente import Studente
import registrazione
from mysql.connector import Error


def login():
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x230")

    label_email = tk.Label(root, text="Email:")
    label_email.pack(pady=10)
    entry_email = tk.Entry(root)
    entry_email.pack(pady=5)

    label_password = tk.Label(root, text="Password:")
    label_password.pack(pady=10)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    def verifica_login():
        email = entry_email.get().strip()
        password = entry_password.get().strip()

        if not email or not password:
            messagebox.showwarning("Attenzione", "Inserisci email e password!")
            return

        conn = connect_to_db()
        if conn is None:
            messagebox.showerror("Errore", "Connessione al database fallita.")
            return

        cursor = conn.cursor(dictionary=True)

        try:
            query = """
                SELECT * 
                FROM studente 
                LEFT JOIN corsidistudio 
                ON studente.Fkcorsodistudio = corsidistudio.id
                WHERE email = %s AND password = %s;
            """
            cursor.execute(query, (email, password))
            user = cursor.fetchone()

            if user:


                if user['Fkcorsodistudio'] is not None:
                    if user['Matricola'] is not None:
                        studente = Studente(
                            nome=user['Nome'],
                            cognome=user['Cognome'],
                            data_nascita=user['Datanascita'],
                            codice_fiscale=user['Codicefiscale'],
                            email=user['Email'],
                            matricola=user['Matricola'],
                            facolta=user['corsodistudio'],
                            password=user['Password']
                        )
                        messagebox.showinfo("Login", f"Benvenuto {user['Nome']} {user['Cognome']}!")
                        root.destroy()
                        HomeStudente(studente)
                    else:
                        messagebox.showerror("Errore", "utente non ancora approvato dall'amministratore")
                else:
                    amministratore = Amministratore(
                        nome=user['Nome'],
                        cognome=user['Cognome'],
                        data_nascita=user['Datanascita'],
                        codice_fiscale=user['Codicefiscale'],
                        email=user['Email'],
                        id_amministratore=user['Matricola'],
                        password=user['Password']
                    )
                    root.destroy()
                    HomeAmministratore(amministratore)

            else:
                messagebox.showerror("Errore", "Email o password errati.")

        except Error as e:
            messagebox.showerror("Errore Database", f"Errore: {e}")
        finally:
            cursor.close()
            conn.close()

    def apri_registrazione():
        root.withdraw()
        registrazione.registrazione([])

    frame_bottoni = tk.Frame(root)
    frame_bottoni.pack(pady=20)

    button_registrazione = tk.Button(frame_bottoni, text="Registrati", command=apri_registrazione)
    button_registrazione.pack(side=tk.LEFT, padx=10)

    button_login = tk.Button(frame_bottoni, text="Login", command=verifica_login)
    button_login.pack(side=tk.LEFT, padx=10)

    root.mainloop()
