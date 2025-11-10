#
from Amministratore import Amministratore
from Studente import Studente
from login import login


def main():

    utenti = []

    studente1 = Studente(
        nome="Giulia",
        cognome="Verdi",
        data_nascita="2000-05-15",
        codice_fiscale="VRDGLL00E55Z404A",
        email="giulia.verdi@email.com",
        matricola="123456",
        facolta="Ingegneria",
        password="password123"
    )

    studente2 = Studente(
        nome="Marco",
        cognome="Rossi",
        data_nascita="2001-09-10",
        codice_fiscale="RSSMRC01P10H501K",
        email="marco.rossi@email.com",
        matricola="654321",
        facolta="Informatica",
        password="securepass456"
    )

    admin1 = Amministratore(
        nome="Luca",
        cognome="Bianchi",
        data_nascita="1985-11-20",
        codice_fiscale="BNCLCU85S20E404H",
        email="luca.bianchi@azienda.com",
        id_amministratore="ADM1001",
        password = "password123"
    )

    # Aggiungiamo gli utenti alla lista
    utenti.append(studente1)
    utenti.append(studente2)
 #   utenti.append(admin1)

    # Mostriamo i dati di tutti gli utenti
    print("Elenco utenti:")
    for utente in utenti:
        print(utente)

    login(utenti)

if __name__ == "__main__":
    main()
