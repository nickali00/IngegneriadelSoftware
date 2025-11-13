#
from Amministratore import Amministratore
from Studente import Studente
from Aula_studio import Aulastudio 
from tavolo import Tavolo
from login import login


def main():
    # Creazione di 2 aule
    aula1 = Aulastudio("Sala A", 101, "Edificio Centrale", 10, 50)
    aula2 = Aulastudio("Sala B", 102, "Edificio Sud", 8, 40)

    # Inserimento in un vettore (lista)
    aule = [aula1, aula2]
    # Creazione di 2 tavoli per ciascuna aula
    tavolo1_aula1 = Tavolo(1, 10)
    tavolo2_aula1 = Tavolo(2, 10)
    # Mostriamo i dati di tutti gli utenti
    
    login()

if __name__ == "__main__":
    main()
