import numpy as np
mx = np.zeros([50,50])

def buscarAgregar(elemento,lista):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

def asignarCodigos(nombres, tamaños, codigo, tamaño, mx):
    for fil in range(len(nombres)):
        for col in range(len(tamaños)):
            if tamaños[col] == tamaño and mx[fil][col] > 0:
                print(f"Asociado: {nombres[fil]} Codigo: {codigo}" )
                mx[fil][col] -= 1
                return

arch = open("solicitudes.txt","r",encoding= "utf-8")
linea = arch.readline().strip()
linea = arch.readline().strip()
tamaños = [5, 11, 15, 45]
nombres = []

while linea != "":
    partes = linea.split(";")
    nombre = partes[0]
    indiceNombre = buscarAgregar(nombre, nombres)
    for i in range(1, len(partes)):
        cantActual = int(partes[i])
        if(cantActual != 0):
            mx[indiceNombre][i - 1] = cantActual

    linea = arch.readline().strip()

print("Detalles totales requeridos:\n")

for col in range(len(tamaños)):
    suma = 0
    for fila in range(len(nombres)):
        suma += mx[fila][col]
    print(f"Cilindro : {tamaños[col]}KG Total Requerido: {suma}")
print("")

print("Detalle asignaciones de códigos:\n")

arch2 = open("codigos.txt","r",encoding= "utf-8")
linea2 = arch2.readline().strip()

while linea2 != "":
    partes = linea2.split(";")
    codigo = partes[0]
    tamaño = int(partes[1])

    asignarCodigos(nombres, tamaños, codigo, tamaño, mx)
    linea2 = arch2.readline().strip()
