### Updates ###
# ver: 1.3:
# - Aggiunta dell'opzione per scegliere se inserire l'orario di partenza oppure quello di arrivo



### Dati ###
import json

with open('Autobus-ver1.4/data.json', 'r') as file:
    data = json.load(file)



### Funzioni ###
def calcoloOrarioMassimo(orario_di_arrivo, autobus):

    ore = orario_di_arrivo // 100
    minuti = orario_di_arrivo % 100

    if minuti > data["durata_tragitto"][autobus]:
        orario_di_arrivo_finale = ore * 100 + minuti - data["durata_tragitto"][autobus]
    else:
        minuti_totali = minuti + ore * 60
        minuti_totali = minuti_totali - data["durata_tragitto"][autobus]

        ore = minuti_totali // 60
        minuti = minuti_totali % 60

        orario_di_arrivo_finale = ore * 100 + minuti

    return orario_di_arrivo_finale

def calcoloRisultato(lista_orari_da_stampare):
    risultato = ""
    contatore_orari_inseriti = 0

    if len(lista_autobus_da_mostrare) > 3:
        estremo = max(len(lista_orari_da_stampare), 3) - 3
        lista_orari_da_stampare = lista_orari_da_stampare[estremo:len(lista_orari_da_stampare)]

    for orario in lista_orari_da_stampare:
        # Rendo orario una stringa e calcolo l'indice centrale di tale stringa
        orario = str(orario)
        posizione_due_punti = len(orario) // 2
        # Se il contatore è 0 non aggiunga una virgola iniziale al risultato
        if contatore_orari_inseriti == 0:
            risultato += orario[0:posizione_due_punti] + ":" + orario[posizione_due_punti:]
        # Altrimenti la aggiungo
        else:
            risultato += ", " + orario[0:posizione_due_punti] + ":" + orario[posizione_due_punti:]
        contatore_orari_inseriti += 1
    
    return risultato

# Procedura in questo caso
def stampaOrari(risultato, autobus):
    # Se il risultato è rimasto invariato, ossia non ci sono orari che soddisfano la richiesta
    if risultato == "":
        # Stampo che non ci sono orari disponibili
        risultato = "non ci sono orari disponibili"
        print("Orari autobus", autobus + ":", risultato)
    # Altrimenti stampo il risultato ottenuto
    elif risultato != "Ciao ;)":
        print("Orari autobus", autobus + ":", risultato, "- durata del tragitto:", data["durata_tragitto"][autobus], "minuti")
        # Altrimenti se il risultato == "Ciao ;)":
        # Vuol dire che non devo mostrare gli orari di questo autobus, quindi non stampo nulla



### Inizio programma ###
run = "DMND"

