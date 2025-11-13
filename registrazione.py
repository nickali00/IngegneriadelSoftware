import tkinter as tk
from tkinter import messagebox, ttk
from Studente import Studente
from tkcalendar import DateEntry
from mysql.connector import Error
from connessione import connect_to_db
from datetime import datetime

def email_o_codice_esiste(email, codice_fiscale):
    conn = connect_to_db()
    if not conn:
        return True  # blocca registrazione se il db non è raggiungibile
    try:
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM studente WHERE email = %s OR codicefiscale = %s;"
        cursor.execute(query, (email, codice_fiscale))
        count = cursor.fetchone()[0]
        return count > 0
    except Error as e:
        print("Errore database:", e)
        return True
    finally:
        cursor.close()
        conn.close()

def registrazione(utenti):
    reg_window = tk.Tk()
    reg_window.title("Registrazione")
    reg_window.geometry("300x550")

    label_nome = tk.Label(reg_window, text="Nome:")
    label_nome.pack(pady=5)
    entry_nome = tk.Entry(reg_window)
    entry_nome.pack(pady=5)

    label_cognome = tk.Label(reg_window, text="Cognome:")
    label_cognome.pack(pady=5)
    entry_cognome = tk.Entry(reg_window)
    entry_cognome.pack(pady=5)

    label_codice_fiscale = tk.Label(reg_window, text="Codice Fiscale:")
    label_codice_fiscale.pack(pady=5)
    entry_codice_fiscale = tk.Entry(reg_window)
    entry_codice_fiscale.pack(pady=5)

    label_email = tk.Label(reg_window, text="Email:")
    label_email.pack(pady=5)
    entry_email = tk.Entry(reg_window)
    entry_email.pack(pady=5)

    label_password = tk.Label(reg_window, text="Password:")
    label_password.pack(pady=5)
    entry_password = tk.Entry(reg_window, show="*")
    entry_password.pack(pady=5)

    label_nascita = tk.Label(reg_window, text="Data di nascita:")
    label_nascita.pack(pady=5)
    entry_nascita = DateEntry(reg_window, date_pattern='dd/MM/yyyy', locale='it_IT')
    entry_nascita.pack(pady=5)

    label_corso = tk.Label(reg_window, text="Seleziona corso di studio:")
    label_corso.pack(pady=5)

    corsi = {}
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, corsodistudio FROM corsidistudio")
        for row in cursor.fetchall():
            corsi[row[1]] = row[0]  # chiave = nome corso, valore = id
        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Errore", "Connessione al database fallita!")
        reg_window.destroy()
        return
    corso_var = tk.StringVar()
    combo_corsi = ttk.Combobox(
        reg_window,
        textvariable=corso_var,
        values=list(corsi.keys()),
        state="readonly"  # obbligatorio per evitare input manuale
    )
    combo_corsi.pack(pady=5)
    combo_corsi.current(0)  # seleziona il primo elemento di default

    # Callback per aggiornare il valore selezionato
    def on_corso_selected(event):
        # aggiorna corso_var con il valore selezionato
        corso_var.set(combo_corsi.get())

    combo_corsi.bind("<<ComboboxSelected>>", on_corso_selected)

    def registra_utente():
        nome = entry_nome.get()
        cognome = entry_cognome.get()
        codice_fiscale = entry_codice_fiscale.get()
        email = entry_email.get()
        password = entry_password.get()
        datanascita_date = entry_nascita.get_date()
        datanascita = datanascita_date.strftime('%Y-%m-%d')
        corso_nome = corso_var.get()
        facolta = corsi.get(corso_nome)

        if not nome:
            messagebox.showerror("Errore", "Inserisci il nome!")
            return
        if not cognome:
            messagebox.showerror("Errore", "Inserisci il cognome!")
            return
        if not codice_fiscale:
            messagebox.showerror("Errore", "Inserisci il codice fiscale!")
            return
        if not email:
            messagebox.showerror("Errore", "Inserisci l'email!")
            return
        if not password:
            messagebox.showerror("Errore", "Inserisci la password!")
            return
        if not datanascita:
            messagebox.showerror("Errore", "Inserisci la data di nascita!")
            return
        if not facolta:
            messagebox.showerror("Errore", "Seleziona un corso di studio!")
            return

        if email_o_codice_esiste(email, codice_fiscale):
            messagebox.showerror("Errore", "Email o codice fiscale già registrati!")
            return

            # Inserimento nel database
        conn = connect_to_db()

        try:
            cursor = conn.cursor()
            query = """
                       INSERT INTO studente (nome, cognome, datanascita, codicefiscale, email, Fkcorsodistudio, password)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)
                   """
            cursor.execute(query, (nome, cognome, datanascita, codice_fiscale, email, facolta, password))
            conn.commit()
            messagebox.showinfo("Registrazione", "Registrazione avvenuta con successo!")
        except Error as e:
            messagebox.showerror("Errore database", str(e))
        finally:
            cursor.close()
            conn.close()


        from login import login
        reg_window.destroy()
        login()



    frame_bottoni = tk.Frame(reg_window)
    frame_bottoni.pack(pady=20)

    def annulla():
        try:
            reg_window.destroy()
        except tk.TclError:
            pass
        from login import login
        login()

    button_annulla = tk.Button(frame_bottoni, text="Annulla", command=annulla)
    button_annulla.pack(side=tk.LEFT, padx=10)

    button_registra = tk.Button(frame_bottoni, text="Registrati", command=registra_utente)
    button_registra.pack(side=tk.LEFT, padx=10)

    reg_window.mainloop()

