import numpy as np

def buscarAgregar(elemento, lista):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

def encontrarMenorPrecio(indiceIngrediente, mxPrecios, supers):
    menor = 9999999999999
    indiceMenor = -1
    for fil in range(len(supers)):
        if mxPrecios[fil][indiceIngrediente] < menor:
            menor = mxPrecios[fil][indiceIngrediente]
            indiceMenor = fil
    return indiceMenor

mxCant = np.zeros([50,50])
mxPrecios = np.zeros([50,50])

arch = open("precios.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

supers = ["Dumbo","Saint Elizabeth","Duomarc"]
ingredientes = []

while linea != "":
    partes = linea.split("-")
    ingrediente = partes[0]
    
    indiceIngrediente = buscarAgregar(ingrediente, ingredientes)
    
    for i in range(3):
        precioActual = int(partes[i + 1])
        mxPrecios[i][indiceIngrediente] = precioActual
    
    linea = arch.readline().strip()

arch = open("recetas.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

recetas = []
valores = []

while linea != "":
    partes = linea.split("-")
    receta = partes[0]
    cant = int(partes[1])
    
    indiceReceta = buscarAgregar(receta, recetas)
    valores.append(0)
    
    for i in range(2, len(partes)):
        ingrediente = partes[i]
        indiceIngrediente = ingredientes.index(ingrediente)
        indiceSuper = encontrarMenorPrecio(indiceIngrediente, mxPrecios, supers)
        mxCant[indiceSuper][indiceIngrediente] += cant
        
        valores[indiceReceta] += mxPrecios[indiceSuper][indiceIngrediente]
    
    linea = arch.readline().strip()

#Pregunta 1
print("1) Productos por supermercado")
for fil in range(len(supers)):
    print(f"{supers[fil]}:")
    for col in range(len(ingredientes)):
        if mxCant[fil][col] != 0:
            print(f"- {ingredientes[col]} {int(mxCant[fil][col])}")

#Pregunta 2
print("2) Total por supermercado")
for fil in range(len(supers)):
    suma = 0
    for col in range(len(ingredientes)):
        suma += mxPrecios[fil][col] * mxCant[fil][col] 
    print(f"- {supers[fil]}: ${int(suma)}")

#Prregunta 3
print("3) Valor por receta")
for i in range(len(recetas)):
    print(f"- {recetas[i]}: ${valores[i]}")
