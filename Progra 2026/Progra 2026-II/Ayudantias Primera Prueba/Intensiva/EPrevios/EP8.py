arch = open("notas.txt", "r", encoding="utf-8")

linea = arch.readline().strip()

mejor = 0
mejorNombre = ""

while (linea != ""):
    partes = linea.split(",")

    nombre = partes[0]
    notas = int(partes[1])

    suma = 0

    for i in range(notas):
        linea = arch.readline().strip()
        suma += float(linea)

    promedio = suma/notas

    if (promedio > mejor):
        mejor = promedio
        mejorNombre = nombre

    print(f"{nombre} tiene promedio {promedio}")

    linea = arch.readline().strip()
