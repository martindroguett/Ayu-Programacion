nombre = input("Ingresa el nombre del estudiante: ")

primer = input("Resolvió el primer ejercicio? (s/n): ")

segundo = input("Resolvió el segundo ejercicio? (s/n): ")

tercero = input("Resolvió el tercer ejercicio? (s/n): ")

nota = 1.0

if (primer == "s" and segundo == "s" and tercero == "s"):
    nota = 7.0
elif (segundo == "s" and tercero == "s"):
    nota = 5.5
elif (primer == "s" and tercero == "s"):
    nota = 5.0
elif (primer == "s" and segundo == "s"):
    nota = 4.5
elif (primer == "s" or segundo == "s" or tercero == "s"):
    nota = 3.0
    
print(f"{nombre} obtuvo un {nota}")