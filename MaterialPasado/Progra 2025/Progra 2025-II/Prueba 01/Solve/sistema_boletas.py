
def comprobarNegativo(valor, mensaje):
    if valor < 0:
        print(mensaje)

def aplicarDescuento(valor):
    if valor >= 5000 and valor <= 9999:
        return 2250
    elif valor >= 10000 and valor < 19999:
        return 5500
    return 0

contraseña = input("Ingrese la contraseña para acceder al sistema: ").lower()
while contraseña != "venta2025":
    print("Error al ingresar la contraseña")
    contraseña = input("Ingrese la contraseña nuevamente para acceder al sistema: ")

print("---- Acceso al sistema ---")
print("=========================== ")
print("Registrando productos")
print("===========================")

subtotal = 0
iva = 0
descuentos_aplicados = 0
boleta = ""

producto = input("Ingrese el producto: ")

while producto != "fin":
    cantidad = int(input("Ingrese la cantidad vendida: "))
    comprobarNegativo(cantidad, "malo")
    valor = int(input("Ingrese el valor del producto: "))
    comprobarNegativo(cantidad, "malo")
    tiene_descuento = input("indique si aplica descuento (si/no): ").lower()

    total = valor * cantidad

    if tiene_descuento == "si":
        print("Aplicando descuento")
        print("procesando monto ...")
        descuento = aplicarDescuento(total)
        descuentos_aplicados += descuento
        total -= descuento
        print(f"aplica descuento de: ${descuento}")
    else:
        print("No aplica descuento")

    boleta += f"Producto: {producto} | Cantidad {cantidad} | Total: ${valor}\n"
    subtotal += total
    print()
    producto = input("Ingrese el producto: ")

print("=========== BOLETA ==========")
print(boleta)
print("------------------------------")
print(f"DESCUENTOS APLICADOS: ${descuentos_aplicados}")
print(f"SUBTOTAL: ${subtotal}") 
iva = 0.19 * subtotal
print(f"IVA(19%): {iva}$")
print(f"TOTAL A PAGAR: {subtotal + iva}$")