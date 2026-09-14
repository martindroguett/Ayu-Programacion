import numpy as np
import random

def mostrar(matriz):
    '''
    Las matrices de numpy (np.zeros(x)) solo aceptan numeros
    Para hacer que se vea linda la impresion, creamos una variable que se llama salida
    A la salida le vamos a ir agregando cosas dependiendo de que numero este en esa posicion
    ej:
    [   [0. -2. 0.],
        [-1. 0. 0.]
        [0. -2. 3.]]
    Se traduciria y se imprimiria como
    |- * -|
    |R - -|
    |- * 3|
    '''
    for i in range(matriz.shape[0]):
        salida = '|'
        for j in range(matriz.shape[1]):
            if matriz[i, j] == 0:
                salida += '- '
            elif matriz[i, j] == -1:
                salida += 'R '
            elif matriz[i, j] == -2:
                salida += '* '
            else:
                salida += f'{int(matriz[i,j])} '
        # este ultimo strip es para quitar el espacio sobrante
        print(salida.strip() + '|')

def limpiarPantalla():
    # No se preocupen mucho de esto, es un truco para limpiar la pantalla
    print("\033[H\033[2J")

def procesarMovimiento(matriz, mov, anterior_pos):

    '''
    Para procesar los movimientos, necesitamos saber dos cosas
    1. Si el 'input' es aceptado
        O sea, que sea w | a | s | d
    2. Si el movimiento cabe en la matriz
        Se tiene que tener cuenta el tamaño de la matriz
        Supongamos es el movimiento es W (arriba) y estamos en la fila 0, no nos podemos mover hacia arriba.
    '''

    nueva_pos = anterior_pos.copy() # para copiar la lista

    # No se puede hacer esto:
    # nueva_pos = anterior_pos
    # Sin complicar mucho la explicacion, hacer esto es llamar a la misma lista pero con distinto nombre
    # nueva_pos[0] = 'x' tambien afecta a anterior_pos[0]

    mov = mov.lower()
    if mov == 'w' and anterior_pos[0] > 0:
        nueva_pos[0] -= 1
    elif mov == 's' and anterior_pos[0] < matriz.shape[0] - 1:
        nueva_pos[0] += 1
    elif mov == 'a' and anterior_pos[1] > 0:
        nueva_pos[1] -= 1
    elif mov == 'd' and anterior_pos[1] < matriz.shape[1] - 1:
        nueva_pos[1] += 1
    elif mov == 'x':
        print("Saliendo...")
        return False
    else:
        print('¡Movimiento inválido!')
        return True

    if matriz[nueva_pos[0], nueva_pos[1]] == -2: # Choco con un *
        limpiarPantalla()
        matriz[anterior_pos[0], anterior_pos[1]] = -2 # Actualizo la posicion
        matriz[nueva_pos[0], nueva_pos[1]] = -1
        mostrar(matriz)
        print("Has regado dos veces en el mismo lugar!")
        return False # Rompo el ciclo

    matriz[anterior_pos[0], anterior_pos[1]] = -2
    matriz[nueva_pos[0], nueva_pos[1]] = -1
    return True

def generarObjetivos(matriz, pos_jugador, limite):

    '''
    Una funcion asi probablemente se la den en la prueba, pero
    Simplificada, lo que hace es generar objetivos 'random' posibles dentro de la matriz
    '''

    objetivos = []
    while len(objetivos) < limite:
        pos_posible = [random.randint(0, matriz.shape[0] - 1), random.randint(0, matriz.shape[1] - 1)]

        if pos_posible != pos_jugador and pos_posible not in objetivos:
            # Si no esta en [0,0] y no hay un objetivo ya ahi
            objetivos.append(pos_posible)
            matriz[pos_posible[0], pos_posible[1]] = len(objetivos)

    return objetivos

objetivos = int(input("Número de objetivos?: "))
filas = int(input("Filas:"))
columnas = int(input("Columnas:"))

matriz = np.zeros([filas, columnas])

posicion = [0, 0] # posicion inicial
matriz[posicion[0], posicion[1]] = -1

lista_objetivos = generarObjetivos(matriz, posicion, objetivos)
objetivos_restantes = len(lista_objetivos)
siguiente_esperado = 0

jugar = True
while jugar:
    limpiarPantalla()
    mostrar(matriz)
    print(f"Objetivos restantes: {objetivos_restantes}")
    print(f"Siguiente objetivo: {siguiente_esperado + 1}")

    accion = input("Movimiento (w/a/s/d o 'x' para salir): ")
    jugar = procesarMovimiento(matriz, accion, posicion)

    if jugar and posicion in lista_objetivos: # Si encuentro un objetivo
        if posicion == lista_objetivos[siguiente_esperado]: # Y los estoy encontrando en orden
            lista_objetivos[siguiente_esperado] = 0 # lo "borro"
            objetivos_restantes -= 1
            siguiente_esperado += 1

            if objetivos_restantes == 0:
                limpiarPantalla()
                mostrar(matriz)
                print("Todo listo!")
                jugar = False
        else:
            limpiarPantalla()
            mostrar(matriz)
            print("Tienes que regar en orden!")
            jugar = False