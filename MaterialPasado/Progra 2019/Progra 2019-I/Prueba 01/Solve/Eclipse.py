
cantClientes = int(input("Cantidad de clientes a confirmar: "))

cantConfirmados = 0

mayorDiasC = 0
nombreMayorDiasC = ""

totalC = 0
totalDiasExtras = 0
totalIngresoLiberadas = 0

cantStandard = 0
cantPremium = 0

for _ in range(cantClientes):    
    nombre = input("Nombre del cliente: ")
    cantDias = int(input("Días reservados por el cliente: "))
    
    tarifa = input("Tarifa (S/P): ").lower()
    while tarifa != "s" and tarifa != "p":
        tarifa = input("Ingrese opción válida (S/P): ").lower()
    
    if tarifa == "s":
        totalCliente = cantDias * 120
        
    else:
        totalCliente = cantDias * 250

    confirmacion = input("Confirmación (S/N): ").lower()
    while confirmacion != "s" and confirmacion != "n":
        confirmacion = input("Ingrese opción válida (S/N): ").lower()
    
    if confirmacion == "n":
        totalIngresoLiberadas += totalCliente
        devolucion = totalCliente * 0.75
        print(f"Reserva cancelada, devolución: USD {devolucion}")
    else:
        cantConfirmados += 1
        
        if tarifa == "s":
            cantStandard += 1
        else:
            cantPremium += 1
            
        agregar = int(input("Desea agregar más días a la reserva (ingrese 0 si no agrega): "))
        
        if agregar > 0:
            cantDias += agregar
            if tarifa == "s":
                cantExtra = agregar * 120
            else:
                cantExtra = agregar * 250
            
            totalDiasExtras += cantExtra
            totalCliente += cantExtra
        
        if cantDias > mayorDiasC:
            mayorDiasC = cantDias
            nombreMayorDiasC = nombre
        
        totalC += totalCliente
        
        print(f"Reserva confirmada, total: USD {totalCliente}")

print("--------------------------------------------")
if cantClientes > 0:
    porcentajeConfirmado = 100 * (cantConfirmados / cantClientes)
    ingresoCLP = (totalC + (0.25 * totalIngresoLiberadas)) * 680
    print(f"Hoy se ha confirmado a {cantConfirmados} cliente(s) ({porcentajeConfirmado}%)")
    print(f"El cliente confirmado que más días reservó fue: {nombreMayorDiasC}")
    print(f"El ingreso confirmado de hoy es: CLP {ingresoCLP}")
    print(f"El ingreso por días extra agregados es: CLP {totalDiasExtras * 680}")
    print(f"El posible ingreso por habitaciones libres es: CLP {totalIngresoLiberadas * 680}")
    print(f"Habitaciones reservadas: {cantStandard} Standard {cantPremium} Premium")
else:
    print("Hoy no se han realizado llamados")