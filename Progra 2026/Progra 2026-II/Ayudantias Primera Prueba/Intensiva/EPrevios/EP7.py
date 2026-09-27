subidas = 0
racha = 0

anterior = -10000

for i in range(8):
    hoy = int(input("Ingrese temperatura: "))

    if (hoy > anterior):
        subidas += 1
        racha += 1

    else:
        racha = 0

    anterior = hoy

print(f"La cantidad de subidas fue de {subidas}")
print(f"La racha más larga fue de {racha} días")
