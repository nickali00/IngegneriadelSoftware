import tkinter as tk
from tkinter import messagebox


# Classe Utente aggiunta per rendere il codice eseguibile
class Utente:
    def __init__(self, nome, cognome, data_nascita, codice_fiscale, email, matricola, facolta):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.codice_fiscale = codice_fiscale
        self.email = email
        self.matricola = matricola
        self.facolta = facolta


class Profilo:
    def __init__(self, utente):
        self.utente = utente
        self.profilo_window = tk.Tk()
        self.profilo_window.title(f"Profilo di {self.utente.nome}")
        self.profilo_window.geometry("1200x300")
        self.profilo_window.config(bg="#f2f2f2")

        # Configura le colonne per 6 colonne
        for col in range(6):
            self.profilo_window.grid_columnconfigure(col, weight=1, minsize=180)

        # Etichetta di benvenuto
        label_benvenuto = tk.Label(self.profilo_window, text=f"Profilo di {self.utente.nome}", font=("Arial", 18),
                                   bg="#f2f2f2")
        label_benvenuto.grid(row=0, column=0, columnspan=6, pady=(30, 30))

        STANDARD_PADY = 0

        # --- PRIMO BLOCCO: Nome, Cognome, Data di Nascita (riga 1) ---

        # Nome - Etichetta (col 0): ***SPAZIO ANNULLATO a destra***
        label_nome = tk.Label(self.profilo_window, text="Nome:", font=("Arial", 12), bg="#f2f2f2")
        label_nome.grid(row=1, column=0, sticky="w", padx=(20, 0), pady=STANDARD_PADY)  # padx a destra: 0
        # Nome - Valore (col 1): ***SPAZIO ANNULLATO a sinistra***, ma 30 a destra per separare il blocco
        label_nome_valore = tk.Label(self.profilo_window, text=self.utente.nome, font=("Arial", 12, "bold"),
                                     bg="#f2f2f2")
        label_nome_valore.grid(row=1, column=1, sticky="w", padx=(0, 30), pady=STANDARD_PADY)  # padx a sinistra: 0

        # Cognome - Etichetta (col 2): ***SPAZIO ANNULLATO a destra***
        label_cognome = tk.Label(self.profilo_window, text="Cognome:", font=("Arial", 12), bg="#f2f2f2")
        label_cognome.grid(row=1, column=2, sticky="w", padx=(5, 0), pady=STANDARD_PADY)  # padx a destra: 0
        # Cognome - Valore (col 3): ***SPAZIO ANNULLATO a sinistra***, ma 30 a destra per separare il blocco
        label_cognome_valore = tk.Label(self.profilo_window, text=self.utente.cognome, font=("Arial", 12, "bold"),
                                        bg="#f2f2f2")
        label_cognome_valore.grid(row=1, column=3, sticky="w", padx=(0, 30), pady=STANDARD_PADY)  # padx a sinistra: 0

        # Data di Nascita - Etichetta (col 4): ***SPAZIO ANNULLATO a destra***
        label_data_nascita = tk.Label(self.profilo_window, text="Data di Nascita:", font=("Arial", 12), bg="#f2f2f2")
        label_data_nascita.grid(row=1, column=4, sticky="w", padx=(5, 0), pady=STANDARD_PADY)  # padx a destra: 0
        # Data di Nascita - Valore (col 5): ***SPAZIO ANNULLATO a sinistra***
        label_data_nascita_valore = tk.Label(self.profilo_window, text=self.utente.data_nascita,
                                             font=("Arial", 12, "bold"), bg="#f2f2f2")
        label_data_nascita_valore.grid(row=1, column=5, sticky="w", padx=(0, 20),
                                       pady=STANDARD_PADY)  # padx a sinistra: 0

        # --- SECONDO BLOCCO: Codice Fiscale, Email (riga 2) ---

        # Codice Fiscale - Etichetta (col 0): ***SPAZIO ANNULLATO a destra***
        label_codice_fiscale = tk.Label(self.profilo_window, text="Codice Fiscale:", font=("Arial", 12), bg="#f2f2f2")
        label_codice_fiscale.grid(row=2, column=0, sticky="w", padx=(20, 0), pady=STANDARD_PADY)  # padx a destra: 0
        # Codice Fiscale - Valore (col 1): ***SPAZIO ANNULLATO a sinistra***
        label_codice_fiscale_valore = tk.Label(self.profilo_window, text=self.utente.codice_fiscale,
                                               font=("Arial", 12, "bold"), bg="#f2f2f2")
        label_codice_fiscale_valore.grid(row=2, column=1, sticky="w", padx=(0, 30),
                                         pady=STANDARD_PADY)  # padx a sinistra: 0

        # Email - Etichetta (col 2): ***SPAZIO ANNULLATO a destra***
        label_email = tk.Label(self.profilo_window, text="Email:", font=("Arial", 12), bg="#f2f2f2")
        label_email.grid(row=2, column=2, sticky="w", padx=(5, 0), pady=STANDARD_PADY)  # padx a destra: 0
        # Email - Valore (col 3): ***SPAZIO ANNULLATO a sinistra***
        label_email_valore = tk.Label(self.profilo_window, text=self.utente.email, font=("Arial", 12, "bold"),
                                      bg="#f2f2f2")
        label_email_valore.grid(row=2, column=3, sticky="w", padx=(0, 30), pady=STANDARD_PADY)  # padx a sinistra: 0

        # --- TERZO BLOCCO: Matricola, Facoltà (riga 3) ---

        # Matricola - Etichetta (col 0): ***SPAZIO ANNULLATO a destra***
        label_matricola = tk.Label(self.profilo_window, text="Matricola:", font=("Arial", 12), bg="#f2f2f2")
        label_matricola.grid(row=3, column=0, sticky="w", padx=(20, 0), pady=STANDARD_PADY)  # padx a destra: 0
        # Matricola - Valore (col 1): ***SPAZIO ANNULLATO a sinistra***
        label_matricola_valore = tk.Label(self.profilo_window, text=self.utente.matricola, font=("Arial", 12, "bold"),
                                          bg="#f2f2f2")
        label_matricola_valore.grid(row=3, column=1, sticky="w", padx=(0, 30), pady=STANDARD_PADY)  # padx a sinistra: 0

        # Facoltà - Etichetta (col 2): ***SPAZIO ANNULLATO a destra***
        label_facolta = tk.Label(self.profilo_window, text="Facoltà:", font=("Arial", 12), bg="#f2f2f2")
        label_facolta.grid(row=3, column=2, sticky="w", padx=(5, 0), pady=STANDARD_PADY)  # padx a destra: 0
        # Facoltà - Valore (col 3): ***SPAZIO ANNULLATO a sinistra***
        label_facolta_valore = tk.Label(self.profilo_window, text=self.utente.facolta, font=("Arial", 12, "bold"),
                                        bg="#f2f2f2")
        label_facolta_valore.grid(row=3, column=3, sticky="w", padx=(0, 20), pady=STANDARD_PADY)  # padx a sinistra: 0

        # Separatore visivo
        separator = tk.Label(self.profilo_window, text="", bg="#f2f2f2")
        separator.grid(row=4, column=0, columnspan=6, pady=10)

        # Bottone di chiusura
        button_chiudi = tk.Button(self.profilo_window, text="Chiudi", command=self.profilo_window.destroy)
        button_chiudi.grid(row=5, column=0, columnspan=6, pady=20)

        self.profilo_window.mainloop()