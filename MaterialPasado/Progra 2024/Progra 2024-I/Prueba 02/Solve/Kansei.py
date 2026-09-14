def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbuja(datos, tiempos):
    for a in range(len(tiempos)-1):
        for b in range(a+1, len(tiempos)):
            if tiempos[a] > tiempos[b]:
                intercambiar(tiempos, a, b)
                intercambiar(datos, a, b)

def añadirPiloto(datosPiloto, año, tiempo, lista1960_1979, tiempos1960_1979, lista1980_1999, tiempos1980_1999, lista2000_2019, tiempos2000_2019, cantParticipantes):
    if año >= 1960 and año <= 1979:
        lista1960_1979.append(datosPiloto)
        tiempos1960_1979.append(tiempo)
        cantParticipantes[0] += 1
    elif año >= 1980 and año <= 1999:
        lista1980_1999.append(datosPiloto)
        tiempos1980_1999.append(tiempo)
        cantParticipantes[1] += 1
    elif año >= 2000 and año <= 2019:
        lista2000_2019.append(datosPiloto)
        tiempos2000_2019.append(tiempo)
        cantParticipantes[2] += 1

def imprimirPodio(datos, tiempos, cantParticipantes):
    burbuja(datos, tiempos)
    if len(datos) >= 3:
        for i in range(3):
            print(f"{i + 1}) {datos[i]}")
        print(f"Total participantes de {cantParticipantes}\n")
    
    
def buscarMayorParticipantes(cantParticipantes):
    cantMayor = -9999999999
    indiceCantMayor = 0
    for i in range(len(cantParticipantes)):
        if(cantParticipantes[i] > cantMayor):
            cantMayor = cantParticipantes[i]
            indiceCantMayor = i
    return indiceCantMayor

def buscarMenorParticipantes(cantParticipantes):
    cantMenor = 9999999999
    indiceCantMenor = 0
    for i in range(len(cantParticipantes)):
        if(cantParticipantes[i] < cantMenor):
            cantMenor = cantParticipantes[i]
            indiceCantMenor = i
    return indiceCantMenor

arch = open("datos0.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

lista1960_1979 = []
tiempos1960_1979 = []
lista1980_1999 = []
tiempos1980_1999 = []
lista2000_2019 = []
tiempos2000_2019 = []

pilotosMasRapidos = []
tiempoMasRapidoActual = 9999999

categorias = ["1960 - 1979", "1980 - 1999", "2000 - 2019"]
cantParticipantes = [0, 0, 0]

while linea != "":
    partes = linea.split(",")
    nombre = partes[0]
    modelo = partes[1]
    año = int(partes[2])
    tiempo = float(partes[3])
    datosPiloto = nombre + " en su " + modelo + " del año " + str(año) + " con un tiempo de " + str(tiempo)

    if tiempo < tiempoMasRapidoActual:
        tiempoMasRapidoActual = tiempo
        pilotosMasRapidos = [nombre + " en su " + modelo + " del año " + str(año)]
    elif tiempo == tiempoMasRapidoActual:
        pilotosMasRapidos.append(nombre + " en su " + modelo + " del año " + str(año))

    añadirPiloto(datosPiloto, año, tiempo, lista1960_1979, 
                tiempos1960_1979, lista1980_1999, tiempos1980_1999, 
                lista2000_2019, tiempos2000_2019, cantParticipantes)
    
    linea = arch.readline().strip()

print("1960 - 1979 El podio de la categoría es:")
imprimirPodio(lista1960_1979, tiempos1960_1979, cantParticipantes[0])

print("1980 - 1999 El podio de la categoría es:")
imprimirPodio(lista1980_1999, tiempos1980_1999, cantParticipantes[1])

print("2000 - 2019 El podio de la categoría es:")
imprimirPodio(lista2000_2019, tiempos2000_2019, cantParticipantes[2])

print(f"Los pilotos más rápidos con un tiempo de {tiempoMasRapidoActual} son:")
for i in range(len(pilotosMasRapidos)):
    print(pilotosMasRapidos[i])
print()

indiceMayor = buscarMayorParticipantes(cantParticipantes)
print(f"La categoría con más participantes es la de {categorias[indiceMayor]} con un total de {cantParticipantes[indiceMayor]} participantes")

indiceMenor = buscarMenorParticipantes(cantParticipantes)
print(f"La categoría con menor participantes es la de {categorias[indiceMenor]} con un total de {cantParticipantes[indiceMenor]} participantes")
