import random

hoferX = 0
hoferY = 0
noviaX = random.randint(1, 10)
noviaY= random.randint(1, 10)

encontrado = False

codigo = input("Ingresa el codigo de movimientos: ")

while codigo != "" and not encontrado:

    for accion in codigo:#Itera en el cdi

        if accion == "X":
            distancia = ((hoferX - noviaX) ** 2 + (hoferY - noviaY) ** 2)**(1/2) #Distancia euclidiana.
            print("La distancia es:", distancia)

        else:
            if accion == "S":
                if(hoferY + 1 <= 10):
                    hoferY += 1
                else:
                    print("Hofer no puede salir de los limites!")
                    
            elif accion == "B":
                if(hoferY - 1 >= 0):
                    hoferY -= 1
                else:
                    print("Hofer no puede salir de los limites!")
                    
            elif accion == "D":
                if(hoferX + 1 <= 10):
                    hoferX += 1
                else:
                    print("¡Hofer no puede salir de los limites!")
                    
            elif accion == "I":
                if(hoferX - 1 >= 0):
                    hoferX -= 1
                else:
                    print("¡Hofer no puede salir de los limites!")

            if hoferX == noviaX and hoferY == noviaY:
                print(f"¡Hofer encontró a su novia! en la posicion ({noviaX},{noviaY})")
                encontrado = True
                break

    if noviaX > hoferX:
        print("La novia grita: ¡Ve a la derecha!")
    elif noviaX < hoferX:
        print("La novia grita: ¡Ve a la izquierda!")

    if noviaY > hoferY :
        print("La novia grita: ¡Sube!")
    elif noviaY < hoferY:
        print("La novia grita: ¡Baja!")

    if not encontrado:
        codigo = input("Ingresa el codigo de movimientos: ")
    

if not encontrado:
    distancia = ((hoferX - noviaX) ** 2 + (hoferY - noviaY) ** 2)**(1/2) #La printea en la salida.
    print(f"No se encontraron, murio el amor. Distancia final: {distancia}")