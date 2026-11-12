def buscarAgregarEquipo(elemento):
    if elemento not in equipos:
        equipos.append(elemento)
        ganados.append(0)
        empates.append(0)
        perdidos.append(0)
        golesFavor.append(0)
        golesContra.append(0)

    return equipos.index(elemento)

def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbujaFecha(goles, ganadores):

    for a in range(len(goles) - 1):
        for b in range(a + 1, len(goles)):
            if (goles[a] < goles[b]):
                intercambiar(goles, a, b)
                intercambiar(ganadores, a, b)

def burbujaTabla():
    for a in range(len(equipos) - 1):
        for b in range(a + 1, len(equipos)):
            puntosA = ganados[a] * 3 + empates[a]
            puntosB = ganados[b] * 3 + empates[b]

            diferenciaA = golesFavor[a] - golesContra[a]
            diferenciaB = golesFavor[b] - golesContra[b]

            if (puntosA < puntosB):
                intercambiar(equipos, a, b)
                intercambiar(ganados, a, b)
                intercambiar(empates, a, b)
                intercambiar(perdidos, a, b)
                intercambiar(golesFavor, a, b)
                intercambiar(golesContra, a, b)

            elif (puntosA == puntosB):
                if (diferenciaA < diferenciaB):
                    intercambiar(equipos, a, b)
                    intercambiar(ganados, a, b)
                    intercambiar(empates, a, b)
                    intercambiar(perdidos, a, b)
                    intercambiar(golesFavor, a, b)
                    intercambiar(golesContra, a, b)

                elif (diferenciaA == diferenciaB):
                    if (golesFavor[a] < golesFavor[b]):
                        intercambiar(equipos, a, b)
                        intercambiar(ganados, a, b)
                        intercambiar(empates, a, b)
                        intercambiar(perdidos, a, b)
                        intercambiar(golesFavor, a, b)
                        intercambiar(golesContra, a, b)

def verTabla():
    for i in range(len(equipos)):
        partidos = ganados[i] + empates[i] + perdidos[i]
        puntos = ganados[i] * 3 + empates[i]
        diferencia = golesFavor[i] - golesContra[i]

        print(f"Equipo: {equipos[i]}")
        print(f"Partidos jugados: {partidos}")
        print(f"Puntos: {puntos}")
        print(f"Partidos ganados: {ganados[i]}")
        print(f"Partidos perdidos: {perdidos[i]}")
        print(f"Partidos empatados: {empates[i]}")
        print(f"Goles a favor: {golesFavor[i]}")
        print(f"Goles en contra: {golesContra[i]}")
        print(f"Diferencia de goles: {diferencia}")

        print("-" * 20)

def revisarFecha(fecha, arch):
    print(f"=== Resultados {fecha} ===")

    golesFecha = []
    ganadoresFecha = []

    for i in range(4):
        linea = arch.readline().strip()
        partes = linea.split(",")

        equipo1 = partes[0]
        idx1 = buscarAgregarEquipo(equipo1)
        goles1 = int(partes[2])

        equipo2 = partes[1]
        idx2 = buscarAgregarEquipo(equipo2)
        goles2 = int(partes[3])

        golesFecha.append(goles1 + goles2)
        golesFavor[idx1] += goles1
        golesContra[idx1] += goles2
        golesFavor[idx2] += goles2
        golesContra[idx2] += goles1


        if (goles1 > goles2):
            ganador = equipo1
            ganados[idx1] += 1
            perdidos[idx2] += 1
            

        elif (goles1 < goles2):
            ganador = equipo2
            ganados[idx2] += 1
            perdidos[idx1] += 1

        else:
            ganador = "Empate"
            empates[idx1] += 1
            empates[idx2] += 1

        ganadoresFecha.append(f"{equipo1} ({goles1}) VS {equipo2} ({goles2}) -> Ganador: {ganador}")

    burbujaFecha(golesFecha, ganadoresFecha)
    burbujaTabla()

    for i in range(len(golesFecha)):
        print(f"Goles totales: {golesFecha[i]} | {ganadoresFecha[i]}")
    print()
    verTabla()

def masGoleador():
    mayor = 0
    for i in range(len(equipos)):
        if golesFavor[i] > golesFavor[mayor]:
            mayor = i
    return equipos[mayor]

def masGoleado():
    mayor = 0
    for i in range(len(equipos)):
        if golesContra[i] > golesContra[mayor]:
            mayor = i
    return equipos[mayor]

def promedioGoles():
    totalGoles = 0
    totalPartidos = 0
    for i in range(len(equipos)):
        totalGoles += golesFavor[i]
        totalPartidos += ganados[i] + empates[i] + perdidos[i]

    # cada partido se cuenta 2 veces (una por cada equipo)
    totalPartidos = totalPartidos // 2
    return round(totalGoles / totalPartidos, 2)

arch = open("partidos.txt","r",encoding="utf-8")
linea = arch.readline().strip()

equipos = []
ganados = []
empates = []
perdidos = []
golesFavor = []
golesContra = []

while (linea != ""):
    fecha = linea

    revisarFecha(fecha, arch)

    linea = arch.readline().strip()
    
print("=== TABLA FINAL ===")
verTabla()

print()
print("=== Podio ===")
print(f"Primer Lugar: {equipos[0]}")
print(f"Segundo Lugar: {equipos[1]}")
print(f"Tercer Lugar: {equipos[2]}")

print()
print(f"Equipo más goleador: {masGoleador()}")
print(f"Equipo más goleado: {masGoleado()}")
print(f"Promedio de goles: {promedioGoles()}")