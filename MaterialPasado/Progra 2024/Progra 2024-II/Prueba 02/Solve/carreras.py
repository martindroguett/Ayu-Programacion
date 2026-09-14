#ROGER VILLARROEL
import random

def intercambiar(lista,a,b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbuja(lista1,lista2):
    for a in range(len(lista1)-1):
        for b in range(a+1,len(lista1)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)

def fichaAleatoria():
    return random.choice(["A","B","C","D","a","b","c","d"])

def quienVaGanando(lista1,lista2,lista3,lista4):
    if len(lista1) > len(lista2) and len(lista1) > len(lista3) and len(lista1) > len(lista4):
        print("Va ganando A")
    if len(lista2) > len(lista1) and len(lista2) > len(lista3) and len(lista2) > len(lista4):
        print("Va ganando B")
    if len(lista3) > len(lista1) and len(lista3) > len(lista2) and len(lista3) > len(lista4):
        print("Va ganando C")
    if len(lista4) > len(lista1) and len(lista4) > len(lista2) and len(lista4) > len(lista3):
        print("Va ganando D")

def printFichas(ficha1,ficha2,ficha3,ficha4):
    print("A:",ficha1)
    print("B:",ficha2)
    print("C:",ficha3)
    print("D:",ficha4)

def printVictorias(ganador1,ganador2,ganador3,ganador4):
    resultados = []
    movimientos = ["A","B","C","D"]
    resultados.append(ganador1)
    resultados.append(ganador2)
    resultados.append(ganador3)
    resultados.append(ganador4)

    burbuja(resultados,movimientos)
    for i in range(len(resultados)):
        print(movimientos[i],":", resultados[i])

# INICIO DEL PROGRAMA
long = int(input("Ingrese longitud del tablero: "))

fichas_A = 0
fichas_B = 0
fichas_C = 0
fichas_D = 0

victorias_A = 0
victorias_B = 0
victorias_C = 0
victorias_D = 0

cant_simulaciones = int(input("Cantidad de simulaciones: "))

for i in range(cant_simulaciones):
    A = ["A"]
    B = ["B"]
    C = ["C"]
    D = ["D"]

    while True:
        ficha = fichaAleatoria()
        print(f"FICHA: {ficha}")

        if ficha == "A" or ficha == "a":
            fichas_A += 1
            indice_actual = A.index("A")
            if ficha == "A":
                A.append("A")
                A[indice_actual] = ""
            else:
                if len(A) > 1:
                    A.pop()
                    if len(A) > 0:
                        A[indice_actual - 1] = "A"

        elif ficha == "B" or ficha == "b":
            fichas_B += 1
            indice_actual = B.index("B")
            if ficha == "B":
                B.append("B")
                B[indice_actual] = ""
            else:
                if len(B) > 1:
                    B.pop()
                    if len(B) > 0:
                        B[indice_actual - 1] = "B"

        elif ficha == "C" or ficha == "c":
            fichas_C += 1
            indice_actual = C.index("C")
            if ficha == "C":
                C.append("C")
                C[indice_actual] = ""
            else:
                if len(C) > 1:
                    C.pop()
                    if len(C) > 0:
                        C[indice_actual - 1] = "C"

        elif ficha == "D" or ficha == "d":
            fichas_D += 1
            indice_actual = D.index("D")
            if ficha == "D":
                D.append("D")
                D[indice_actual] = ""
            else:
                if len(D) > 1:
                    D.pop()
                    if len(D) > 0:
                        D[indice_actual - 1] = "D"

        print(A)
        print(B)
        print(C)
        print(D)

        if len(A) > long - 1:
            print("GANA A")
            victorias_A += 1
            printFichas(fichas_A, fichas_B, fichas_C, fichas_D)
            printVictorias(victorias_A,victorias_B,victorias_C,victorias_D)
            break

        elif len(B) > long - 1:
            print("GANA B")
            victorias_B += 1
            printFichas(fichas_A, fichas_B, fichas_C, fichas_D)
            printVictorias(victorias_A,victorias_B,victorias_C,victorias_D)
            break

        elif len(C) > long - 1:
            print("GANA C")
            victorias_C += 1
            printFichas(fichas_A, fichas_B, fichas_C, fichas_D)
            printVictorias(victorias_A,victorias_B,victorias_C,victorias_D)
            break

        elif len(D) > long - 1:
            print("GANA D")
            victorias_D += 1
            printFichas(fichas_A, fichas_B, fichas_C, fichas_D)
            printVictorias(victorias_A,victorias_B,victorias_C,victorias_D)
            break

        quienVaGanando(A,B,C,D)
