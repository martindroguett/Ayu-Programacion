cartas = 250000
matcha = 7000
donas = 15000
kuromi = 50000
voley = 120000
ropa = 200000

acumulado = 0

opcion = input("Lleva cartas Pokémon? (s/n): ")

if opcion == "s":
    acumulado+=cartas
    
opcion = input("Lleva matcha latte? (s/n): ")

if (opcion == "s"):
    acumulado+=matcha
    
opcion = input("Lleva donas? (s/n): ")

if (opcion == "s"):
    acumulado+=donas

opcion = input("Lleva merch Kuromi? (s/n): ")

if (opcion == "s"):
    acumulado+=kuromi
    
opcion = input("Lleva accesorios de voleibol? (s/n): ")

if (opcion == "s"):
    acumulado+=voley
    
opcion = input("Lleva ropa? (s/n): ")

if (opcion == "s"):
    acumulado+=ropa
    
print(f"Total acumulado: ${acumulado}")

descuento = 0

if acumulado >= 200000:
    descuento = 15
    acumulado *= 0.85
elif acumulado >= 100000:
    descuento = 10
    acumulado *= 0.90
elif acumulado >= 50000:
    descuento = 5
    acumulado *= 0.95
    
print(f"Descuento aplicado: {descuento}%")
print(f"Precio final: ${int(acumulado)}")