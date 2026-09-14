import numpy as np

def cargar_nombres(nombre_archivo):
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    linea = archivo.readline().strip()

    nombres = []

    while linea != '':
        partes = linea.split(";")
        nombres.append(partes[0])
        linea = archivo.readline().strip()

    archivo.close()
    return nombres


def cargar_matriz(nombre_archivo):
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    linea = archivo.readline().strip()

    matriz = np.zeros([8, 7])
    fila = 0
    while linea != '':
        partes = linea.split(";")
        for j in range(1, len(partes)):
            matriz[fila][j-1] = int(partes[j])
        fila += 1
        linea = archivo.readline().strip()

    archivo.close()
    return matriz


def total_por_equipo(nombres, matriz):
    print("--------------------------")
    print("Total de ejercicios resueltos por equipo")
    for i in range(matriz.shape[0]):
        total = 0
        for j in range(matriz.shape[1]):
            total += int(matriz[i][j])
        print(f"{nombres[i]}: {total}")


def ejercicio_mas_resuelto(matriz):
    letras = ["A", "B", "C", "D", "E", "F", "G"]
    indice_mayor = 0
    suma_mayor = 0
    for j in range(matriz.shape[1]):
        suma = 0
        for i in range(matriz.shape[0]):
            suma += matriz[i][j]
        if suma > suma_mayor:
            suma_mayor = suma
            indice_mayor = j
    return letras[indice_mayor]


def ejercicio_menos_resuelto(matriz):
    letras = ["A", "B", "C", "D", "E", "F", "G"]
    indice_menor = 0
    suma_menor = matriz.shape[0]
    for j in range(matriz.shape[1]):
        suma = 0
        for i in range(matriz.shape[0]):
            suma += matriz[i][j]
        if suma < suma_menor:
            suma_menor = suma
            indice_menor = j
    return letras[indice_menor]


def equipos_destacados(nombres, matriz):
    print("--------------------------")
    print("Equipos que resolvieron mas de 3 ejercicios")
    for i in range(matriz.shape[0]):
        total = 0
        for j in range(matriz.shape[1]):
            total += int(matriz[i][j])
        if total > 3:
            print(f"{nombres[i]} ({total} ejercicios)")


nombres = cargar_nombres("resultados_apc.txt")
matriz = cargar_matriz("resultados_apc.txt")

total_por_equipo(nombres, matriz)

print("--------------------------")
mas = ejercicio_mas_resuelto(matriz)
menos = ejercicio_menos_resuelto(matriz)
print(f"Ejercicio mas resuelto: {mas}")
print(f"Ejercicio menos resuelto: {menos}")

equipos_destacados(nombres, matriz)