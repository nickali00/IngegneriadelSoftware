import tkinter as tk
from tkinter import messagebox

# Funzione di login
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Simuliamo un controllo di login (ad esempio, confrontando con un utente hardcoded)
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login", "Login riuscito!")
    else:
        messagebox.showerror("Login", "Username o password errati!")

root = tk.Tk()
root.title("Login")

root.geometry("300x250")

label_username = tk.Label(root, text="Nome utente:")
label_username.pack(pady=10)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")  # show="*" nasconde la password
entry_password.pack(pady=5)


button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

root.mainloop()
