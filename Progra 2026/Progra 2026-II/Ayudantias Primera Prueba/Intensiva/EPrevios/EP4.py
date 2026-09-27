n = input("Ingrese un número: ")

digitos = 0
suma = 0

for i in n:
    digitos += 1

    suma += (int(i))

print(f"Dígitos: {digitos}")
print(f"Suma: {suma}")