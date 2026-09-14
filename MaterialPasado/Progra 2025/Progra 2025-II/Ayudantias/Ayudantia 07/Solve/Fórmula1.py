def buscarAgregar(elemento, lista1, lista2):
    if elemento not in lista1:
        lista1.append(elemento)
        lista2.append(0)
    return lista1.index(elemento)

def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def ordenamientoBurbuja(lista1, lista2):
    for a in range(len(lista2)-1):
        for b in range(a+1, len(lista2)):
            if lista2[a] > lista2[b]:
                intercambiar(lista1, a, b)
                intercambiar(lista2, a, b)

def imprimirDatos(indice, pilotos, tiemposPilotos):
    print(f"{pilotos[indice]}: {tiemposPilotos[indice]} segundos")

arch = open("pilotos.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

equipos = []
tiemposEquipos = []
cantidadesEquipos = []

pilotos = []
tiemposPilotos = []

while linea != "":
    partes = linea.split(",")
    equipo = partes[0]
    nombre = partes[1]

    indiceEquipo = buscarAgregar(equipo, equipos, tiemposEquipos)
    if len(cantidadesEquipos) < len(equipos):
        cantidadesEquipos.append(0)
        
    cantidadesEquipos[indiceEquipo] += 1
    
    indiceParticipante = buscarAgregar(nombre, pilotos, tiemposPilotos)

    tiempoTotal = 0
    
    for i in range(5):
        partes2 = partes[2 + i].split(":")
        tiempo = int(partes2[0]) * 60 + int(partes2[1])
        tiempoTotal += tiempo

    tiemposEquipos[indiceEquipo] += tiempoTotal
    tiemposPilotos[indiceParticipante] += tiempoTotal

    linea = arch.readline().strip()

print("1) Promedio de tiempo por equipo")
for i in range(len(equipos)):
    promedio = tiemposEquipos[i] / cantidadesEquipos[i]
    print(f"{equipos[i]}: promedio de {round(promedio,2)} segundos")

ordenamientoBurbuja(pilotos, tiemposPilotos)
print()
print("2) Ranking de pilotos del menor al mayor tiempo total:")
for i in range(len(pilotos)):
    imprimirDatos(i, pilotos, tiemposPilotos)
    
print()
print("3) Piloto(s) con el menor tiempo total registrado en la temporada:")
menorTiempo = tiemposPilotos[0]
pos = 0
while tiemposPilotos[pos] == menorTiempo:
    imprimirDatos(pos, pilotos, tiemposPilotos)
    pos += 1
    
print()
print("4) Ranking de pilotos por promedio entre las 5 carreras")
for i in range(len(pilotos)):
    promedioPiloto = tiemposPilotos[i] / 5
    print(f"{pilotos[i]} -> Promedio por carrera: {round(promedioPiloto,2)} segundos")



    

