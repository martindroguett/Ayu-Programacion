arch = open("ventas.txt", "r", encoding="utf-8")

linea = arch.readline().strip()

mayor = 0
mayorFecha = ""

while (linea != ""):
    partes = linea.split(";")

    fecha = partes[1]

    linea = arch.readline().strip()
    partes = linea.split(";")
    tipo = partes[0]

    sumaVentas = 0

    while (tipo != "F" and tipo != ""):
        producto = partes[1]
        precio = int(partes[2])
        cantidad = int(partes[3])

        sumaVentas += (precio * cantidad)

        linea = arch.readline().strip()
        partes = linea.split(";")
        tipo = partes[0]

    if (sumaVentas > mayor):
        mayor = sumaVentas
        mayorFecha = fecha

    print(f"{fecha}: ${sumaVentas}")

print(f"fecha con mayores ventas: {mayorFecha} (${mayor})")