while run != "stop":
    ### Prima scelta: inserire l'orario desiderto di partenza oppure quello di arrivo ###
    print("Scegliere tra: 1, 2" + "\n" + "1: per scegliere l'orario di partenza desiderato" + "\n" + "2: per scegliere l'orario di arrivo desiderato")
    scelta = int(input("Scelta: "))

    orario_di_partenza = False
    orario_di_arrivo = False

    if scelta == 1:
        orario_di_partenza = True
    elif scelta == 2:
        orario_di_arrivo = True

    if orario_di_partenza:
        ### Eventuale seconda scelta: orario partenza (alla fermata) ###
        print("\n" + "Scegliere tra: 1, 2" + "\n" + "1: per usare l'orario corrente" + "\n" + "2: per inserire l'orario di partenza desiderato")
        scelta = int(input("Scelta: "))

        # Se la scelta è 1
        if scelta == 1:
            # Importo la libreria datetime
            from datetime import datetime
            # Inizializzazione variabili
            now = datetime.now()
            # Assegnazione della stringa dell'orario corrente (calcolata grazie alla funzione datetime.now()) a orario_scelto
            orario_scelto = now.strftime("%H%M")
        # Altrimenti se la scelta è 2
        elif scelta == 2:
            print("\n" + "Inserire l'orario di partenza desiderato (formato accettato: 730 oppure 7:30): ")
            # Prendo come input orario_scelto
            orario_scelto = input("Scelta: ")

    elif orario_di_arrivo:
        print("\n" + "Inserire l'orario di arrivo desiderato (formato accettato: 730 oppure 7:30): ")
        orario_scelto = input("Scelta: ")

    # Rimuovo eventuali ":"
    orario_scelto = orario_scelto.replace(":", "")
    # Rendo orario_scelto un intero
    orario_scelto = int(orario_scelto)

    # Eventuale stampa dell'orario scelto
    # print("Orario scelto:", orario_scelto)



    ### Terza scelta: direzione ###
    print("\n" + "Scegliere tra: 1, 2" + "\n" + "1: direzione Università, partenza dal Terminal" + "\n" + "2: direzione Terminal, partenza dall'Università")
    scelta = int(input("Scelta: "))

    # Se la scelta è 1
    if scelta == 1:
        # Assegno alla variabile direzione "università"
        direzione = "universita"
    # Altrimenti se la scelta è 2
    elif scelta == 2:
        # Assegno alla variabile direzione "terminal"
        direzione = "terminal"



    ### Quarta scelta: quali autobus mostrare ###
    print("\n" + "Scegliere quali autobus mostrare tra: 1, 2U/2UT, 3, 4, 6D/6S, 15, 19, 'tutti'" + "\n" + "(formato accettato: 1, 2U/2UT)")
    scelta = input("Scelta: ")
    scelta = scelta.replace("'", "")
    print()

    # Se la scelta non è tutti
    if scelta != "tutti":
        # Rimuovo le virgole
        scelta = scelta.replace(",", "")
        # Aggiungo uno spazio alla fine
        scelta += " "
        # Inizializzazione variabili
        lista_autobus_da_mostrare = []
        contatore = 0

        # Per ogni i (indice) da 1 a len(scelta)
        for i in range(1, len(scelta)):
            # Se il carattere di tale indice i è uguale a " "
            if scelta[i] == " ":
                # Aggiungo alla lista degli autobus da mostrare i caratteri che vanno da contatore a i (escluso)
                lista_autobus_da_mostrare.append(scelta[contatore:i])
                # Update variabili
                contatore = i + 1
    else:
        lista_autobus_da_mostrare = ["1", "2U/2UT", "3", "4", "6D/6S", "15", "19"]



    ### Eventuale scelta: numero di orari da visualizzare ###
    # scelta = int(input("Inserire il numero di orari da visualizzare: "))
    # numero_di_orari_da_visualizzare = scelta
    numero_di_orari_da_visualizzare = 3



    ### Calcolo elenco degli orari e stampa ###
    for autobus in data["tutti_gli_autobus"]:
        # Inizializzazione variabili
        orario_da_non_superare = calcoloOrarioMassimo(orario_scelto, autobus)
        risultato = "Ciao ;)"
        # Se autobus si trova anche nella lista di autobus da mostrare
        if autobus in lista_autobus_da_mostrare:
            # Inizializzazione variabili
            lista_orari_da_stampare = []
            # Per ogni orario nella tupla di autobus con la direzione scelta
            for orario in data["tutti_gli_autobus"][autobus][direzione]:
                # Se l'orario è più grande dell'orario scelto e se il contatore non ha superato il numero di orari da visualizzare
                if orario_di_partenza and orario >= orario_scelto and len(lista_orari_da_stampare) < numero_di_orari_da_visualizzare:
                    # Update variabili
                    lista_orari_da_stampare.append(orario)
                # Altrimenti se è stato scelto l'orario di arrivo
                elif orario_di_arrivo and orario <= orario_da_non_superare:
                    # Update variabili
                    lista_orari_da_stampare.append(orario)
            # Calcolo risultato
            risultato = calcoloRisultato(lista_orari_da_stampare)
        # Stampo il risultato
        stampaOrari(risultato, autobus)

    print()
    run = input("Scrivere 'stop' per fermare il programma, altrimenti inserire qualsiasi carettere per continuare: ")
    run = run.lower()
    run = run.replace("'", "")
    print()


# Idee ancora da implementare:
# - Mettere i dati dentro un file e leggerli da quel file
# - Aggiungere la possibilità di scegliere la stazione di partenza e quella di arrivo (con annesso calcolo della direzione)