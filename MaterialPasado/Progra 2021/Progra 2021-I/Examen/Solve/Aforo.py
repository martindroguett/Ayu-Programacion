import numpy as np

def buscarAgregar(elemento, lista):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

mxAforo = np.zeros([6,8])
mxCant = np.zeros([6,8])

arch = open("metrajes.txt")
linea = arch.readline().strip()

tiendas = []
cuidades = []

mayor = -1
tiendaMayor = ""
cuidadMayor = ""

menor = 999999
tiendaMenor = ""
cuidadMenor = ""

while linea != "":
    partes = linea.split("-")
    cuidad = partes[0]
    tienda = partes[1]
    metros = int(partes[2])
    
    indiceTienda = buscarAgregar(tienda, tiendas)
    indiceCuidad = buscarAgregar(cuidad, cuidades)
    
    cantMaxima = metros / 8
    
    mxAforo[indiceTienda][indiceCuidad] = cantMaxima
    
    if cantMaxima > mayor:
        mayor = cantMaxima
        tiendaMayor = tienda
        cuidadMayor = cuidad
    
    if cantMaxima < menor:
        menor = cantMaxima
        tiendaMenor = tienda
        cuidadMenor = cuidad
        
    linea = arch.readline().strip()
    
arch = open("fiscalizaciones.txt")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split("-")
    cuidad = partes[0]
    tienda = partes[1]
    cantPersonas = int(partes[2])
    
    indiceTienda = buscarAgregar(tienda, tiendas)
    indiceCuidad = buscarAgregar(cuidad, cuidades)
    
    mxCant[indiceTienda][indiceCuidad] += cantPersonas
    linea = arch.readline().strip()

#Pregunta 1
print("a).")
for fil in range(len(tiendas)):
    for col in range(len(cuidades)):
        cantMaxima = mxAforo[fil][col]
        cantPresentes = mxCant[fil][col]
        if cantPresentes > cantMaxima:
            print(f"{tiendas[fil]} - {cuidades[col]}")
            
#Pregunta 2
print("b).")
for col in range(len(cuidades)):
    suma = 0
    for fil in range(len(tiendas)):
        cantMaxima = mxAforo[fil][col]
        cantPresentes = mxCant[fil][col]
        if cantPresentes > cantMaxima:
            cantExtras = abs(cantMaxima - cantPresentes)
            suma += 150000 * cantExtras
    print(f"{cuidades[col]} :$ {suma}")

#Pregunta 3
print("c).")
print(f"El aforo maximo en una tienda es de: {mayor} personas")
print(f"{tiendaMayor} ubicada en la cuidad {cuidadMayor}")
print(f"El aforo minimo en una tienda es de: {menor} personas")
print(f"{tiendaMenor} ubicada en la cuidad {cuidadMenor}")
