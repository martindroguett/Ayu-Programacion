texto = input("Ingrese texto: ")

vocales = 0

for i in texto.lower():
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        vocales += 1

print(f"El texto tiene {vocales} vocales")