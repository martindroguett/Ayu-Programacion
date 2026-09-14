n = int(input("Ingrese el número entero positivo para analizar (0 al 1000): "))
while (n != -1):
    while (n < 1 or n > 1000):
        n = int(input("Numero fuera de rango, ingrese nuevamente: "))
    suma_total = 0
    for i in range(1, n + 1):
        suma_total += i

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    potencia = 1
    for i in range(n):
        potencia *= n

    es_primo = True

    if n < 2:
        es_primo = False
    else:
        for i in range(2, n):
            if n % i == 0:
                es_primo = False

    print("======== RESULTADOS =========")
    print(f"> Sumatoria: {suma_total}")
    print(f"> Factorial: {factorial}")
    print(f"> Potencia ({n}^{n}): {potencia}")

    if es_primo:
        print(f"> El número {n} es primo.")
    else:
        print(f"> El número {n} no es primo.")
    print("=============================")
    n = int(input("Ingresa otro numero para continuar, para salir ingresa -1: "))
print("Saliendo del programa...")