# precios
precio_simple = 1000
precio_napo = 1500
precio_vegana = 1300
precio_condimentos = 200
# costos
costo_simple = 400
costo_napo = 900
costo_vegana = 700
costo_condimentos = 50
# contadores
cant_vendidas = 0
cant_simple = 0
cant_napo = 0
cant_vegana = 0

ganancias = 0
costos = 0

chaparra_mas_vendida = ""

opcion = 0

while (opcion != 3):
    print("Bienvenido Fernando! ¿Que quieres hacer?")
    print("1. Agregar venta.")
    print("2. Mostrar resumen del dia.")
    print("3. Salir del programa.")
    opcion = int(input("Ingresa tu opcion: "))

    while (opcion != 1 and opcion != 2 and opcion != 3):
        opcion = int(input("Opcion invalida, ingrese nuevamente: "))

    if opcion == 1:
        tipo_chaparra = input("Ingresa el tipo de chaparra vendida (Simple, Napolitana, Vegana): ")
        while (tipo_chaparra != "Simple" and tipo_chaparra != "Napolitana" and tipo_chaparra != "Vegana"):
            tipo_chaparra = input("Opcion invalida, ingrese nuevamente: ")
        if tipo_chaparra == "Simple":
            cant_simple += 1
            ganancias += precio_simple
            costos += costo_simple
        elif tipo_chaparra == "Napolitana":
            cant_napo += 1
            ganancias += precio_napo
            costos += costo_napo
        elif tipo_chaparra == "Vegana":
            cant_vegana += 1
            ganancias += precio_vegana
            costos += costo_vegana
        agregar_condimentos = input("Agrega condimentos? (Si, No): ")
        if agregar_condimentos == "Si":
            ganancias += precio_condimentos
            costos += costo_condimentos
        cant_vendidas += 1
        print(f"Chaparrita {tipo_chaparra} agregada!")
    elif opcion == 2:
        if cant_vendidas < 1:
            print("¡Todavia no vendes nada!")
        else:
            # porcentajes
            porc_simple = (cant_simple / cant_vendidas) * 100
            porc_napo = (cant_napo / cant_vendidas) * 100
            porc_vegana = (cant_vegana / cant_vendidas) * 100
            ganancia_total = ganancias - costos
            if cant_simple >= cant_napo and cant_simple >= cant_vegana:
                chaparra_mas_vendida = "Simple"
            elif cant_napo >= cant_simple and cant_napo >= cant_vegana:
                chaparra_mas_vendida = "Napolitana"
            else:
                chaparra_mas_vendida = "Vegana"

            print("====== RESUMEN DEL DIA ======")
            print(f"Cantidad de chaparritas vendidas: {cant_vendidas} ")
            print(f"Ganancia: {ganancias}$")
            print(f"Costo total: {costos}$")
            print(f"Ganancia total: {ganancia_total}$")
            print("Porcentaje de venta de cada chaparrita: ")
            print(f"Chaparrita simple: {round(porc_simple,2)}%")
            print(f"Chaparrita napolitana: {round(porc_napo,2)}%")
            print(f"Chaparrita vegana: {round(porc_vegana,2)}%")
            print(f"Chaparrita más vendida: {chaparra_mas_vendida}")
    elif opcion == 3:
        print("Adios Fernando, suerte con las ventas!")