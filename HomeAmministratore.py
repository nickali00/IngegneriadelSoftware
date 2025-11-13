import tkinter as tk
from tkinter import messagebox

from Studente import Studente
from profilo import Profilo  # Assicurati che questa classe sia definita correttamente per visualizzare il profilo


class HomeAmministratore:
    def __init__(self, utente, utenti):
        self.utente = utente
        self.utenti = utenti  # Lista di utenti (studente, amministratore, ecc.)

        # Finestra principale
        self.home_window = tk.Tk()
        self.home_window.title(f"Home Amministratore: {self.utente.nome}")
        self.home_window.geometry("400x400")

        # Etichetta di benvenuto
        label_benvenuto = tk.Label(self.home_window, text=f"Benvenuto, {self.utente.nome}!", font=("Arial", 16))
        label_benvenuto.pack(pady=20)

        # Bottone per gestire gli utenti
        button_gestione_utenti = tk.Button(self.home_window, text="Gestisci Utenti", command=self.mostra_lista_utenti)
        button_gestione_utenti.pack(pady=10)
        
        # Bottone per aggiungerr nuova aulta studio
        button_gestione_utenti = tk.Button(self.home_window, text="Aggiungi aula studio", command=self.mostra_lista_utenti)
        button_gestione_utenti.pack(pady=10)
        
        # Bottone per aggiungerr nuova aulta studio
        button_gestione_utenti = tk.Button(self.home_window, text="Aggiungi nuovo tavolo", command=self.mostra_lista_utenti)
        button_gestione_utenti.pack(pady=10)
        
        # Bottone per visualizzare report
        button_report = tk.Button(self.home_window, text="Visualizza Report", command=self.visualizza_report)
        button_report.pack(pady=10)

        # Bottone per fare logout
        button_logout = tk.Button(self.home_window, text="Logout", command=self.logout)
        button_logout.pack(pady=20)

        self.home_window.mainloop()

    def mostra_lista_utenti(self):
        # Finestra per visualizzare la lista degli utenti
        lista_utenti_window = tk.Toplevel(self.home_window)
        lista_utenti_window.title("Lista Utenti")
        lista_utenti_window.geometry("300x300")

        # Etichetta per la lista
        label_lista_utenti = tk.Label(lista_utenti_window, text="Seleziona un utente:", font=("Arial", 14))
        label_lista_utenti.pack(pady=10)

        # Aggiungi un bottone per ogni utente nella lista
        for utente in self.utenti:
            if isinstance(utente, Studente):
                button_utente = tk.Button(lista_utenti_window, text=f"{utente.nome} {utente.cognome}",
                                      command=lambda u=utente: self.visualizza_profilo(u))
                button_utente.pack(pady=5)

    def visualizza_profilo(self, utente):
        # Quando un amministratore clicca su un utente, viene mostrato il suo profilo
        profilo = Profilo(utente)
        profilo.mostra_profilo()

    def visualizza_report(self):
        # Aggiungi logica per visualizzare il report
        messagebox.showinfo("Report", "Report delle attività recenti nel sistema.")

    def logout(self):
        self.home_window.destroy()
        print("Logout effettuato.")
