import tkinter as tk
from tkinter import messagebox

from profilo import Profilo


class HomeStudente:
    def __init__(self, utente):
        self.utente = utente
      #  self.utenti = utenti  # Lista di utenti (studenti e amministratori)

        # Crea la finestra principale
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



    def mostra_profilo(self):
        # Crea un'istanza di Profilo e chiama il metodo per visualizzare il profilo
        profilo = Profilo(self.utente)
        profilo.mostra_profilo()

    def visualizza_esami(self):
        # Aggiungi logica per visualizzare esami
        messagebox.showinfo("Esami", "Esami disponibili: Esame1, Esame2, Esame3")

    def logout(self):
        self.home_window.destroy()
        print("Logout effettuato.")
