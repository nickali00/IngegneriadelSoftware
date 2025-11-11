import tkinter as tk
from tkinter import messagebox
from Studente import Studente

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

    label_matricola = tk.Label(reg_window, text="Matricola:")
    label_matricola.pack(pady=5)
    entry_matricola = tk.Entry(reg_window)
    entry_matricola.pack(pady=5)

    label_facolta = tk.Label(reg_window, text="Facoltà:")
    label_facolta.pack(pady=5)
    entry_facolta = tk.Entry(reg_window)
    entry_facolta.pack(pady=5)

    def registra_utente():
        nome = entry_nome.get()
        cognome = entry_cognome.get()
        codice_fiscale = entry_codice_fiscale.get()
        email = entry_email.get()
        password = entry_password.get()
        matricola = entry_matricola.get()
        facolta = entry_facolta.get()

        if not all([nome, cognome, codice_fiscale, email, password, matricola, facolta]):
            messagebox.showerror("Errore", "Tutti i campi devono essere compilati!")
            return

        for utente in utenti:
            if isinstance(utente, Studente):
                if utente.email == email:
                    messagebox.showerror("Errore", "Email già registrata!")
                    return
                if utente.codice_fiscale == codice_fiscale:
                    messagebox.showerror("Errore", "Codice fiscale già registrato!")
                    return
                if utente.matricola == matricola:
                    messagebox.showerror("Errore", "Matricola già registrata!")
                    return

        nuovo_studente = Studente(nome, cognome, "", codice_fiscale, email, matricola, facolta, password)
        utenti.append(nuovo_studente)

        messagebox.showinfo("Registrazione", "Registrazione avvenuta con successo!")

        reg_window.destroy()
        from login import login
        login(utenti)


    frame_bottoni = tk.Frame(reg_window)
    frame_bottoni.pack(pady=20)

    def annulla():
        reg_window.destroy()
        from login import login
        login(utenti)

    button_annulla = tk.Button(frame_bottoni, text="Annulla", command=annulla)
    button_annulla.pack(side=tk.LEFT, padx=10)

    button_registra = tk.Button(frame_bottoni, text="Registrati", command=registra_utente)
    button_registra.pack(side=tk.LEFT, padx=10)

    reg_window.mainloop()

