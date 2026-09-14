import numpy as np

def buscarAgregar(elemento, lista1, lista2):
    if elemento not in lista1:
        lista1.append(elemento)
        lista2.append(0)
    return lista1.index(elemento)

def crearMatriz(arch):
    linea = arch.readline().strip()

    cantFil = int(linea.split(",")[0])
    cantCol = int(linea.split(",")[1])

    mxFabrica = np.zeros([cantFil, cantCol])
    linea = arch.readline().strip()

    fila = 0

    while linea != "":
        partes = linea.split(",")

        for i in range(len(partes)):
            mxFabrica[fila][i] = int(partes[i])
        fila += 1

        linea = arch.readline().strip()
    return mxFabrica

def calcularLotes(fil, col, cantLotes, productos, cantUnidades, años, mxAños):
    for i in range(1, cantLotes + 1):
        total = 0

        arch = open(f"{str(fil)}-{str(col)}-{str(i)}.txt","r",encoding="utf-8")
        linea = arch.readline().strip()
        fecha = linea
        año = int(fecha.split("/")[2])
        indiceAño = años.index(año)
    
        linea = arch.readline().strip()

        while linea != "":
            partes = linea.split(",")
            producto = partes[0]
            cant = int(partes[1])
            coste = float(partes[2])

            total += coste

            indiceProducto = buscarAgregar(producto, productos, cantUnidades)
            cantUnidades[indiceProducto] += cant

            mxAños[indiceAño][indiceProducto] += cant

            linea = arch.readline().strip()
        
        print(f"Lote: {fil}-{col}-{i}: {round(total,2)}")

        arch.close()

def calcularValorInventario(arch, productos, cantUnidades):
    linea = arch.readline().strip()

    valorInventario = 0

    while linea != "":
        partes = linea.split(",")
        producto = partes[0]
        precioUnitario = float(partes[1])

        indiceProducto = productos.index(producto)
        valor = precioUnitario * cantUnidades[indiceProducto]
        valorInventario += valor

        linea = arch.readline().strip()

    return round(valorInventario,2)

mxFabrica = crearMatriz(open("indice.txt","r", encoding = "utf-8"))

años = [2020, 2021, 2022, 2023, 2024, 2025]
mxAños = np.zeros([len(años), 100])
productos = []
cantUnidades = []

print("1. Coste de producción de cada lote")
for fil in range(len(mxFabrica)):
    for col in range(len(mxFabrica[0])):
        cantLotes = int(mxFabrica[fil][col])
        calcularLotes(fil, col, cantLotes, productos, cantUnidades, años, mxAños)

print("----------------------------------------------------\n")
print("----------------------------------------------------")

print("2. Listado de productos con sus unidades producidas")
for i in range(len(productos)):
    print(f"{productos[i]}: {cantUnidades[i]} unidades")

print("----------------------------------------------------\n")
print("----------------------------------------------------")

print(f"3. Valor de todos los productos fabricados: {calcularValorInventario(open("precios.txt","r",encoding = "utf-8"), productos, cantUnidades)}")

print("----------------------------------------------------\n")
print("----------------------------------------------------")

print("4. Detalle de producción anual")
for fil in range(len(mxAños)):
    print(f"\n{años[fil]}\n")
    for col in range(len(mxAños[0])):
        cant = mxAños[fil][col]
        if cant > 0:
            print(f"{productos[col]}: {cant}")