from datetime import datetime

# Orario corrente
now = datetime.now()
current_time = int(now.strftime("%H%M"))

# Stampa dell'orario corrente
print("Orario corrente: ", current_time)

# Liste degli orari
autobus_1_direzione_terminal = [1145, 1225, 1305]
autobus_1_direzione_aquilone = [1110, 1140, 1220]

# Liste degli autobus con la stessa direzione
direzione_terminal = [autobus_1_direzione_terminal]
direzione_aquilone = [autobus_1_direzione_aquilone]

# Input direzione
direzione = input("Inserire una direzione a scelta tra Aquilone o Terminal: ")
direzione = direzione.lower()

# Controllo input
while direzione != "aquilone" or direzione != "terminal":
    direzione = input("Input invalido, inserire una direzione a scelta tra Aquilone o Terminal: ")
    direzione = direzione.lower()


if direzione == "terminal":
    lista_orari = []
elif direzione == "aquilone":
    lista_orari = []