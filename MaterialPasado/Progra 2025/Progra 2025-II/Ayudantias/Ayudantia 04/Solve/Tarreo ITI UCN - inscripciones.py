archivo = open("inscripciones.txt", "r", encoding="utf-8")

# Variables para guardar totales
total_ucn_evento = 0
total_participantes_evento = 0

# Variables para identificar juegos con menos equipos / menos UCN
menor_equipos = 0
juego_menor_equipos = ""
menor_ucn = 0
juego_menor_ucn = ""

print("Porcentaje de participación UCN por juego:")

linea = archivo.readline()   # leer primera línea
while linea != "":           # mientras no sea fin del archivo
    partes = linea.strip().split(", ")
    nombre = partes[0]

    if nombre == "Super Smash Bros Ultimate":
        inscritos = int(partes[1])
        equipos = inscritos
        tam_equipo = 1
        ucn = inscritos
    else:
        equipos = int(partes[1])

        # Determinar tamaño de equipo
        if nombre == "League of Legends" or nombre == "Valorant":
            tam_equipo = 5
        elif nombre == "Rocket League":
            tam_equipo = 3
        else:
            tam_equipo = 1

        # Contar alumnos UCN de esta línea
        ucn = 0
        for i in range(2, equipos + 2):
            ucn = ucn + int(partes[i])

    # Calcular participantes de este juego
    participantes = equipos * tam_equipo
    porcentaje = ucn * 100.0 / participantes
    print(nombre, ":", round(porcentaje, 2), "%")

    # Acumular para el evento completo
    total_ucn_evento = total_ucn_evento + ucn
    total_participantes_evento = total_participantes_evento + participantes

    # Buscar juego con menos equipos (solo juegos en equipo)
    if juego_menor_equipos == "":
        menor_equipos = participantes
        juego_menor_equipos = nombre
    elif participantes < menor_equipos:
        menor_equipos = participantes
        juego_menor_equipos = nombre

    # Buscar juego con menos UCN
    if juego_menor_ucn == "":
        menor_ucn = ucn
        juego_menor_ucn = nombre
    elif ucn < menor_ucn:
        menor_ucn = ucn
        juego_menor_ucn = nombre

    # leer siguiente línea
    linea = archivo.readline()

archivo.close()

# Porcentaje total en el evento
porcentaje_evento = total_ucn_evento * 100.0 / total_participantes_evento
print()
print("Porcentaje total UCN en el evento:", round(porcentaje_evento, 2), "%")

print()
print("Juego con menor cantidad de participantes:", juego_menor_equipos)
print("Juego con menor participación UCN:", juego_menor_ucn)
