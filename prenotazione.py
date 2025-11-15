import tkinter as tk
from tkinter import messagebox, ttk
from Studente import Studente
from tkcalendar import DateEntry
from mysql.connector import Error
from connessione import connect_to_db
from datetime import datetime, timedelta

def prenotazione(utente):
    # Creazione della finestra principale
    reg_window = tk.Tk()
    reg_window.title("Seleziona Orari")
    reg_window.geometry("650x300")

    # Label con la data di domani
    domani = (datetime.now() + timedelta(days=1)).date()
    tk.Label(reg_window, text=f"Prenotazione per giorno: {domani.strftime('%d/%m/%Y')}")\
        .grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # --------------------- ORARIO ---------------------
    tk.Label(reg_window, text="Ora di inizio:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    combo_inizio_ore = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(8, 20)], width=5)
    combo_inizio_ore.set("08")
    combo_inizio_ore.grid(row=1, column=1, padx=5, pady=5)
    combo_inizio_minuti = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(0, 60, 5)], width=5)
    combo_inizio_minuti.set("00")
    combo_inizio_minuti.grid(row=1, column=2, padx=5, pady=5)

    tk.Label(reg_window, text="Ora di fine:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    combo_fine_ore = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(8, 20)], width=5)
    combo_fine_ore.set("08")
    combo_fine_ore.grid(row=2, column=1, padx=5, pady=5)
    combo_fine_minuti = ttk.Combobox(reg_window, values=[f'{i:02d}' for i in range(0, 60, 5)], width=5)
    combo_fine_minuti.set("00")
    combo_fine_minuti.grid(row=2, column=2, padx=5, pady=5)

    # --------------------- MATERIA ---------------------
    tk.Label(reg_window, text="Seleziona materia:").grid(row=3, column=0, padx=10, pady=5, sticky="w")

    materia_var = tk.StringVar()
    combo_materie = ttk.Combobox(reg_window, textvariable=materia_var, state="readonly", width=40)
    combo_materie.grid(row=3, column=1, padx=10, pady=5)

    # Recupero materie dal DB in base alla matricola dell'utente
    matricola = utente.matricola  
    materie_dict = {} 

    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                SELECT materia.id, materia.materia 
                FROM studente
                JOIN materia ON studente.Fkcorsodistudio = materia.Fkcorsodistudio
                WHERE studente.Matricola = %s
            """
            cursor.execute(query, (matricola,))
            result = cursor.fetchall()
            materie = [row[1] for row in result]
            materie_dict = {row[1]: row[0] for row in result}
            combo_materie["values"] = materie
            if materie:
                combo_materie.current(0)
                materia_var.set(materie[0])
        except Error as e:
            messagebox.showerror("Errore database", str(e))
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Errore", "Connessione al database fallita!")
        reg_window.destroy()
        return


    # --------------------- EDIFICIO ---------------------
    edifici = {}
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM edificio")
        for row in cursor.fetchall():
            edifici[row[1]] = row[0]  # chiave = nome edificio, valore = id
        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Errore", "Connessione al database fallita!")
        reg_window.destroy()
        return

    tk.Label(reg_window, text="Seleziona edificio:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    edificio_var = tk.StringVar()
    combo_edifici = ttk.Combobox(
        reg_window,
        textvariable=edificio_var,
        values=list(edifici.keys()),
        state="readonly"  # impedisce l'inserimento manuale
    )
    combo_edifici.grid(row=4, column=1, padx=10, pady=5)
    combo_edifici.current(0)  # seleziona il primo elemento di default

    # Callback per aggiornare il valore selezionato
    def on_edificio_selected(event):
        edificio_var.set(combo_edifici.get())  # aggiorna il StringVar
        aggiorna_aule()  # aggiorna la combobox delle aule

    combo_edifici.bind("<<ComboboxSelected>>", on_edificio_selected)

    # --------------------- AULA ---------------------
    tk.Label(reg_window, text="Seleziona aula:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    aula_var = tk.StringVar()
    combo_aule = ttk.Combobox(reg_window, textvariable=aula_var, state="readonly")
    combo_aule.grid(row=5, column=1, padx=10, pady=5)

    aule_dict = {}  # mappatura nome aula -> id aula

    # Funzione per aggiornare le aule in base all'edificio selezionato
    def aggiorna_aule(*args):
        edificio_selezionato = edificio_var.get()
        if not edificio_selezionato:
            combo_aule["values"] = []
            combo_aule.set("")
            return

        id_edificio = edifici[edificio_selezionato]
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM aula WHERE fkedificio = %s", (id_edificio,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        aule = [row[1] for row in result]
        nonlocal aule_dict
        aule_dict = {row[1]: row[0] for row in result}

        combo_aule["values"] = aule
        if aule:
            combo_aule.current(0)
            aula_var.set(aule[0])
            aggiorna_tavoli()  # ← aggiungi questa riga qui
        else:
            combo_aule.set("")

    aggiorna_aule()  # aggiorna le aule all'avvio

    # --------------------- TAVOLI ---------------------
    tk.Label(reg_window, text="Seleziona tavolo:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    frame_tavoli = tk.Frame(reg_window)
    frame_tavoli.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    tavolo_selezionato = tk.StringVar(value="")

    def recupera_tavoli_per_aula(aula_id):
        conn = connect_to_db()
        if not conn:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, numeroposti FROM tavolo WHERE fkaula = %s", (aula_id,))
            tavoli = cursor.fetchall()
            # Ritorna lista di tuple (id, descrizione)
            return [(row[0], f"Tavolo {row[0]} - {row[1]} posti") for row in tavoli]
        except Error as e:
            print("Errore nel recupero dei tavoli:", e)
            return []
        finally:
            cursor.close()
            conn.close()


    tavolo_selezionato_id = tk.IntVar(value=0)  # memorizza l'ID reale del tavolo

    def aggiorna_tavoli(*args):
        for widget in frame_tavoli.winfo_children():
            widget.destroy()

        aula_selezionata = combo_aule.get()
        id_aula = aule_dict.get(aula_selezionata)
        if not id_aula:
            tavolo_selezionato.set("")
            tavolo_selezionato_id.set(0)
            return

        tavoli = recupera_tavoli_per_aula(id_aula)
        if not tavoli:
            tavolo_selezionato.set("")
            tavolo_selezionato_id.set(0)
            return

        # Seleziona automaticamente il primo tavolo
        tavolo_selezionato.set(tavoli[0][1])      # descrizione
        tavolo_selezionato_id.set(tavoli[0][0])   # ID reale

        for i, (tid, descrizione) in enumerate(tavoli, start=1):
            rb = tk.Radiobutton(
                frame_tavoli,
                text=descrizione,
                variable=tavolo_selezionato,
                value=descrizione,
                command=lambda tid=tid: tavolo_selezionato_id.set(tid)  # aggiorna ID reale
            )
            rb.grid(row=i, column=0, sticky="w", padx=5, pady=2)


    combo_aule.bind("<<ComboboxSelected>>", aggiorna_tavoli)
    aggiorna_tavoli()  # aggiorna tavoli all'avvio

    # --------------------- BOTTONE CONFERMA ---------------------
    def conferma_prenotazione():
        aula_selezionata = combo_aule.get()
        id_aula = aule_dict.get(aula_selezionata)
        tavolo_descrizione = tavolo_selezionato.get()
        tavolo_id = tavolo_selezionato_id.get()  # ID reale del tavolo
        ora_inizio_str = f"{combo_inizio_ore.get()}:{combo_inizio_minuti.get()}"
        ora_fine_str = f"{combo_fine_ore.get()}:{combo_fine_minuti.get()}"
        
        materia_selezionata = combo_materie.get()
        id_materia = materie_dict.get(materia_selezionata)
        
        # Costruisci datetime completo usando la data di domani
        domani = (datetime.now() + timedelta(days=1)).date()
        ora_inizio = datetime.strptime(f"{domani} {ora_inizio_str}", "%Y-%m-%d %H:%M")
        ora_fine = datetime.strptime(f"{domani} {ora_fine_str}", "%Y-%m-%d %H:%M")
        
        # Inserimento nel DB
        conn = connect_to_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                    INSERT INTO prenotazione (fkstudente, fktavolo, orainizio, orafine, fkmateria)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (utente.matricola, tavolo_id, ora_inizio, ora_fine, id_materia))
                conn.commit()
                messagebox.showinfo(
                    "Prenotazione Confermata",
                    f"Aula: {aula_selezionata}\nTavolo: {tavolo_descrizione}\nID Tavolo: {tavolo_id}\nMateria: {materia_selezionata}\nOrario: {ora_inizio_str} - {ora_fine_str}"
                )
            except Error as e:
                messagebox.showerror("Errore database", str(e))
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Errore", "Connessione al database fallita!")

        # Chiudi la finestra dopo conferma
        reg_window.destroy()


    submit_button = tk.Button(reg_window, text="Conferma prenotazione", command=conferma_prenotazione)
    submit_button.grid(row=7, column=1, columnspan=3, pady=10)

    # --------------------- BOTTONE ANNULLA ---------------------
    def annulla():
        reg_window.destroy()


    button_annulla = tk.Button(reg_window, text="Annulla", command=annulla)
    button_annulla.grid(row=7, column=0, columnspan=3, pady=5)

    reg_window.mainloop()
