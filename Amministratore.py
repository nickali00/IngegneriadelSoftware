from Persona import Persona


class Amministratore(Persona):
    def __init__(self, nome, cognome, data_nascita, codice_fiscale, email, id_amministratore, password):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, email,password)
        self.id_amministratore = id_amministratore

    def __str__(self):
        return (f"Amministratore: {self.nome} {self.cognome}, ID: {self.id_amministratore}, "
                f"Email: {self.email}")
