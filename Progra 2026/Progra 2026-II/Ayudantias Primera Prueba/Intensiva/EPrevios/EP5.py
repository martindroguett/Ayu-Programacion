n = int(input("Ingrese número: "))

divisores = 0

for i in range (2,n):
    if (n % 2 == 0):
        divisores += 1

if (n != 1 and divisores == 0):
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")