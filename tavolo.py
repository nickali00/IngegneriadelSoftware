class Tavolo:
    def __init__(self, id, numero_postazioni):

        self.id = id
        self.numero_postazioni = numero_postazioni

    def __str__(self):
        return f" id: {self.id}, numero postazioni: {self.numero_postazioni}"
