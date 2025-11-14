import tkinter as tk
from tkinter import messagebox, ttk
from mysql.connector import Error
from connessione import connect_to_db

def nuovotavolo():
    reg_window = tk.Tk()
    reg_window.title("Nuovo Tavolo")
    reg_window.geometry("300x250")

    label_posti = tk.Label(reg_window, text="Numero posti:")
    label_posti.pack(pady=5)
    entry_posti = tk.Entry(reg_window)
    entry_posti.pack(pady=5)

    label_aula = tk.Label(reg_window, text="Seleziona aula:")
    label_aula.pack(pady=5)

    aule = {}
    conn = connect_to_db()
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
    combo_aule = ttk.Combobox(
        reg_window,
        textvariable=aula_var,
        values=list(aule.keys()),
        state="readonly"  # obbligatorio per evitare input manuale
    )
    combo_aule.pack(pady=5)
    combo_aule.current(0)  # seleziona il primo elemento di default

    # Callback per aggiornare il valore selezionato
    def on_corso_selected(event):
        # aggiorna corso_var con il valore selezionato
        aula_var.set(combo_aule.get())

    combo_aule.bind("<<ComboboxSelected>>", on_corso_selected)

    def nuovo_tavolo():
        numero = entry_posti.get()
        aula_nome = aula_var.get()
        au = aule.get(aula_nome)

        if not numero:
            messagebox.showerror("Errore", "Inserisci il numero!")
            return

        try:
            numero = int(numero)  # Prova a convertirlo in un intero
            if numero <= 0:
                raise ValueError("Il numero deve essere maggiore di zero.")
        except ValueError:
            messagebox.showerror("Errore", "Inserisci un numero intero valido!")
            return


        if not au:
            messagebox.showerror("Errore", "Seleziona un aula!")
            return

            # Inserimento nel database
        conn = connect_to_db()

        try:
            cursor = conn.cursor()
            query = """
                       INSERT INTO tavolo (numeroposti, fkaula)
                       VALUES (%s, %s)
                   """
            cursor.execute(query, (numero, au))
            conn.commit()
            messagebox.showinfo("Registrazione", "aula aggiunta con successo!")
        except Error as e:
            messagebox.showerror("Errore database", str(e))
        finally:
            cursor.close()
            conn.close()


        reg_window.destroy()




    frame_bottoni = tk.Frame(reg_window)
    frame_bottoni.pack(pady=20)

    def annulla():
        try:
            reg_window.destroy()
        except tk.TclError:
            pass

    button_annulla = tk.Button(frame_bottoni, text="Annulla", command=annulla)
    button_annulla.pack(side=tk.LEFT, padx=10)

    button_registra = tk.Button(frame_bottoni, text="aggiungi", command=nuovo_tavolo)
    button_registra.pack(side=tk.LEFT, padx=10)

    reg_window.mainloop()

