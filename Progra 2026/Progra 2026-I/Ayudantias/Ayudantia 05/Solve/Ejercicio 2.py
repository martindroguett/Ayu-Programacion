def leer_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    archivo = open(nombre_archivo, "r", encoding = "utf-8")
    return archivo

def calcular_promedio(suma, cantidad):
    # promedio = suma / cantidad
    # return promedio
    return (suma/cantidad)

def imprimir_promedio(categoria, promedio):
    print(f"Promedio de tiempo de dificultad {categoria}: {round(promedio)} segundos.")

arch = leer_archivo()
linea = arch.readline().strip()

menorTiempo = 99999
jugadorMenorTiempo = ""

sumaTiempoFacil = 0
contFacil = 0

sumaTiempoInter = 0
contInter = 0

sumaTiempoDificil = 0
contDificil = 0

pistasLaboratorio = 0

print()
print("1) Jugadores que no lograron salir del Escape Room: ")
while linea != "":
    partes = linea.split(",")
    pieza = partes[0]
    dificultad = partes[1]
    jugador = partes[2]
    edad = int(partes[3])
    pistas = int(partes[4])
    puzzles = int(partes[5])
    tiempo_salida = int(partes[6])
    
    if tiempo_salida == -1:
        print(f"- {jugador} ({edad})")
    
    elif tiempo_salida < menorTiempo:
        menorTiempo = tiempo_salida
        jugadorMenorTiempo = jugador
        
    if tiempo_salida != -1:
        
        if dificultad == "facil":
            contFacil += 1
            sumaTiempoFacil += tiempo_salida
        elif dificultad == "intermedio":
            contInter += 1
            sumaTiempoInter += tiempo_salida
        elif dificultad == "dificil":
            contDificil += 1
            sumaTiempoDificil += tiempo_salida
    
    """
    VERSION MEJORADA
    if tiempo_salida != -1:
        
        if tiempo_salida < menorTiempo:
            menorTiempo = tiempo_salida
            jugadorMenorTiempo = jugador
        
        
        if dificultad == "facil":
            contFacil += 1
            sumaTiempoFacil += tiempo_salida
        elif dificultad == "intermedio":
            contIntermedio += 1
            sumaTiempoIntermedio += tiempo_salida
        elif dificultad == "dificil":
            contDificil += 1
            sumaTiempoDificil += tiempo_salida
        
    else:
        print(f"- {jugador} ({edad})")
    """
            
    if pieza == "Laboratorio X":
        pistasLaboratorio += pistas
        
    
    linea = arch.readline().strip()

print()
print(f"2) {jugadorMenorTiempo} fue el/la jugador/a más rápido/a, demorando {menorTiempo} segundos.")

promedioFacil = calcular_promedio(sumaTiempoFacil, contFacil)
promedioInter = calcular_promedio(sumaTiempoInter, contInter)
promedioDificil = calcular_promedio(sumaTiempoDificil, contDificil)

print()
print("3) Promedios:")
imprimir_promedio("Facil", promedioFacil)
imprimir_promedio("Intermedio", promedioInter)
imprimir_promedio("Dificil", promedioDificil)

print()
print(f"4) Pistas utilizadas en Laboratorio X: {pistasLaboratorio}")