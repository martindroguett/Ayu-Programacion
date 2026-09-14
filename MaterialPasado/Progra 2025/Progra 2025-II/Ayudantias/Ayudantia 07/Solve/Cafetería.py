def buscarAgregar(elemento, lista):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def ordenamientoBurbuja(lista1, lista2):
    for a in range(len(lista2)-1):
        for b in range(a+1, len(lista2)):
            if lista2[a] < lista2[b]:
                intercambiar(lista1, a, b)
                intercambiar(lista2, a, b)
                
productos = []
cantDisponibles = []
cantVendida = []

movimientos = []

arch = open("movimientos_cafeteria.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    accion = partes[0].lower()
    
    if accion == "todo":
        linea = arch.readline().strip()
        indiceProducto = buscarAgregar(linea, productos)
        cantVendida[indiceProducto] += cantDisponibles[indiceProducto]
        cantDisponibles[indiceProducto] = 0
        linea = arch.readline().strip()
        continue
    
    producto = partes[1]
    cantidad = int(partes[2])
    
    indiceProducto = buscarAgregar(producto, productos)
    if len(cantDisponibles) < len(productos):
        cantDisponibles.append(0)
        cantVendida.append(0)
    
    if accion == "agregar":
        cantDisponibles[indiceProducto] += cantidad
        movimiento = f"Se agregaron {cantidad} unidades de {producto} al inventario"
    else:
        if cantDisponibles[indiceProducto] - cantidad < 0:
            movimiento = f"No se pudo vender {cantidad} unidades de {producto} por la falta de stock"
        else:
            cantDisponibles[indiceProducto] -= cantidad
            cantVendida[indiceProducto] += cantidad
            movimiento = f"Se vendieron {cantidad} unidades de {producto}"
    
    movimientos.append(movimiento)
    linea = arch.readline().strip()

print()
print("Inventario final al cierre del dia:")
for i in range(len(productos)):
    print(f"{productos[i]}: {cantDisponibles[i]}")
    
ordenamientoBurbuja(productos,cantVendida)
print()
print("Cantidad vendida de cada producto ordenado de mayor a menor")
for i in range(len(productos)):
    print(f"{productos[i]}: {cantVendida[i]}")

print()
print("Resumen de los movimientos realizados durante el dia")
for i in range(len(movimientos)):
    print(movimientos[i])    