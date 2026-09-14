limiteBencina= 8
kmTotales = 0
combustibleTotal = 0
gasto = 0
mayorGasto = -5000

km = float(input("Kilómetros recorridos (-1 para terminar): "))

while km != -1:# Fin de datos.
    
    trayecto = input("Tipo de trayecto (ciudad/autopista): ")
    while(trayecto != "ciudad" and trayecto != "autopista"):
        trayecto = input("Tipo de trayecto (ciudad/autopista): ")

    if trayecto == "ciudad":
        gasto = km * 0.08
    else:
        gasto = km * 0.05
        
    lluvia = input("¿Está lloviendo? (s/n): ")
    if(lluvia == "s"):
        gasto *= 1.2

    if combustibleTotal + gasto > limiteBencina: #Condicion de salida, gasto + combustible total.
        print("Matías se quedó sin bencina, debe volver a casa")
        break
    
    if gasto > mayorGasto: #Sacamos el mayor gasto del viaje.
        mayorGasto = gasto
    
    kmTotales += km
    combustibleTotal += gasto

    km = float(input("Kilómetros recorridos (-1 para terminar): "))

print()
print("*"* 12 + "DIA DE MANUGO" + 12*"*")
print(f"Kilómetros totales: {kmTotales}")
print("Combustible total gastado:", round(combustibleTotal, 2))
print(f"Mayor gasto en un solo trayecto: {mayorGasto}")