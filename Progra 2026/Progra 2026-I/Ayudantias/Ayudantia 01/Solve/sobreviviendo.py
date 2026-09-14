print("Bienvenido forastero, ¿Qué quieres hacer?")
print("1) Comprar Suministros")
print("2) Salir")
opcion = int(input("Ingrese una opcion: "))
print()

if opcion == 1:
    montoDisponible = float(input("Ingresa el monto disponible: "))
    gasto = float(input("Ingresa el monto que deseas gastar: "))

    if gasto > montoDisponible:
        print("No tienes dinero suficiente")

    else:
        if gasto <= 20000:
            descuento = 0
        elif gasto <= 50000:
            descuento = 0.05
        elif gasto <= 100000:
            descuento = 0.10
        else:
            descuento = 0.15

        gastoDescuento = gasto - (gasto * descuento)

        if gasto % 2 == 0:
            gastoDescuento = gastoDescuento - (gastoDescuento * 0.03)
            print("El mercader del refugio te dio un descuento extra del 3%")

        dineroRestante = montoDisponible - gastoDescuento

        print()
        print("===RESUMEN DE LA COMPRA===")
        print(f"Monto inicial: {montoDisponible}")
        print(f"Gasto original: {gasto}")
        print(f"Gasto con descuento: {gastoDescuento}")
        print(f"Dinero restante: {dineroRestante}")
elif opcion == 2:
    print("Buena suerte sobreviviendo")