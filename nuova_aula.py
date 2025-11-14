import tkinter as tk
from tkinter import messagebox, ttk
from mysql.connector import Error
from connessione import connect_to_db

def nuovaaula():
    reg_window = tk.Tk()
    reg_window.title("Nuova Aula")
    reg_window.geometry("300x250")

    label_nome = tk.Label(reg_window, text="Nome:")
    label_nome.pack(pady=5)
    entry_nome = tk.Entry(reg_window)
    entry_nome.pack(pady=5)

    label_corso = tk.Label(reg_window, text="Seleziona edificio:")
    label_corso.pack(pady=5)

    edifici = {}
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM edificio")
        for row in cursor.fetchall():
            edifici[row[1]] = row[0]  # chiave = nome corso, valore = id
        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Errore", "Connessione al database fallita!")
        reg_window.destroy()
        return
    edificio_var = tk.StringVar()
    combo_edifici = ttk.Combobox(
        reg_window,
        textvariable=edificio_var,
        values=list(edifici.keys()),
        state="readonly"  # obbligatorio per evitare input manuale
    )
    combo_edifici.pack(pady=5)
    combo_edifici.current(0)  # seleziona il primo elemento di default

    # Callback per aggiornare il valore selezionato
    def on_corso_selected(event):
        # aggiorna corso_var con il valore selezionato
        edificio_var.set(combo_edifici.get())

    combo_edifici.bind("<<ComboboxSelected>>", on_corso_selected)

    def aggiungiaula():
        nome = entry_nome.get()
        edificio_nome = edificio_var.get()
        ed = edifici.get(edificio_nome)

        if not nome:
            messagebox.showerror("Errore", "Inserisci il nome!")
            return
        if not ed:
            messagebox.showerror("Errore", "Seleziona un edificio!")
            return


            # Inserimento nel database
        conn = connect_to_db()

        try:
            cursor = conn.cursor()
            query = """
                       INSERT INTO aula (nome, fkedificio)
                       VALUES (%s, %s)
                   """
            cursor.execute(query, (nome, ed))
            conn.commit()
            messagebox.showinfo("Registrazione", "Edificio aggiunto con successo!")
        except Error as e:
            messagebox.showerror("Errore database", str(e))
        finally:
            cursor.close()
            conn.close()


        from login import login
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

    button_registra = tk.Button(frame_bottoni, text="Aggiungi", command=aggiungiaula)
    button_registra.pack(side=tk.LEFT, padx=10)

    reg_window.mainloop()

