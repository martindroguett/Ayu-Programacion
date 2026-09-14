print("Calculadora de viaje")
cantMillas = int(input("Ingrese la cantidad de millas: "))
cantKm = round(cantMillas * 1.61, 2)

velocidadMph = int(input("Velocidad a la que irán (mph): "))
velocidadKmh = round(velocidadMph * 1.609, 2)

print()

if velocidadKmh > 140:
    print(f"Rick conduciendo a {velocidadKmh} km/h está superando el límite permitido en carretera")
    print()

tiempoH = round(cantKm / velocidadKmh, 2)
tiempoM = round(tiempoH * 60, 2)

print("===RESULTADOS OBTENIDOS===")
print(f"{cantMillas} millas equivalen a {cantKm} kilómetros")
print(f"{velocidadMph} mph equivalen a {velocidadKmh} km/h")
print(f"Con los datos ingresados el viaje tardará aproximadamente {tiempoH} horas lo que tambien equivale a {tiempoM} minutos")
