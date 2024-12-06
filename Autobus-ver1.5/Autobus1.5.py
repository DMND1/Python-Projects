### Updates ###
# ver: 1.5:
# - Aggiunta la formattazione dell'output



### Dati ###
from json import load

with open('Autobus-ver1.4/data.json', 'r') as file:
    data = load(file)



### Funzioni ###
def calcoloOrarioMassimo(orario_di_arrivo, autobus):
    # Conversione di orario di arrivo in ore e minuti
    ore = orario_di_arrivo // 100
    minuti = orario_di_arrivo % 100
    # Se i minuti sono maggiori della durata del tragitto
    if minuti > data["durata_tragitto"][autobus]:
        # Non è necessario fare il calcolo che segue l'else e quindi ritorno questo:
        orario_di_arrivo_finale = ore * 100 + minuti - data["durata_tragitto"][autobus]
    # Altrimneti
    else:
        # Calcolo delle nuove variabili
        minuti_totali = minuti + ore * 60
        minuti_totali = minuti_totali - data["durata_tragitto"][autobus]
        ore = minuti_totali // 60
        minuti = minuti_totali % 60
        orario_di_arrivo_finale = ore * 100 + minuti

    return orario_di_arrivo_finale

# Procedura in questo caso
def calcoloRisultatoEStampa(lista_orari, autobus, bool):
    # Inizializzazione variabili
    risultato = ""
    contatore_orari_inseriti = 0
    # Controllo se la lista ha più di 3 elementi
    # Se la lista ha più di tre elementi e la variabile bool (orario_di_arrivo) è vera
    if len(lista_orari) > 3 and bool:
        # Faccio in modo che la lista abbia solo gli ultimi 3 elementi 
        # (orario_di_arrivo: devo mostrare gli orari più vicini a tale orario - durata_tragitto)
        estremo = max(len(lista_orari), 3) - 3
        lista_orari = lista_orari[estremo:len(lista_orari)]
    # Altrimenti se la lista ha più di tre elementi e la variabile bool (orario_di_arrivo) è falsa
    elif len(lista_orari) > 3 and not bool:
        # Faccio in modo che la lista abbia solo i primi 3 elementi
        estremo = min(len(lista_orari), 3)
        lista_orari = lista_orari[:estremo]
    # Ciclo di conversione orario e aggiunta di tale stringa al risultato
    for orario in lista_orari:
        # Rendo orario una stringa e calcolo l'indice centrale di tale stringa
        orario = str(orario)
        posizione_due_punti = len(orario) // 2
        # Se il contatore è 0 non aggiunga una virgola iniziale al risultato
        if contatore_orari_inseriti == 0:
            risultato += orario[0:posizione_due_punti] + ":" + orario[posizione_due_punti:]
        # Altrimenti la aggiungo
        else:
            risultato += ", " + orario[0:posizione_due_punti] + ":" + orario[posizione_due_punti:]
        # Update variabili
        contatore_orari_inseriti += 1

    # Larghezza massima del nome dell'autobus
    larghezza_autobus = 8
    larghezza_orari = 20

    # Se il risultato è rimasto invariato, ossia non ci sono orari che soddisfano la richiesta
    if risultato == "":
        # Stampo che non ci sono orari disponibili
        risultato = "non ci sono orari disponibili"
        print(f"Orari autobus {autobus + ":":<{larghezza_autobus}} {risultato}")
    # Altrimenti stampo il risultato ottenuto
    else:
        print(
            f"Orari autobus {autobus + ":":<{larghezza_autobus}} {risultato:<{larghezza_orari}}"
            f" - durata del tragitto: {data['durata_tragitto'][autobus]} minuti"
        )



### Inizio programma ###
run = "DMND"

while run != "stop":
    ### Prima scelta: inserire l'orario desiderto di partenza oppure quello di arrivo ###
    print("Scegliere tra: 1, 2" + "\n" + "1: per scegliere l'orario di partenza desiderato" + "\n" + "2: per scegliere l'orario di arrivo desiderato")
    scelta = int(input("Scelta: "))

    orario_di_partenza = False
    orario_di_arrivo = False
    # Se la scelta è 1
    if scelta == 1:
        orario_di_partenza = True
    # Altrimenti se la scelta è 2
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
        # Se autobus si trova anche nella lista di autobus da mostrare
        if autobus in lista_autobus_da_mostrare:
            # Inizializzazione variabili
            lista_orari_da_stampare = []
            # Per ogni orario nella tupla di autobus con la direzione scelta
            for orario in data["tutti_gli_autobus"][autobus][direzione]:
                # Se l'orario è più grande dell'orario scelto e se il contatore non ha superato il numero di orari da visualizzare
                if orario_di_partenza and orario >= orario_scelto:
                    # Update variabili
                    lista_orari_da_stampare.append(orario)
                # Altrimenti se è stato scelto l'orario di arrivo
                elif orario_di_arrivo and orario <= orario_da_non_superare:
                    # Update variabili
                    lista_orari_da_stampare.append(orario)
            # Calcolo e stampo il risultato
            calcoloRisultatoEStampa(lista_orari_da_stampare, autobus, orario_di_arrivo)

    print()
    run = input("Scrivere 'stop' per fermare il programma, altrimenti inserire qualsiasi carettere per continuare: ")
    run = run.lower()
    run = run.replace("'", "")
    run = run.replace(" ", "")
    print()

file.close()



# Idee ancora da implementare:
# - Aggiungere la possibilità di scegliere la stazione di partenza e quella di arrivo (con annesso calcolo della direzione)