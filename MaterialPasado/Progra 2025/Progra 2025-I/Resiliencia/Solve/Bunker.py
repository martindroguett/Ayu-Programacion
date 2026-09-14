
print("SISTEMA DE ACCESO BUNKER OMEGA - AÑO 2049")
print("Inicio de validacion de operadores...")

print("\nNueva solicitud de acceso")
codigo = input("Ingrese su codigo de acceso (o '0000' para cerrar jornada): ")

cantIntentaron = 0
cantExitosos = 0
cantBloqueados = 0
emergencia = "NO ACTIVADO"

while codigo != "0000" and emergencia != "ACTIVADO":
    cantIntentaron += 1
    intentos = 3
    
    while intentos > 0:
        if codigo == "0000":
            break
        
        if codigo == "7429":
            print("Acceso concedido")
            cantExitosos += 1
            deseaActivar = input("¿Desea activar el Protocolo de Emergencia? (si/no): ").lower()
            if deseaActivar == "si":
                emergencia = "ACTIVADO"
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Codigo incorrecto. Intentos restantes: {intentos}")
                codigo = input("Reintente su código: ")

    if intentos == 0 and emergencia == "NO ACTIVADO":
        print("Acceso denegado. Usuario bloqueado")
        cantBloqueados += 1

    if emergencia != "ACTIVADO" and codigo != "0000":
        print("\nNueva solicitud de acceso")
        codigo = input("Ingrese su codigo de acceso (o '0000' para cerrar jornada): ")

print("\nCerrando sistema de validación...")
print("\nREPORTE FINAL DE ACCESOS")
print(f"Total de personas que intentaron ingresar: {cantIntentaron}")
print(f"Cantidad de accesos exitosos: {cantExitosos}")
print(f"Cantidad de personas bloqueadas: {cantBloqueados}")
print(f"Protocolo de emergencia {emergencia}")

