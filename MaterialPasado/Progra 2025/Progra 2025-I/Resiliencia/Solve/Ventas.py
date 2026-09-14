
arch = open("data-ventas-24-25.txt", "r", encoding= "utf-8")
linea = arch.readline().strip()

totalVentas = 0
cantVentas = 0

totalElectronics = 0
totalSports = 0

totalEntre2024 = 0
totalEntre2025 = 0

idUnitarioMayorH = 0
mayorUnitarioH = -1

idUnitarioMayorO = 0
mayorUnitario0 = -1

while linea != "":
    partes = linea.split(",")
    id = int(partes[0])
    
    fecha = partes[1]
    partesFecha = fecha.split("/")
    dia = int(partesFecha[0])
    mes = int(partesFecha[1])
    año = int(partesFecha[2])
    
    categoria = partes[2]
    cantUnidades = int(partes[3])
    total = int(partes[4])
    
    #Pregunta 1
    cantVentas += 1
    totalVentas += total
    
    #Pregunta 2 y 3
    if categoria == "Electronics":
        totalElectronics += total
    elif categoria == "Sports":
        totalSports += total
    
    #Pregunta 4 y 5
    if mes == 6 and año == 2024 and dia >= 1 and dia <= 10:
        totalEntre2024 += total
    elif (mes == 1 and dia >= 1 and año == 2025) or (mes == 2 and año == 2025 and dia <= 14):
        totalEntre2025 += total
    
    #Pregunta 6 y 7
    precioUnitario = total / cantUnidades
    if categoria == "Health":
        if precioUnitario > mayorUnitarioH:
            mayorUnitarioH = precioUnitario
            idUnitarioMayorH = id
    elif categoria == "Outdoor":
        if precioUnitario > mayorUnitario0:
            mayorUnitario0 = precioUnitario
            idUnitarioMayorO = id
    linea = arch.readline().strip()

print("--Reporte--")
promedioVentas = totalVentas / cantVentas
print(f"Promedio de ventas: {int(promedioVentas)}")
print(f"Total de ventas de la categoría Electronics: ${totalElectronics}")
print(f"Total de ventas de la categoría Sports: ${totalSports}")
print(f"Total de ventas entre 01/06/2024 y 10/06/2024: ${totalEntre2024}")
print(f"Total de ventas entre 01/01/2025 y 14/02/2025: ${totalEntre2025}")
print(f"ID de la venta con el precio unitario mayor en Health: {idUnitarioMayorH}")
print(f"ID de la venta con el precio unitario mayor en Outdoor: {idUnitarioMayorO}")