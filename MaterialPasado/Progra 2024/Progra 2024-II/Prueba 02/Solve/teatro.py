import numpy as np

def buscarAgregar(elemento, lista1, lista2):
    if elemento not in lista1:
        lista1.append(elemento)
        lista2.append(0)
    return lista1.index(elemento)

def sumarCol(mx, lista1, lista2):
    sumaCol = []
    for col in range(len(lista2)):
        suma = 0
        for fil in range(len(lista1)):
            if mx[fil][col] == 1:
                suma += 1
        sumaCol.append(suma)
    return sumaCol

def intercambiar(lista,a,b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbuja(lista1,lista2):
    for a in range(len(lista1)-1):
        for b in range(a+1,len(lista1)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)

filas = ["a", "b", "c", "d", "e", "f", "g", "h"]
columnas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

mxAsientos = np.zeros([len(filas), len(columnas)])

arch = open("teatro.txt","r",encoding="utf-8")
linea = arch.readline().strip()

fila = 0

while linea != "":
    partes = linea.split(" ")
    
    for i in range(len(partes)):
        asiento = partes[i]
        
        if asiento == "1":
            mxAsientos[fila][i] = 1
        elif asiento == "S" or asiento == "P":
            mxAsientos[fila][i] = 2

    fila += 1
    linea = arch.readline().strip()

arch = open("reservas.txt","r",encoding="utf-8")
linea = arch.readline().strip()

totalRecaudado = 0

cantOcupados = 0

nombres = []
cantCompradas = []

noRealizadas = [0] * len(filas)

while linea != "":
    partes = linea.split(";")
    nombre = partes[0]
    fil = int(partes[1])
    col = int(partes[2])

    indiceNombre = buscarAgregar(nombre, nombres, cantCompradas)

    if mxAsientos[fil][col] == 0:
        mxAsientos[fil][col] = 1
        totalRecaudado += 5000
        cantOcupados += 1
        cantCompradas[indiceNombre] += 1
    elif mxAsientos[fil][col] == 1:
        noRealizadas[fil] += 1
    
    linea = arch.readline().strip()

#Pregunta 1
print(f"Recaudación total: {totalRecaudado}")

#Pregunta 2
asientosTotales = len(filas) * len(columnas)
porcentajeOcupacion = 100 * (cantOcupados / asientosTotales)
print(f"Porcentaje de ocupación: {round(porcentajeOcupacion, 2)}%")

#Pregunta 3
mayorDisponible = -1
filaMayorDisponible = 0

for fil in range(len(filas)):
    suma = 0
    for col in range(len(columnas)):
        if mxAsientos[fil][col] == 0:
            suma += 1
    if suma > mayorDisponible:
        mayorDisponible = suma
        filaMayorDisponible = fil

print(f"Fila con mayor cantidad de asientos libres: {filaMayorDisponible}")

#Pregunta 4
mayorCompradas = -1
indiceMayorCompradas = 0
for i in range(len(cantCompradas)):
    cantComprada = cantCompradas[i]
    if cantComprada > mayorCompradas:
        mayorCompradas = cantComprada
        indiceMayorCompradas = i
        
print(f"El cliente con más entradas compradas es: {nombres[indiceMayorCompradas]}")

#Pregunta 5
colSumadas = sumarCol(mxAsientos, filas, columnas)
burbuja(colSumadas, columnas)
print("Tres columnas con mayor cantidad de asientos ocupados:")
for i in range(3):
    print(f"- Columna {columnas[i]}: {colSumadas[i]}")

#Pregunta 6
mayorNoRealizada = -1
filMayorNoRealizada = 0
for i in range(len(noRealizadas)):
    cant = noRealizadas[i]
    if cant > mayorNoRealizada:
        mayorNoRealizada = cant
        filMayorNoRealizada = i
print(f"La fila más popular es: {filas[filMayorNoRealizada].upper()}")

