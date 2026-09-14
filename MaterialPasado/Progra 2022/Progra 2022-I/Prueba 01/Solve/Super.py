
arch = open("problema1.txt","r",encoding= "utf-8")

numSucursales = int(arch.readline().strip())

totalVentasGeneral = 0

mayorVentasSucursal = -1
nombreSucursalMayorVentas = ""

mayorVentaProductoGeneral = -1
nombreSucursalProductoCaro = ""
nombreProductoCaro = ""

for _ in range(numSucursales):
    linea = arch.readline().strip()
    partes = linea.split(",")
    nombreSucursal = partes[0]
    cantidadProductos = int(partes[1])
    
    mayorVentaEnSucursal = -1
    nombreProductoMayorVentaSucursal = ""
    
    cantidadVentasUnitarias = 0

    totalVentasSucursal = 0
    
    for _ in range(cantidadProductos):
        linea = arch.readline().strip()
        partes = linea.split(",")
        nombreProducto = partes[0]
        cantidadVendida = int(partes[1])
        precioUnitario = int(partes[2])
        
        ventaProducto = precioUnitario * cantidadVendida
        
        if ventaProducto > mayorVentaEnSucursal:
            mayorVentaEnSucursal = ventaProducto
            nombreProductoMayorVentaSucursal = nombreProducto
        
        if cantidadVendida == 1:
            cantidadVentasUnitarias += 1
        
        totalVentasGeneral += ventaProducto
        
        if ventaProducto > mayorVentaProductoGeneral:
            mayorVentaProductoGeneral = ventaProducto
            nombreSucursalProductoCaro = nombreSucursal
            nombreProductoCaro = nombreProducto
        
        totalVentasSucursal += ventaProducto
        
    if totalVentasSucursal > mayorVentasSucursal:
        mayorVentasSucursal = totalVentasSucursal
        nombreSucursalMayorVentas = nombreSucursal
        
    if cantidadProductos == 0:
        print(f"No hubo ventas en la sucursal {nombreSucursal}")
    else:    
        print(f"Producto con mayor venta en sucursal {nombreSucursal}")
        print(f"es {nombreProductoMayorVentaSucursal} con total {mayorVentaEnSucursal}")
        porcentajeUnitarias = 100 * (cantidadVentasUnitarias / cantidadProductos)
        print(f"porcentaje de ventas unitarias es {porcentajeUnitarias} %")
    print("")

print(f"Total de ventas {totalVentasGeneral}")
print(f"La sucursal con más ventas es {nombreSucursalMayorVentas}")
print(f"con total de ventas {mayorVentasSucursal}")
print(f"El producto más caro fue {nombreProductoCaro}")
print(f"vendido en la sucursal {nombreSucursalProductoCaro}")
print(f"con un precio de {mayorVentaProductoGeneral}")