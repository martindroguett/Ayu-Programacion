import numpy as np

def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbuja(zonas, itemsPendientes):
    for a in range(len(itemsPendientes)-1):
        for b in range(a+1, len(itemsPendientes)):
            if itemsPendientes[a] < itemsPendientes[b]:
                intercambiar(itemsPendientes, a, b)
                intercambiar(zonas, a, b)

arch = open("recibidos.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

mxCantItems = np.zeros([6,6])
mxCantDespachos = np.zeros([6,6])

zonas = ["A","B","C","D","E","F"]
sectores = [1, 2, 3, 4, 5, 6]

while linea != "":
    partes = linea.split(";")
    fecha = partes[0]
    
    partesPosicion = partes[1].split("-")
    indiceZona = zonas.index(partesPosicion[0])
    indiceSector = sectores.index(int(partesPosicion[1]))
    
    cantItems = int(partes[2])
    
    mxCantItems[indiceZona][indiceSector] += cantItems
    
    # Pregunta 1
    if mxCantItems[indiceZona][indiceSector] >= 100:
        mxCantItems[indiceZona][indiceSector] -= 100
        mxCantDespachos[indiceZona][indiceSector] += 1
        print(f"Se realiza un despacho en {zonas[indiceZona]} {sectores[indiceSector]} el {fecha}")
        
    linea = arch.readline().strip()

#Pregunta 2
print("2) Los envios por zona-sector en el mes fueron:")
print(mxCantDespachos)

#Pregunta 3
costos = [125, 325, 198, 635, 312, 185]
sumaTotal = 0
cantDespachos = 0
for fil in range(len(zonas)):
    for col in range(len(sectores)):
        sumaTotal += mxCantDespachos[fil][col] * costos[col]
        cantDespachos += mxCantDespachos[fil][col]
print(f"3) El costo total de los {cantDespachos} despachos es {sumaTotal}")

#Pregunta 4
print("4) Las ubicaciones con la mayor cantidad de items pendientes")
mayores = []
mayor = -1
for fil in range(len(zonas)):
    for col in range(len(sectores)):
        cantActual = mxCantItems[fil][col]
        if cantActual > mayor:
            mayor = cantActual
            mayores = [zonas[fil] + " - " + str(sectores[col]) + " con " + str(int(cantActual))]
        elif cantActual == mayor:
            mayores.append(zonas[fil] + " - " + str(sectores[col]) + " con " + str(int(cantActual)))
for i in range(len(mayores)):
    print(mayores[i])

#Pregunta 5
print("5) El total de items pendientes por zonas:")
itemsPendientes = []
for fil in range(len(zonas)):
    suma = 0
    for col in range(len(sectores)):
        suma += mxCantItems[fil][col]
    itemsPendientes.append(suma)
burbuja(zonas, itemsPendientes)
for i in range(len(zonas)):
    print(f"Zona {zonas[i]} - {itemsPendientes[i]}")
