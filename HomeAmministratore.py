import tkinter as tk
from tkinter import messagebox

from mysql.connector import Error

from nuova_aula import nuovaaula
from nuovo_tavolo import nuovotavolo
from Studente import Studente
from connessione import connect_to_db
from profilo import Profilo  # Assicurati che questa classe sia definita correttamente per visualizzare il profilo


class HomeAmministratore:
    def __init__(self, utente):
        self.utente = utente


        # Finestra principale
        self.home_window = tk.Tk()
        self.home_window.title(f"Home Amministratore: {self.utente.nome}")
        self.home_window.geometry("400x400")

        # Etichetta di benvenuto
        label_benvenuto = tk.Label(self.home_window, text=f"Benvenuto, {self.utente.nome}!", font=("Arial", 16))
        label_benvenuto.pack(pady=20)

        # Bottone per gestire gli utenti
        button_gestione_utenti = tk.Button(self.home_window, text="Approva Utenti", command=self.mostra_lista_utenti)
        button_gestione_utenti.pack(pady=10)
        
        # Bottone per aggiungerr nuova aulta studio
        button_gestione_aule = tk.Button(self.home_window, text="Aggiungi aula studio", command=self.nuova_aula_studiio)
        button_gestione_aule.pack(pady=10)
        
        # Bottone per aggiungerr nuova aulta studio
        button_gestione_tavoli = tk.Button(self.home_window, text="Aggiungi nuovo tavolo", command=self.nuovo_tavolo)
        button_gestione_tavoli.pack(pady=10)
        
        # Bottone per visualizzare report
        button_report = tk.Button(self.home_window, text="Visualizza Report", command=self.visualizza_report)
        button_report.pack(pady=10)

        # Bottone per fare logout
        button_logout = tk.Button(self.home_window, text="Logout", command=self.logout)
        button_logout.pack(pady=20)

        self.home_window.mainloop()

    def mostra_lista_utenti(self):
        utenti = []  # inizializzo lista vuota
        conn = connect_to_db()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                query = """
                            SELECT studente.*, corsidistudio.corsodistudio AS corsodistudio
                            FROM studente
                            LEFT JOIN corsidistudio ON studente.Fkcorsodistudio = corsidistudio.id
                            WHERE studente.Matricola IS NULL
                              AND studente.Fkcorsodistudio IS NOT NULL;
                        """
                cursor.execute(query)
                for user in cursor.fetchall():
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
                    utenti.append(studente)  # aggiungi oggetto alla lista

            except Error as e:
                print("Errore durante la query:", e)

            finally:
                cursor.close()
                conn.close()

        # Crea la finestra della lista utenti
        lista_utenti_window = tk.Toplevel(self.home_window)
        lista_utenti_window.title("Lista Utenti")
        lista_utenti_window.geometry("300x300")

        # Salva il riferimento alla finestra nella variabile d'istanza
        self.lista_utenti_window = lista_utenti_window  # Salvo il riferimento

        # Etichetta per la lista
        label_lista_utenti = tk.Label(lista_utenti_window, text="Seleziona un utente:", font=("Arial", 14))
        label_lista_utenti.pack(pady=10)

        # Aggiungi un bottone per ogni utente nella lista
        for utente in utenti:
            if isinstance(utente, Studente):
                button_utente = tk.Button(lista_utenti_window, text=f"{utente.nome} {utente.cognome}",
                                          command=lambda u=utente: self.visualizza_profilo(u))
                button_utente.pack(pady=5)

    def visualizza_profilo(self, utente):
        # Chiudi la finestra della lista utenti
        if hasattr(self, 'lista_utenti_window') and self.lista_utenti_window.winfo_exists():
            self.lista_utenti_window.destroy()

        # Crea e mostra il profilo dell'utente
        Profilo(utente, is_admin=True)
    def visualizza_report(self):
        # Aggiungi logica per visualizzare il report
        messagebox.showinfo("Report", "Report delle attività recenti nel sistema.")

    def nuova_aula_studiio(self):
        # Aggiungi logica per visualizzare il report
        nuovaaula()

    def nuovo_tavolo(self):
        # Aggiungi logica per visualizzare il report
        nuovotavolo()
    def logout(self):
        self.home_window.destroy()
        print("Logout effettuato.")
