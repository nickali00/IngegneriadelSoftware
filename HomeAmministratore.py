import tkinter as tk
from tkinter import messagebox


class HomeAmministratore:
    def __init__(self, utente):
        self.utente = utente
        self.home_window = tk.Tk()
        self.home_window.title(f"Home Amministratore: {self.utente.nome}")
        self.home_window.geometry("400x400")

        # Etichetta di benvenuto
        label_benvenuto = tk.Label(self.home_window, text=f"Benvenuto, {self.utente.nome}!", font=("Arial", 16))
        label_benvenuto.pack(pady=20)

        # Bottone per gestire gli utenti
        button_gestione_utenti = tk.Button(self.home_window, text="Gestisci Utenti", command=self.gestione_utenti)
        button_gestione_utenti.pack(pady=10)

        # Bottone per visualizzare report
        button_report = tk.Button(self.home_window, text="Visualizza Report", command=self.visualizza_report)
        button_report.pack(pady=10)

        # Bottone per fare logout
        button_logout = tk.Button(self.home_window, text="Logout", command=self.logout)
        button_logout.pack(pady=20)

        self.home_window.mainloop()

    def gestione_utenti(self):
        # Logica per gestire gli utenti
        messagebox.showinfo("Gestione Utenti", "Funzione per aggiungere, modificare o rimuovere utenti.")

    def visualizza_report(self):
        # Logica per visualizzare report
        messagebox.showinfo("Report", "Report delle attività recenti nel sistema.")

    def logout(self):
        self.home_window.destroy()
        print("Logout effettuato.")
