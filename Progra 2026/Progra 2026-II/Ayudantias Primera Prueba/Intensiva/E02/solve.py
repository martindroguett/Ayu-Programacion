
contra = input("Ingrese contraseña: ")

while (contra != "venta2025"):
    print("Contraseña incorrecta!")
    contra = input("Ingrese contraseña: ")


print()
print("Bienvenida al sistema Doña Juanita")        

producto = input("Ingrese el producto: ").lower()

boleta = ""

subtotal = 0
descuentosTotales = 0 

while (producto != "fin"):
    
    cantidad = int(input("Ingrese la cantidad vendida: "))

    while (cantidad <= 0):
        
        print("Cantidad inválida!")
        
        cantidad = int(input("Ingrese la cantidad vendida: "))

    precio = int(input("Ingrese el precio del producto: "))


    while (precio <= 0):
        
        print("Precio inválido!")
        
        precio = int(input("Ingrese el precio del producto: "))
        
    aplica = input("Indique si aplica descuento (si/no): ").lower()
        
    while (aplica != "si" and aplica != "no"):
        print("Ingrese una opción válida (si/no)")
        
        aplica = input("Indique si aplica descuento (si/no): ").lower()
    
    venta = precio * cantidad
    
    if (aplica == "si"):
        print("Procesando monto...")
        
        if (venta >= 5000 and venta <= 9999):
            descuento = 2250
        
        elif (venta >= 10000 and venta <= 19999):
            descuento = 5500
        
        else:
            descuento = 0
            
        descuentosTotales += descuento
            
        print(f"Aplica descuento de ${descuento}")
    
    else:
        print("No aplica descuento")
        descuento = 0
        
    boleta += (f"Producto: {producto} | Cantidad: {cantidad} | Total: ${venta}\n")
    
    subtotal += (venta - descuento)
    
    print()
    producto = input("Ingrese el producto: ").lower()
  
if (boleta == ""):
    
    print("Sin productos")
    
else:
    print("=== Boleta ===")
    print(boleta)

print("-"*20)
print(f"Descuentos aplicados: ${descuentosTotales}")
print(f"Subtotal: ${subtotal}")
print(f"IVA(19%): ${subtotal * 0.19}")
print(f"Total: ${subtotal * 1.19}")