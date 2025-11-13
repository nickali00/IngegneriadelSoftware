from Persona import Persona

class Studente(Persona):
    def __init__(self, nome, cognome, data_nascita, codice_fiscale, email, password, matricola, facolta):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, email, password)
        self.matricola = matricola
        self.facolta = facolta


    def __str__(self):
        return (f"Studente: {self.nome} {self.cognome}, Facoltà: {self.facolta}, "
                f"Matricola: {self.matricola}, Email: {self.email}")

    def saluta(self):
        print(f"Benvenuto  {self.nome} {self.cognome}!")