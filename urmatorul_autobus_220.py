from datetime import datetime, timedelta

# Orarul pentru Luni-Vineri, ruta Brasov -> Codlea (hh:mm)
orar_brasov_codlea_saptamana = [
    "05:00", "05:30", "06:05", "06:25", "06:51", "07:20", "07:38", "08:01", "08:30", 
    "09:10", "09:35", "10:20", "10:40", "11:45", "12:10", "12:25", "12:55", "13:15", 
    "13:35", "14:00", "14:25", "14:45", "15:20", "15:45", "16:00", "16:21", "16:55", 
    "17:10", "17:35", "18:10", "18:40", "19:15", "19:50", "20:25", "21:00", "21:35", 
    "22:10", "22:50"
]

# Orarul pentru Sambata-Duminica, ruta Brasov -> Codlea (hh:mm)
orar_brasov_codlea_weekend = [
    "05:25", "06:35", "07:45", "08:59", "10:05", "11:15", "12:25", "13:35", "14:45", 
    "15:55", "17:05", "18:19", "19:25", "20:35", "21:45", "22:55"
]

# Orarul pentru Luni-Vineri, ruta Codlea -> Brasov (hh:mm)
orar_codlea_brasov_saptamana = [
    "05:35", "06:10", "06:45", "07:01", "07:31", "07:55", "08:18", "08:41", "09:05", 
    "09:50", "10:15", "11:15", "11:35", "12:25", "12:45", "13:05", "13:35", "13:55", 
    "14:15", "14:41", "15:20", "15:35", "15:55", "16:25", "16:40", "17:01", "17:35", 
    "17:50", "18:11", "18:50", "19:20", "19:55", "20:30", "21:05", "21:40", "22:15", 
    "22:50", "23:30"
]

# Orarul pentru Sambata-Duminica, ruta Codlea -> Brasov (hh:mm)
orar_codlea_brasov_weekend = [
    "06:05", "07:15", "08:25", "09:35", "10:45", "11:55", "13:05", "14:15", "15:25", 
    "16:35", "17:45", "18:55", "20:05", "21:15", "22:25", "23:35"
]

# Convertim string-urile de oră în obiecte datetime pentru comparații
def convert_to_datetime(orar, today):
    return [today.replace(hour=int(hh.split(":")[0]), minute=int(hh.split(":")[1]), second=0, microsecond=0) for hh in orar]

# Funcție pentru calcularea timpului până la următorul autobuz
def timpul_pana_la_urmatorul_autobuz(orar_saptamana, orar_weekend):
    # Obținem data și ora curentă
    now = datetime.now()
    
    # Verificăm dacă este weekend (Sâmbătă = 5, Duminică = 6) sau zi lucrătoare
    if now.weekday() >= 5:  # 5 = Sâmbătă, 6 = Duminică
        orar_curent = convert_to_datetime(orar_weekend, now)
    else:
        orar_curent = convert_to_datetime(orar_saptamana, now)
    
    # Căutăm următorul autobuz
    for ora_autobuz in orar_curent:
        if ora_autobuz > now:
            timpul_ramas = ora_autobuz - now  # Calculăm timpul rămas
            
            # Extragem orele și minutele
            ore_ramas = timpul_ramas.seconds // 3600
            minute_ramas = (timpul_ramas.seconds % 3600) // 60

            print(f"Următorul autobuz pleacă la ora {ora_autobuz.strftime('%H:%M')}. Timp rămas: {ore_ramas} ore și {minute_ramas} minute.")
            return
    
    # Dacă nu mai sunt autobuze în ziua curentă
    print("Nu mai sunt autobuze disponibile astăzi.")

# Funcția principală care cere direcția și calculează timpul în funcție de aceasta
def main():
    # Întrebăm utilizatorul în ce direcție vrea să meargă
    directie = input("În ce direcție doriți să călătoriți? (1 = Brașov -> Codlea, 2 = Codlea -> Brașov): ")
    
    if directie == "1":
        # Calculăm timpul pentru ruta Brașov -> Codlea
        timpul_pana_la_urmatorul_autobuz(orar_brasov_codlea_saptamana, orar_brasov_codlea_weekend)
    elif directie == "2":
        # Calculăm timpul pentru ruta Codlea -> Brașov
        timpul_pana_la_urmatorul_autobuz(orar_codlea_brasov_saptamana, orar_codlea_brasov_weekend)
    else:
        print("Opțiune invalidă. Te rog să alegi 1 sau 2.")

# Apelăm funcția principală
main()