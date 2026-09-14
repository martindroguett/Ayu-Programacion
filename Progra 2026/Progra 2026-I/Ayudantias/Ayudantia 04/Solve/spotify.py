
arch = open("playlist.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

cantCanciones = 0

mayorDuracion = -1
cancionMayorDuracion = ""

masEscuchada = -1
cancionMasEscuchada = ""

while linea != "":
    partes = linea.split(",")
    id = partes[0]
    cancion = partes[1]
    album = partes[2]
    minutosSegundos = partes[3]
    partesDuracion = minutosSegundos.split(".")
    duracion = int(partesDuracion[0]) * 60 + int(partesDuracion[1]) 
    rating = int(partes[4])
    fecha = partes[5]
    cantEscuchada = int(partes[6])

    if duracion > mayorDuracion:
        mayorDuracion = duracion
        cancionMayorDuracion = cancion
    
    if cantEscuchada > masEscuchada:
        masEscuchada = cantEscuchada
        cancionMasEscuchada = cancion

    cantCanciones += 1

    linea = arch.readline().strip()

print("Estadísticas")
print(f"a) Cantidad de canciones en la playlist: {cantCanciones}")
print(f"b) Cancion de mayor duración: {cancionMayorDuracion} -> {mayorDuracion} segundos.")
print(f"c) Cancion más escuchada: {cancionMasEscuchada} -> {masEscuchada} veces")
