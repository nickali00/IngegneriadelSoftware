import tkinter as tk
from tkinter import messagebox

# Funzione di login
def login(utenti):
    # Creiamo la finestra di login
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x230")

    # Etichette e campi di input
    label_email = tk.Label(root, text="Email:")
    label_email.pack(pady=10)
    entry_email = tk.Entry(root)
    entry_email.pack(pady=5)

    label_password = tk.Label(root, text="Password:")
    label_password.pack(pady=10)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Funzione di verifica login
    def verifica_login():
        email = entry_email.get()
        password = entry_password.get()

        for utente in utenti:
            if utente.email == email and utente.password == password:
                messagebox.showinfo("Login", f"Benvenuto {utente.nome} {utente.cognome}!")
                root.destroy()  # Chiudi la finestra di login
                return

        messagebox.showerror("Login", "Email o password errati!")

    # Bottone di login
    button_login = tk.Button(root, text="Login", command=verifica_login)
    button_login.pack(pady=20)

    # Avvia l'interfaccia grafica
    root.mainloop()

