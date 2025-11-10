class Aulastudio:
    def __init__(self, nome, id, edificio, numero_tavoli, numero_postazioni):
        self.nome = nome
        self.id = id
        self.edificio = edificio
        self.numero_tavoli = numero_tavoli
        self.numero_postazioni = numero_postazioni

    def __str__(self):
        return f"{self.nome} {self.edificio}, id: {self.id}, numero tavoli: {self.numero_tavoli}, numero postazioni: {self.numero_postazioni}"
