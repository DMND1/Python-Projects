### Dati ###
# Liste degli orari
orari_autobus_1_direzione_terminal = [712, 722, 747, 822, 842, 905, 945, 1025, 1105, 1145, 1225, 1305, 1345, 1402, 1425, 1505, 1545, 1625, 1705, 1745, 1825, 1905, 1945, 2025, 2120]
orari_autobus_1_direzione_università = [600, 715, 740, 800, 820, 900, 940, 1020, 1100, 1140, 1300, 1340, 1420, 1500, 1540, 1620, 1700, 1740, 1820, 1900, 1940, 2020]

# Dizionari per ogni autobus
autobus_1 = {"terminal": orari_autobus_1_direzione_terminal, "università": orari_autobus_1_direzione_università}

# Liste dei dizionari degli autobus con relativo nome
tutti_gli_autobus =  {"Autobus 1": autobus_1}



### Prima scelta: orario partenza (alla fermata) ###
print("Scegliere tra:" + "\n" + "1: per usare l'orario corrente" + "\n" + "2: per inserire l'orario di partenza desiderato")
scelta = int(input("Scelta: "))

if scelta == 1:
    from datetime import datetime
    now = datetime.now()
    tempo_scelto = now.strftime("%H%M")
elif scelta == 2:
    tempo_scelto = input("Inserire l'orario di partenza desiderato (formato di es: 730 oppure 7:30): ")

tempo_scelto = tempo_scelto.replace(":", "")
tempo_scelto = int(tempo_scelto)

# Stampa dell'orario corrente
print("Orario corrente:", tempo_scelto)



### Seconda scelta: direzione ###
print("Scegliere tra:" + "\n" + "1: direzione Università" + "\n" + "2: direzione Terminal")
scelta = int(input("Scelta: "))

if scelta == 1:
    direzione = "università"
elif scelta == 2:
    direzione = "terminal"



### Calcolo degli orari e stampa ###
for autobus in tutti_gli_autobus:
        l = []
        
        for orario in tutti_gli_autobus[autobus][direzione]:
            if orario >= tempo_scelto and len(l) < 5:
                l.append(orario)

        if l == []:
            print(autobus + ": non ci sono più orari disponibili")
        else:
            print("Orari", autobus + ":", l)