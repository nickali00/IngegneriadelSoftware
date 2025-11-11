import tkinter as tk
from tkinter import messagebox


class HomeStudente:
    def __init__(self, utente):
        self.utente = utente
        self.home_window = tk.Tk()
        self.home_window.title(f"Home Studente: {self.utente.nome}")
        self.home_window.geometry("400x400")

        # Etichetta di benvenuto
        label_benvenuto = tk.Label(self.home_window, text=f"Benvenuto, {self.utente.nome}!", font=("Arial", 16))
        label_benvenuto.pack(pady=20)

        # Bottone per visualizzare il profilo
        button_profilo = tk.Button(self.home_window, text="Visualizza Profilo", command=self.mostra_profilo)
        button_profilo.pack(pady=10)

        # Bottone per visualizzare gli esami
        button_esami = tk.Button(self.home_window, text="Visualizza Esami", command=self.visualizza_esami)
        button_esami.pack(pady=10)

        # Bottone per fare logout
        button_logout = tk.Button(self.home_window, text="Logout", command=self.logout)
        button_logout.pack(pady=20)

        self.home_window.mainloop()

    def mostra_profilo(self):
        # Mostra i dettagli del profilo dello studente
        messagebox.showinfo("Profilo",
                            f"Nome: {self.utente.nome}\nCognome: {self.utente.cognome}\nEmail: {self.utente.email}")

    def visualizza_esami(self):
        # Aggiungi logica per visualizzare esami
        messagebox.showinfo("Esami", "Esami disponibili: Esame1, Esame2, Esame3")

    def logout(self):
        self.home_window.destroy()
        print("Logout effettuato.")
