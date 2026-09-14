
print("Bienvenido a la picada de Nokotan!")
print()

seguir = "si"

numPedido = 0
cantCanjes = 0

totalGlobal = 0

masCostoso = 0
pedidoMasCostoso = 0

cantArroz = 0
cantSopa = 0
cantGalletas = 0

while seguir != "no":
    numPedido += 1
    print(f"Pedido #{numPedido}!")
    print("MENU DE LA PICADA")
    print("[ARROZ] Arroz de Bashame ($2500)")
    print("[SOPA] Sopa de Astas ($1500)")
    print("[GALLETAS] Galletas Shika ($1000)")
    print("[PAGAR] Realizar pago del pedido")

    plato = input("Selecciona un plato: ").lower()
    totalPedido = 0

    while plato != "pagar":
        if plato == "arroz":
            totalPedido += 2500
            cantArroz += 1
        elif plato == "sopa":
            totalPedido += 1500
            cantSopa += 1
        elif plato == "galletas":
            totalPedido += 1000
            cantGalletas += 1
        plato = input("Selecciona un plato: ").lower()

    print(f"Total del pedido: ${totalPedido}")
    seguir = input("Desea seguir procesando pedidos: ").lower()
    
    if seguir == "nun!":
        cantCanjes += 1
        print("Excelente! Se ha aplicado el descuento del 10%")
        totalPedido -= 0.1 * totalPedido
        print(f"Nuevo total del pedido: {totalPedido}")
        seguir = input("Desea seguir procesando pedidos: ").lower()
    
    if totalPedido > masCostoso:
        masCostoso = totalPedido
        pedidoMasCostoso = numPedido
    
    totalGlobal += totalPedido
    print()

menor = 99999
menosPedido = ""
if cantArroz < cantGalletas and cantArroz < cantSopa:
    menosPedido = "Arroz de Bashame"
    menor = cantArroz
elif cantSopa < cantArroz and cantSopa < cantGalletas:
    menosPedido = "Sopa de Astas"
    menor = cantSopa
else:
    menosPedido = "Galletas Shika"
    menor = cantGalletas

print("RESUMEN DEL DIA!")
print(f"Pedidos realizados: {numPedido}")
print(f"Ganancia: ${totalGlobal}")
print(f"Pedido más costoso: #{pedidoMasCostoso} (${masCostoso})")
print(f"Plato menos pedido: {menosPedido} ({menor})")
print(f"Num. veces canje de descuento: {cantCanjes}")