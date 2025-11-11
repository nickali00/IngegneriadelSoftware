import tkinter as tk
from tkinter import messagebox
import registrazione

def login(utenti):
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
        email = entry_email.get()
        password = entry_password.get()

        for utente in utenti:
            if utente.email == email and utente.password == password:
                messagebox.showinfo("Login", f"Benvenuto {utente.nome} {utente.cognome}!")
                root.destroy()
                return

        messagebox.showerror("Login", "Email o password errati!")

    def apri_registrazione():
        root.withdraw()
        registrazione.registrazione(utenti)

    frame_bottoni = tk.Frame(root)
    frame_bottoni.pack(pady=20)

    button_login = tk.Button(frame_bottoni, text="Login", command=verifica_login)
    button_login.pack(side=tk.LEFT, padx=10)

    button_registrazione = tk.Button(frame_bottoni, text="Registrati", command=apri_registrazione)
    button_registrazione.pack(side=tk.LEFT, padx=10)

    root.mainloop()
