
def buscar_agregar(elemento, lista1, lista2):
    if elemento not in lista1:
        lista1.append(elemento)
        lista2.append(0)
    return lista1.index(elemento)

def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux


def burbuja(lista1, lista2):
    for a in range(len(lista1)-1):
        for b in range(a+1, len(lista1)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1, a, b)
                intercambiar(lista2, a, b)

def imprimir_selecciones_etapa(selecciones, partidos_selecciones, cant_partidos):
    for i in range(len(selecciones)):
        if partidos_selecciones[i] == cant_partidos:
            print(f"- {selecciones[i]}")
    print("---------------------------")

jugadores = []
goles_jugadores = []

selecciones = []
goles_selecciones = []

partidos_selecciones = []

'''
Lo que hace esto es:
1. leer linea y dividir en partes
2. si no hemos leido la seleccion, su numPartidos se agrega a la lista partidos_selecciones
3. buscamos y agregamos usando buscar_agregar el jugador y la seleccion (sin repetidos)
4. conseguimos los indices de tanto el jugador en Jugadores y seleccion en selecciones
5. revisamos los goles y los insertamos en la lista de goles_jugadores y goles_selecciones, utilizando el indice anterior
'''


arch = open("datos.txt", 'r', encoding="utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    seleccion = partes[0]
    jugador = partes[1]

    if seleccion not in selecciones:
        partidos_selecciones.append(len(partes)-2)

    indice_jugador = buscar_agregar(jugador, jugadores, goles_jugadores)

    indice_seleccion = buscar_agregar(seleccion, selecciones, goles_selecciones)

    for i in range(2,len(partes)):
        goles = int(partes[i])

        goles_selecciones[indice_seleccion] += goles

        goles_jugadores[indice_jugador] += goles

    linea = arch.readline().strip()


# Este primer burbuja sirve para ordenar los jugadores en base a sus goles, de mayor a menor
# Importante que se va a ordenar tomando en cuenta solo goles_jugadores

burbuja(goles_jugadores, jugadores)

print("ANALISIS DEL MUNDIAL 2030")
print()

# Podemos hacer un for 5 para mostralos, ya que los ordenamos

print("1) TOP 5 GOLEADORES")
for i in range(5):
    print(f"{i+1}. {jugadores[i]} con {goles_jugadores[i]} goles")
print()

print("2) Promedio de goles por seleccion")
for i in range(len(selecciones)):
    promedio = round(goles_selecciones[i] / partidos_selecciones[i],2)
    print(f"- {selecciones[i]} -> {promedio} goles por partido")
print()

print("3) CLASIFICACIÓN DE SELECCIONES POR MAXIMA ETAPA ALCANZADA")

# Aqui recien ordenamos los partidos con las selecciones, si no tendriamos que ordenar
# partidos, selecciones Y goles para que no se desordenaran

# Se repite lo mismo de la linea 70, se ordena en base a el numero de partidos
burbuja(partidos_selecciones, selecciones)

# Las listas tambien son utiles para mantener un orden especifico de impresion

etapas = ["Fase De Grupos", "Dieciseisavos de final", "Octavos de final", "Cuartos de final", "Semifinal", "Final"]
cant_partidos = [3, 4, 5, 6, 7, 8]

for i in range(len(etapas)):
    print(f"{etapas[i].upper()} ({cant_partidos[i]} partidos jugados)")
    imprimir_selecciones_etapa(selecciones, partidos_selecciones, cant_partidos[i])
