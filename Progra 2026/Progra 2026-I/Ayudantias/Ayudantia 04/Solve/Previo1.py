archivo = open("numeros.txt","r",encoding="utf-8")
linea = archivo.readline().strip()

contador = 0
suma = 0

mayor = -99999
menor = 99999
while linea != "":
    numero = int(linea)
    #B.
    if numero % 3 == 0:
        print(numero)
    #C.
    contador += 1
    suma += numero
    
    #D.
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
        
    linea = archivo.readline()
    
print(f"""Contador: {contador}
Sumatoria: {suma}""")
print(f"El mayor número es {mayor}")   
print(f"El menor número es {menor}")
      