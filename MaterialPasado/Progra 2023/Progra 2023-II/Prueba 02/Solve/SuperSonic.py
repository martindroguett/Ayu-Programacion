
def buscarAgregar(elemento, lista, lista2):
    if elemento not in lista:
        lista.append(elemento)
        lista2.append(0)
    return lista.index(elemento)

def intercambiar(lista,a,b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbuja(lista1,lista2):
    for a in range(len(lista2)-1):
        for b in range(a+1,len(lista2)):
            if lista2[a] < lista2[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)

arch = open("super_sonic_legend_cup.txt","r",encoding="utf-8")
linea = arch.readline().strip()

selecciones = []
puntajes = []

cantEnfrentamientos = 0

lugares = []
puntajesEntregados = []

while linea != "":
    partes = linea.split(",")
    seleccion1 = partes[0]
    seleccion2 = partes[1]
    goles1 = int(partes[2])
    goles2 = int(partes[3])
    lugar = partes[4]
    
    indice1 = buscarAgregar(seleccion1, selecciones, puntajes)
    indice2 = buscarAgregar(seleccion2, selecciones, puntajes)
    indiceLugar = buscarAgregar(lugar, lugares, puntajesEntregados)
    
    if goles1 > goles2:
        puntajes[indice1] += 3
        puntajesEntregados[indiceLugar] += 3
    elif goles2 > goles1:
        puntajes[indice2] += 3
        puntajesEntregados[indiceLugar] += 3
    else:
        puntajes[indice1] += 1
        puntajes[indice2] += 1
        puntajesEntregados[indiceLugar] += 2
    
    cantEnfrentamientos += 1
    
    linea = arch.readline().strip()
    
print(f"#1 El total de enfrentamientos fue de {cantEnfrentamientos}")
print()

burbuja(selecciones, puntajes)
mayorPuntajeSeleccion = puntajes[0]
print(f"#2 El puntaje máximo fue de {mayorPuntajeSeleccion} puntos alcanzado por:")
i = 0
while puntajes[i] == mayorPuntajeSeleccion:
    print()
    print(f"- {selecciones[i]}")
    i += 1

print()
print("#3 El o los lugares que entregaron mayor puntaje:")
burbuja(lugares, puntajesEntregados)
mayorPuntajeLugar = puntajesEntregados[0]
i = 0
while puntajesEntregados[i] == mayorPuntajeLugar:
    print()
    print(f"- {lugares[i]}")
    i += 1
print()
print(f"Los puntos entregados fueron {mayorPuntajeLugar}")
print()

print("#4 Las 4 selecciones con mayor puntaje son:")
burbuja(selecciones, puntajes)
for i in range(4):
    print()
    print(f"- {selecciones[i]} con {puntajes[i]}")

