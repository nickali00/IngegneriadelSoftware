class Studente:
    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola

    def __str__(self):
        return f"Studente: {self.nome} {self.cognome}, Età: {self.eta}, Matricola: {self.matricola}"

    def saluta(self):
        print(f"Ciao, sono {self.nome} {self.cognome}!")


