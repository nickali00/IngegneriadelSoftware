import tkinter as tk
from tkinter import messagebox, ttk
from Studente import Studente
from tkcalendar import DateEntry
from mysql.connector import Error
from connessione import connect_to_db
from datetime import datetime

def prenotazione(utente):

    # Creazione della finestra principale
    reg_window = tk.Tk()
    reg_window.title("Seleziona Orari")
    reg_window.geometry("450x300")  # Imposta una dimensione della finestra adatta

    # Etichetta e Combobox per l'ora di inizio
    label_inizio = tk.Label(reg_window, text="Ora di inizio:")
    label_inizio.grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Allinea a sinistra

    combo_inizio_ore = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(8, 20)], width=5)
    combo_inizio_ore.set("08")  # Imposta valore di default
    combo_inizio_ore.grid(row=0, column=1, padx=10, pady=5)

    combo_inizio_minuti = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(0, 60, 5)], width=5)
    combo_inizio_minuti.set("00")  # Imposta valore di default
    combo_inizio_minuti.grid(row=0, column=2, padx=10, pady=5)

    # Etichetta e Combobox per l'ora di fine
    label_fine = tk.Label(reg_window, text="Ora di fine:")
    label_fine.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    combo_fine_ore = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(8, 20)], width=5)
    combo_fine_ore.set("08")  # Imposta valore di default
    combo_fine_ore.grid(row=1, column=1, padx=10, pady=5)

    combo_fine_minuti = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(0, 60, 5)], width=5)
    combo_fine_minuti.set("00")  # Imposta valore di default
    combo_fine_minuti.grid(row=1, column=2, padx=10, pady=5)

    # Etichetta e Combobox per il corso
    label_corso = tk.Label(reg_window, text="Seleziona corso di studio:")
    label_corso.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    aule = {}
    conn = connect_to_db()  # Supponiamo che questa funzione connetta al DB
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM aula")
        for row in cursor.fetchall():
            aule[row[1]] = row[0]  # chiave = nome corso, valore = id
        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Errore", "Connessione al database fallita!")
        reg_window.destroy()
        return

    aula_var = tk.StringVar()

    # Usa grid() per il Combobox aula
    combo_aule = ttk.Combobox(
        reg_window,
        textvariable=aula_var,
        values=list(aule.keys()),
        state="readonly"  # obbligatorio per evitare input manuale
    )
    combo_aule.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky="w")
    combo_aule.current(0)  # Seleziona il primo elemento di default

    # Funzione per gestire il cambio di aula
    def on_corso_selected(event):
        aula_var.set(combo_aule.get())
        aggiorna_tavoli()  # Ricarica i tavoli quando cambia aula

    # Aggiungi la callback di selezione
    combo_aule.bind("<<ComboboxSelected>>", on_corso_selected)

    def aggiorna_tavoli():
        # Elimina i RadioButton precedenti
        for widget in frame_tavoli.winfo_children():
            widget.destroy()

        aula_selezionata = aula_var.get()
        id_aula = aule[aula_selezionata]
        # Recupera i tavoli per l'aula selezionata
        tavoli = recupera_tavoli_per_aula(id_aula)

        # Creazione dei Radiobutton
        for i, tavolo in enumerate(tavoli, start=1):
            radio_button = tk.Radiobutton(frame_tavoli, text=f"Tavolo {i}", variable=tavolo_selezionato,
                                          value=f"Tavolo {i}")
            radio_button.grid(row=i, column=0, padx=5, pady=5, sticky="w")

        # Variabile per il Radiobutton (è condivisa tra tutti i Radiobutton per l'aula)

    tavolo_selezionato = tk.StringVar(value="")

    # Funzione per recuperare i tavoli dall'aula selezionata (simulata)
    def recupera_tavoli_per_aula(aula_id):
        conn = connect_to_db()
        if not conn:
            return []  # Se il DB non è raggiungibile, ritorna una lista vuota

        try:
            cursor = conn.cursor()
            # Query per recuperare i tavoli della specifica aula
            query = "SELECT * FROM tavolo WHERE fkaula = %s;"
            cursor.execute(query, (aula_id,))

            tavoli = cursor.fetchall()  # Ottieni tutti i tavoli per quell'aula
            if not tavoli:
                return []  # Se non ci sono tavoli, ritorna una lista vuota

            # Crea una lista dei tavoli (es. Tavolo 1, Tavolo 2, ...)
            lista_tavoli = [f"Tavolo {tavolo[0]}" for tavolo in tavoli]  # tavolo[0] è l'id del tavolo
            return lista_tavoli

        except Error as e:
            print("Errore nel recupero dei tavoli:", e)
            return []  # In caso di errore nel DB, ritorna una lista vuota

        finally:
            cursor.close()
            conn.close()

    # Frame per i Radiobutton dei tavoli
    frame_tavoli = tk.Frame(reg_window)
    frame_tavoli.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    # Aggiorna i tavoli iniziali
    #aggiorna_tavoli()

    # Bottone di conferma
    submit_button = tk.Button(reg_window, text="Conferma prenotazione",
                              command=lambda: conferma_prenotazione(combo_inizio_ore, combo_inizio_minuti,
                                                                    combo_fine_ore, combo_fine_minuti, combo_aule))
    submit_button.grid(row=4, column=0, columnspan=3, pady=20)

    # Avvio dell'applicazione
    reg_window.mainloop()

    def conferma_prenotazione():



            # Inserimento nel database
        conn = connect_to_db()

        try:
            cursor = conn.cursor()
            query = """
                       INSERT INTO studente (nome, cognome, datanascita, codicefiscale, email, Fkcorsodistudio, password)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)
                   """
      #      cursor.execute(query, (nome, cognome, datanascita, codice_fiscale, email, facolta, password))
            conn.commit()
            messagebox.showinfo("Registrazione", "Registrazione avvenuta con successo!")
        except Error as e:
            messagebox.showerror("Errore database", str(e))
        finally:
            cursor.close()
            conn.close()


        from login import login
        reg_window.destroy()
        login()



    frame_bottoni = tk.Frame(reg_window)
    frame_bottoni.pack(pady=20)

    def annulla():
        try:
            reg_window.destroy()
        except tk.TclError:
            pass
        from login import login
        login()

    button_annulla = tk.Button(frame_bottoni, text="Annulla", command=annulla)
    button_annulla.pack(side=tk.LEFT, padx=10)

   # button_registra = tk.Button(frame_bottoni, text="Registrati", command=registra_utente)
    #button_registra.pack(side=tk.LEFT, padx=10)

    reg_window.mainloop()

