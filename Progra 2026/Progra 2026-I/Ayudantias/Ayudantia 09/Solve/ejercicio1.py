import numpy as np

def cargar_matriz(nombre_archivo):
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    linea = archivo.readline().strip()

    matriz = np.zeros([5, 5])
    fila = 0
    while linea != "":
        valores = linea.split(" ")
        for j in range(len(valores)):
            matriz[fila][j] = int(valores[j])
        fila += 1
        linea = archivo.readline().strip()

    archivo.close()
    return matriz


def imprimir_matriz(matriz):
    print("--------------------------")
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            print(f"{int(matriz[i][j])} ", end="")
        print()
    print("--------------------------")


def marcar_numero(matriz, numero):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i][j] == numero:
                matriz[i][j] = 0


def verificar_ganador(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i][j] != 0:
                return False
    return True


carton = cargar_matriz("carton.txt")

print("Bingo a beneficio del APC UCN")
imprimir_matriz(carton)

ganador = False
numero = int(input("Ingrese el numero (-1 para terminar): "))

while numero != -1 and not ganador:
    if numero < 1 or numero > 90:
        print("Numero invalido, debe ser entre 1 y 90")
    else:
        marcar_numero(carton, numero)

        imprimir_matriz(carton)

        if verificar_ganador(carton):
            ganador = True
            print("El carton gana!")

    if not ganador:
        numero = int(input("Ingrese el numero cantado (-1 para terminar): "))

if not ganador:
    print("Juego terminado sin ganador")