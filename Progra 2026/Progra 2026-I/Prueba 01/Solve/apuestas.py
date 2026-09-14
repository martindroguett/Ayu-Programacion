def menu():
    print("------ MENÚ DE APUESTAS ------")
    print("1. Fútbol")
    print("2. Boxeo clandestino")
    print("3. Ruleta")
    
    opcion = int(input("Seleccione una opción: "))

    while opcion != 1 and opcion != 2 and opcion != 3:
        opcion = int(input("Seleccione una opción: "))

    return opcion

def solicitar_y_validar_monto():
    monto = float(input("Ingrese monto apostado: "))

    while monto < 0:
        monto = float(input("Ingrese monto apostado: "))

    return monto


def validar_sn():
    respuesta = input("¿Acertó? (S/N): ").lower()

    while respuesta != "s" and respuesta != "n":
        respuesta = input("¿Acertó? (S/N): ").lower()

    return respuesta

def apuesta_futbol(monto):
    acerto = validar_sn()

    premio = 0

    if acerto == "s":
        if monto <= 10000:
            premio = monto * 2
        else:
            premio = monto * 2.5
        premio *= 0.9

    return premio

def apuesta_boxeo(monto):
    elegido = int(input("Número del peleador elegido: "))
    ganador = int(input("Número del peleador ganador: "))

    premio = 0

    if elegido == ganador:
        if monto <= 15000:
            premio = monto * 3
        else:
            premio = monto * 4
        premio *= 0.9

    return premio

def apuesta_ruleta(monto):
    apostado = int(input("Número apostado: "))
    ganador = int(input("Número ganador: "))

    premio = 0

    if apostado == ganador:
        if monto < 5000:
            premio = monto * 4
        else:
            premio = monto * 6
        premio *= 0.9

    return premio

def juego_mas_elegido(cont_futbol , cont_boxeo, cont_ruleta):
    
    if cont_futbol == cont_boxeo == cont_ruleta:
        resultado = "Empate"
    
    elif cont_futbol > cont_boxeo and cont_futbol > cont_ruleta:
        resultado = "Futbol"
    
    elif cont_boxeo > cont_futbol and cont_boxeo > cont_ruleta:
        resultado = "Boxeo"
    
    else:
        resultado = "Ruleta"

    return resultado

cant_apostadores = 0
total_apostado = 0
total_premios = 0

cant_futbol = 0
cant_boxeo = 0
cant_ruleta = 0

mayor_premio = -1
mejor_apostador = ""

nombre = input("Ingrese nombre (-1 para salir): ")

while nombre != "-1":
    print("------ DATOS DEL APOSTADOR ------")
    print(f"Apostador: {nombre}")
    monto_apostado = solicitar_y_validar_monto()
    opcion = menu()

    if opcion == 1:
        premio = apuesta_futbol(monto_apostado)
        cant_futbol += 1
    elif opcion == 2:
        premio = apuesta_boxeo(monto_apostado)
        cant_boxeo += 1
    else:
        premio = apuesta_ruleta(monto_apostado)
        cant_ruleta += 1


    print("------ RESULTADO DE LA APUESTA ------")
    print(f"Apostador: {nombre}")
    print(f"Monto: {monto_apostado}")
    print(f"Premio: {premio}")

    cant_apostadores += 1
    total_apostado += monto_apostado
    total_premios += premio

    if premio > mayor_premio:
        mayor_premio = premio
        mejor_apostador = nombre
    
    print("------------------------------------")
    nombre = input("Ingrese nombre (-1 para salir): ")

print("------ RESUMEN DE TU APP DE APUESTAS ------")
print(f"Total apostadores: {cant_apostadores}")
print(f"Total apostado: {total_apostado}")
print(f"Total premios: {total_premios}")
print(f"Fútbol: {cant_futbol}")
print(f"Boxeo clandestino: {cant_boxeo}")
print(f"Ruleta: {cant_ruleta}")
print(f"Juego mas elegido: {juego_mas_elegido(cant_futbol, cant_boxeo, cant_ruleta)}")
print(f"Mayor premio: {mayor_premio}")
print(f"Mejor apostador: {mejor_apostador}")
balance = total_apostado - total_premios
print(f"Balance: {balance}")

if balance > 0:
    print("La app gano dinero")
else:
    print("La app perdio dinero")

