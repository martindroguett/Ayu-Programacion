def menu(mensaje):
    print(mensaje)
    print("1) Propulsión.")
    print("2) Navegación.")
    print("3) Soporte vital.")
    opcion = input("Ingrese una opción ('fin' para salir): ").lower()
    return opcion

def obtener_mensaje_estado(estado):
    if estado == "operativo":
        return "todo funcionando correctamente."
    elif estado == "en revisión":
        return "requiere supervisión técnica."
    elif estado == "crítico":
        return "atención inmediata requerida."

def informar_modulo(nombre, estado):
    mensaje = obtener_mensaje_estado(estado)
    print()
    print("Enviando mensaje...")
    print(f"Módulo de {nombre}: {mensaje}")


opcion = menu("Bienvenido! ¿Qué módulo desea chequear?")

while opcion != "fin":

    while opcion != "propulsión" and opcion != "navegación" and opcion != "soporte vital" and opcion != "fin":
        opcion = input("Por favor, ingrese una opción válida: ").lower()
    
    estado = input("Ingrese el estado del módulo: ").lower()
    
    while estado != "operativo" and estado != "en revisión" and estado != "crítico":
        estado = input("Por favor, ingrese estado válido: ").lower()
    
    informar_modulo(opcion, estado)
    
    print()
    print("="*30)
    print()
    opcion = menu("¿Desea chequear otro módulo?")
    
print("Saliendo del programa...")

