import numpy as np

def leer_sismos():
    matriz = np.zeros((16, 13))
    for i in range(12):
        nombre = "sismos_mes_" + str(i+1) + ".txt"
        arch = open(nombre, "r", encoding = "utf-8")
        linea = arch.readline().strip()
        
        while linea != "":
            partes = linea.split(";")
            codigo = int(partes[0])
            promedio = float(partes[1])
            
            matriz[codigo-1][i] = promedio
            
            linea = arch.readline().strip()
        
    return matriz
        
        
def calcular_promedio(matriz):
    for i in range(16):
        suma = 0
        for j in range(12):
            suma += matriz[i][j]
        matriz[i][12] = suma/12
        
        
def ordenar_matriz(matriz, regiones):
    filas = len(matriz)
    for pasada in range(filas - 1):
        for i in range(filas - 1 - pasada):
            if matriz[i][12] < matriz[i+1][12]:
                matriz[[i, i + 1]] = matriz[[i + 1, i]]
                regiones[i], regiones[i + 1] = regiones[i + 1], regiones[i]
                
def imprimir_ranking(matriz, regiones):
    print("RANKING DE REGIONES \n")
    for i in range(16):
        print(f"Región: {regiones[i]} - Magnitud promedio: {round(matriz[i][12], 2)}")

arch = open("regiones.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

regiones = []

while linea != "":
    partes = linea.split(";")
    region = partes[1]
    
    regiones.append(region)
    
    linea = arch.readline().strip()
    

matriz = leer_sismos()
calcular_promedio(matriz)
ordenar_matriz(matriz, regiones)
imprimir_ranking(matriz, regiones)