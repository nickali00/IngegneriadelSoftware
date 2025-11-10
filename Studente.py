class Studente:
    def __init__(self, nome, cognome, data, matricola, codicefiscale , email, facolta, password):
        self.nome = nome
        self.cognome = cognome
        self.data = data
        self.matricola = matricola
        self.codicefiscale = codicefiscale
        self.email = email
        self.facolta = facolta
        self.password = password
    def __str__(self):
        return f"Studente: {self.nome} {self.cognome}, data di nascita: {self.data}, matricola: {self.matricola}, codice fiscale: {self.codicefiscale}, email: {self.email}, facoltà: {self.facolta}, password: {self.password}"

    def saluta(self):
        print(f"Benvenuto  {self.nome} {self.cognome}!")


