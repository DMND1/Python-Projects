### Dati ###
# Tuple degli orari
orari_autobus_1_direzione_terminal =        (712,  722,  747,  822,  842,  905,  945,  1025, 1105, 1145, 1225, 1305, 1345, 1402, 1425, 1505, 1545, 1625, 1705, 1745, 1825, 1905, 1945, 2025, 2120)
orari_autobus_1_direzione_università =      (715,  740,  800,  820,  900,  940,  1020, 1100, 1140, 1300, 1340, 1420, 1500, 1540, 1620, 1700, 1740, 1820, 1900, 1940, 2020)
orari_autobus_2U_2UT_direzione_terminal =   (1255, 1328, 1338, 1400, 1602, 1605, 1632, 1705, 1735, 1805, 1825, 1920)
orari_autobus_2U_2UT_direzione_università = (600,  730,  805,  810,  830,  845,  900,  915,  1010)
orari_autobus_3_direzione_terminal =        (610,  723,  750,  840,  920,  1000, 1040, 1120, 1205, 1240, 1320, 1400, 1440, 1520, 1600, 1640, 1715, 1755, 1835, 1915, 2010)
orari_autobus_3_direzione_università =      (715,  805,  845,  925,  1005, 1045, 1125, 1205, 1245, 1305, 1325, 1345, 1405, 1445, 1525, 1605, 1640, 1720, 1800, 1840, 1925, 2005)
orari_autobus_4_direzione_terminal =        (733,  813,  853,  933,  1013, 1053, 1133, 1213, 1258, 1333, 1413, 1453, 1533, 1613, 1653, 1728, 1808, 1848, 1928, 2013)
orari_autobus_4_direzione_università =      (735,  745,  815,  855,  935,  1015, 1055, 1135, 1215, 1255, 1335, 1415, 1455, 1535, 1615, 1650, 1730, 1810, 1850, 1935, 2015)
orari_autobus_6D_6S_direzione_terminal =    (858,  1003, 1108, 1213, 1318, 1423, 1528, 1633, 1743, 1843, 1948, 2008)
orari_autobus_6D_6S_direzione_università =  (630,  850,  910,  1015, 1120, 1225, 1330, 1435, 1540, 1645, 1750, 1900, 2000)
orari_autobus_15_direzione_terminal =       (737,  732,  852,  957,  1248, 1533, 1802)
orari_autobus_15_direzione_università =     (640,  750,  830,  855,  1240, 1320, 1405, 1410, 1700, 1835)
orari_autobus_19_direzione_terminal =       (831,  856,  1036, 1211, 1321, 1351, 1501, 1621, 1806, 1926)
orari_autobus_19_direzione_università =     (655,  750,  815,  850,  955,  1130, 1230, 1300, 1350, 1420, 1540, 1725, 1845)

# Dizionari per ogni autobus, ad ogni direzione tra "terminal" e "università" è associata la relativa tupla
autobus_1 =      {"terminal": orari_autobus_1_direzione_terminal,      "università": orari_autobus_1_direzione_università}
autobus_2U_2UT = {"terminal": orari_autobus_2U_2UT_direzione_terminal, "università": orari_autobus_2U_2UT_direzione_università}
autobus_3 =      {"terminal": orari_autobus_3_direzione_terminal,      "università": orari_autobus_3_direzione_università}
autobus_4 =      {"terminal": orari_autobus_4_direzione_terminal,      "università": orari_autobus_4_direzione_università}
autobus_6D_6S =  {"terminal": orari_autobus_6D_6S_direzione_terminal,  "università": orari_autobus_6D_6S_direzione_università}
autobus_15 =     {"terminal": orari_autobus_15_direzione_terminal,     "università": orari_autobus_15_direzione_università}
autobus_19 =     {"terminal": orari_autobus_19_direzione_terminal,     "università": orari_autobus_19_direzione_università}

# Dizionario dei dizionari degli autobus con relativo nome già formattato per la stampa
tutti_gli_autobus =  {
    "autobus 1:      ": autobus_1, 
    "autobus 2U/2UT: ": autobus_2U_2UT, 
    "autobus 4:      ": autobus_4, 
    "autobus 6D/6S:  ": autobus_6D_6S, 
    "autobus 3:      ": autobus_3, 
    "autobus 15:     ": autobus_15, 
    "autobus 19:     ": autobus_19
}



### Prima scelta: orario partenza (alla fermata) ###
print("Scegliere tra:" + "\n" + "1: per usare l'orario corrente" + "\n" + "2: per inserire l'orario di partenza desiderato")
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
    # Prendo come input orario_scelto
    orario_scelto = input("Inserire l'orario di partenza desiderato (formato accettato: 730 oppure 7:30): ")

# Rimuovo eventuali ":"
orario_scelto = orario_scelto.replace(":", "")
# Rendo orario_scelto un intero
orario_scelto = int(orario_scelto)

# Eventuale stampa dell'orario scelto
# print("Orario scelto:", orario_scelto)



### Seconda scelta: direzione ###
print("Scegliere tra:" + "\n" + "1: direzione Università, partenza dal Terminal" + "\n" + "2: direzione Terminal, partenza dall'Università")
scelta = int(input("Scelta: "))

# Se la scelta è 1
if scelta == 1:
    # Assegno alla variabile direzione "università"
    direzione = "università"
# Altrimenti se la scelta è 2
elif scelta == 2:
    # Assegno alla variabile direzione "terminal"
    direzione = "terminal"



### Eventuale scelta: numero di orari da visualizzare ###
# scelta = int(input("Inserire il numero di orari da visualizzare: "))
# numero_di_orari_da_visualizzare = scelta
numero_di_orari_da_visualizzare = 3



### Calcolo elenco degli orari e stampa ###
for autobus in tutti_gli_autobus:
        # Inizializzazione variabili
        risultato = ""
        contatore_orari_inseriti = 0
        # Per ogni orario nella tupla di autobus con la direzione scelta
        for orario in tutti_gli_autobus[autobus][direzione]:
            if orario >= orario_scelto and contatore_orari_inseriti < numero_di_orari_da_visualizzare:
                # Rendo orario una stringa e calcolo l'indice centrale di tale stringa
                orario = str(orario)
                posizione_due_punti = len(orario) // 2
                # Se il contatore è 0 non aggiunga una virgola iniziale al risultato
                if contatore_orari_inseriti == 0:
                    orario = orario[0:posizione_due_punti] + ":" + orario[posizione_due_punti:]
                # Altrimenti la aggiungo
                else:
                    orario = ", " + orario[0:posizione_due_punti] + ":" + orario[posizione_due_punti:]
                # Update variabili
                risultato += orario
                contatore_orari_inseriti += 1
        # Se il risultato è rimasto invariato, ossia non ci sono orari che soddisfano la richiesta
        if risultato == "":
            # Stampo che non ci sono orari disponibili
            risultato = "non ci sono orari disponibili"
            print("Orari", autobus, risultato)
        # Altrimenti stampo il risultato ottenuto
        else:
            print("Orari", autobus, risultato)



# Idee ancora da implementare: 
# - Aggiungere la scelta di quali autobus mostrare gli orari
# - Aggiungere l'opzione per scegliere se inserire l'orario desiderto di partenza oppure quello di arrivo
# - Aggiungere la possibilità di scegliere la stazione di partenza e quella di arrivo (con annesso calcolo della direzione)