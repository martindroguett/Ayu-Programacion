
categoria = input("Ingrese categoría del producto, Belleza=B, Limpieza=L, Comida=C:").lower()
while categoria != "b" and categoria != "l" and categoria != "c":
    categoria = input("Ingrese categoría del producto, Belleza=B, Limpieza=L, Comida=C:").lower()

mayor = -1
categoriaMayor = ""

menor = 999999
categoriaMenor = ""

totalImpuestos = 0

while categoria != "fin":
    precio = int(input("Ingrese precio del producto: "))
    
    while precio < 0:
        precio = int(input("Ingrese precio del producto: "))
        
    if categoria == "b":
        impuesto = 0.2 * precio
    elif categoria == "l":
        impuesto = 0.1 * precio
    else:
        impuesto = 0.15 * precio
    
    print(f"Valor del impuesto a pagar: {impuesto}")
    final = precio + impuesto
    print(f"Valor final por pagar por el producto: {final}")
    
    if impuesto > mayor:
        mayor = impuesto
        if categoria == "b":
            categoriaMayor = "Belleza"
        elif categoria == "l":
            categoriaMayor = "Limpieza"
        else:
            categoriaMayor = "Comida"
    
    if impuesto < menor:
        menor = impuesto
        if categoria == "b":
            categoriaMenor = "Belleza"
        elif categoria == "l":
            categoriaMenor = "Limpieza"
        else:
            categoriaMenor = "Comida"
            
    totalImpuestos += impuesto
    
    print("")
    categoria = input("Ingrese categoría del producto, Belleza=B, Limpieza=L, Comida=C:").lower()
    while categoria != "fin" and categoria != "b" and categoria != "l" and categoria != "c":
        categoria = input("Ingrese categoría del producto, Belleza=B, Limpieza=L, Comida=C:").lower()

print("")
print(f"a) El impuesto más alto fue de: {mayor} En un producto de {categoriaMayor}")
print(f"b) El impuesto más bajo fue de: {menor} En un producto de {categoriaMenor}")
print(f"c) El monto total de impuesto es: {totalImpuestos}")