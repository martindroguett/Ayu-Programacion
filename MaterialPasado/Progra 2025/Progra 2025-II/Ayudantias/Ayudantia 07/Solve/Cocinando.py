def seleccionarIngrediente():
    ingredientes = ["Fideos", "Tomate", "Huevo", "Harina", "Leche"]
    print()
    print("0. Finalizar selección")
    print("1. Fideos")
    print("2. Tomate")
    print("3. Huevo")
    print("4. Harina")
    print("5. Leche")
    
    opcion = int(input("Seleccione un ingrediente: "))
    while opcion < 0 or opcion > 5:
        print("Valor fuera de rango")
        opcion = int(input("Seleccione un ingrediente: "))
        
    if opcion == 0:
        return "0"
    else:
        return ingredientes[opcion - 1]


ingredientesUsuario = []
print("Selecciona tus ingredientes disponibles en casa (0 para finalizar):")
ingrediente = seleccionarIngrediente()
while ingrediente != "0":
    if ingrediente not in ingredientesUsuario:
        ingredientesUsuario.append(ingrediente)
    else:
        print(f"El ingrediente {ingrediente} ya se encuentra añadido")
    print("Ingredientes actuales:")
    print(ingredientesUsuario)
    ingrediente = seleccionarIngrediente()

arch = open("recetas.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    plato = partes[0]
    cantIngredientes = int(partes[1])
    
    print()
    print(f"Plato: {plato}")
    
    FaltaAlgo = False
    for i in range(cantIngredientes):
        ingrediente = partes[2 + i]
        if ingrediente not in ingredientesUsuario:
            print(f"No puedes cocinar el plato {plato}, te hace falta {ingrediente}")
            FaltaAlgo = True
            break
    
    if not FaltaAlgo:
        print(f"Si es posible cocinar el plato {plato}")
    
    linea = arch.readline().strip()
    