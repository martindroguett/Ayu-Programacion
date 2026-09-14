def check_gol(pelota, largo, movx):

    if (pelota[0] + movx <= 0) or (pelota[0] + movx >= largo - 1):
        return True

    return False


def lateral(pelota, ancho, movy):

    if pelota[1] + movy < 0 or pelota[1] + movy > ancho - 1:
        return True

    return False


equipos = []
toques = []
puntos = []
goles_recibidos = []


arch = open("equipos.txt", "r", encoding="utf-8")

linea = arch.readline().strip()

while linea != "":
    if linea not in equipos:
        equipos.append(linea)
        toques.append(0)
        puntos.append(0)
        goles_recibidos.append(0)

    linea = arch.readline().strip()

arch.close()


arch = open("movimientos.txt", "r", encoding="utf-8")

linea = arch.readline().strip()

while linea != "":

    nombreFecha = linea
    print(nombreFecha)
    print()

    linea = arch.readline().strip()

    while linea != "" and "Fecha" not in linea:

        partes = linea.split(",")

        local = partes[0]
        visita = partes[1]
        ancho = int(partes[2])
        largo = int(partes[3])

        pelota = [largo // 2, ancho // 2]

        goles_local = 0
        goles_visita = 0

        linea = arch.readline().strip()

        if linea != "":
            partes = linea.split(",")
        else:
            partes = []

        while linea != "" and "Fecha" not in linea and len(partes) != 4:

            equipo = partes[0]
            movx = int(partes[1])
            movy = int(partes[2])

            pos_equipo = equipos.index(equipo)
            toques[pos_equipo] += 1

            if check_gol(pelota, largo, movx):

                if pelota[0] + movx <= 0:
                    goles_visita += 1
                else:
                    goles_local += 1

                pelota = [largo // 2, ancho // 2]

            else:

                pelota[0] += movx

                if lateral(pelota, ancho, movy):

                    if pelota[1] + movy < 0:
                        pelota[1] = 0
                    else:
                        pelota[1] = ancho - 1

                else:
                    pelota[1] += movy

            linea = arch.readline().strip()

            if linea != "":
                partes = linea.split(",")
            else:
                partes = []

        pos_local = equipos.index(local)
        pos_visita = equipos.index(visita)

        goles_recibidos[pos_local] += goles_visita
        goles_recibidos[pos_visita] += goles_local

        if goles_local > goles_visita:
            puntos[pos_local] += 3

        elif goles_visita > goles_local:
            puntos[pos_visita] += 3

        else:
            puntos[pos_local] += 1
            puntos[pos_visita] += 1

        print(local, goles_local, "-", goles_visita, visita)
        print()

arch.close()


equipos_copia = []

for equipo in equipos:
    equipos_copia.append(equipo)

puntos_copia = []

for punto in puntos:
    puntos_copia.append(punto)

podio = []
puntos_podio = []

i = 0

while i < 3:

    mayor = puntos_copia[0]
    pos_mayor = 0

    j = 1

    while j < len(puntos_copia):

        if puntos_copia[j] > mayor:
            mayor = puntos_copia[j]
            pos_mayor = j

        j += 1

    podio.append(equipos_copia[pos_mayor])
    puntos_podio.append(puntos_copia[pos_mayor])

    equipos_copia.pop(pos_mayor)
    puntos_copia.pop(pos_mayor)

    i += 1


mayor_toques = toques[0]
pos_mayor_toques = 0

i = 1

while i < len(toques):

    if toques[i] > mayor_toques:
        mayor_toques = toques[i]
        pos_mayor_toques = i

    i += 1


mayor_recibidos = goles_recibidos[0]
pos_mayor_recibidos = 0

i = 1

while i < len(goles_recibidos):

    if goles_recibidos[i] > mayor_recibidos:
        mayor_recibidos = goles_recibidos[i]
        pos_mayor_recibidos = i

    i += 1

print()
print("PODIO")
print("1° lugar:", podio[0], "-", puntos_podio[0], "puntos")
print("2° lugar:", podio[1], "-", puntos_podio[1], "puntos")
print("3° lugar:", podio[2], "-", puntos_podio[2], "puntos")

print()
print("Equipo con más toques:")
print(equipos[pos_mayor_toques], "-", mayor_toques, "toques")

print()
print("Equipo que recibió más goles:")
print(equipos[pos_mayor_recibidos], "-", mayor_recibidos, "goles recibidos")

