
nota = float(input("Ingrese nota: "))

suma = 0
cantidad = 0

rojos = 0

while (nota != 0):
    if (nota < 1 or nota > 7):
        print("Nota inválida")

    else:
        suma += nota
        cantidad += 1

        if (nota < 4):
            rojos += 1

print(f"El promedio es: {suma / cantidad}")
print("Las notas rojas son:", rojos)