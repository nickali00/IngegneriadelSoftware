from Persona import Persona

class Studente(Persona):
    def __init__(self, nome, cognome, data_nascita, codice_fiscale, email, matricola, facolta, password):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, email)
        self.matricola = matricola
        self.facolta = facolta
        self.password = password

    def __str__(self):
        return (f"Studente: {self.nome} {self.cognome}, Facoltà: {self.facolta}, "
                f"Matricola: {self.matricola}, Email: {self.email}")

    def saluta(self):
        print(f"Benvenuto  {self.nome} {self.cognome}!")