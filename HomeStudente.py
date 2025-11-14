import tkinter as tk
from tkinter import messagebox

from prenotazione import prenotazione
from profilo import Profilo

class HomeStudente:
    def __init__(self, utente):
        self.utente = utente
        self.is_admin=False
        # Crea la finestra principale
        self.home_window = tk.Tk()
        self.home_window.title(f"Home Studente: {self.utente.nome}")
        self.home_window.geometry("400x400")

        # Etichetta di benvenuto
        label_benvenuto = tk.Label(self.home_window, text=f"Benvenuto, {self.utente.nome}!", font=("Arial", 16))
        label_benvenuto.pack(pady=20)

        # Bottone per gestire il profilo utente
        button_gestione_utenti = tk.Button(self.home_window, text="Visualizza Profilo", command=self.mostra_profilo)
        button_gestione_utenti.pack(pady=10)

        button_gestione_prenotazioni= tk.Button(self.home_window, text="Prenotati", command=self.mostra_prenotazioni)
        button_gestione_prenotazioni.pack(pady=10)

        # Bottone per visualizzare report
        button_report = tk.Button(self.home_window, text="Visualizza Report", command=self.visualizza_report)
        button_report.pack(pady=10)

        # Bottone per fare logout
        button_logout = tk.Button(self.home_window, text="Logout", command=self.logout)
        button_logout.pack(pady=20)

        self.home_window.mainloop()

    def mostra_profilo(self):
        # Crea un'istanza di Profilo e chiama il metodo per visualizzare il profilo
        Profilo(self.utente, False)

    def visualizza_report(self):
        # Aggiungi logica per visualizzare un report
        messagebox.showinfo("Report", "Visualizzazione dei report in corso...")

    def mostra_prenotazioni(self):
        # Aggiungi logica per visualizzare un report
        prenotazione(self.utente)

    def logout(self):
        self.home_window.destroy()
        print("Logout effettuato.")
