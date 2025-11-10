class Persona:
    def __init__(self, nome, cognome, data_nascita, codice_fiscale, email):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.codice_fiscale = codice_fiscale
        self.email = email

    def __str__(self):
        return f"{self.nome} {self.cognome}, Nata il: {self.data_nascita}, Codice Fiscale: {self.codice_fiscale}, Email: {self.email}"
