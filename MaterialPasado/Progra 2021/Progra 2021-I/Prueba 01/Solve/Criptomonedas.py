
arch = open("PruebasPy//Prueba1_2021_1//doge.txt","r",encoding= "utf - 8")
linea = arch.readline().strip()

totalMarzo = 0
cantMarzo = 0

menorVolumen = 999999999999999
fechaMenorVolumen = ""

mayorVariacion = -999999999999999
fechaMayorVariacion = ""

mayorPrecio = -99999999
fechaMayorPrecio = ""

sumatoriaTransaccionDiaria = 0
cantDias = 0

dogecoinsCompradas = 0
ultimoAjustado = 0
inversion = 0

while linea != "":
    partes = linea.split(",")
    fecha = partes[0]
    partesFecha = fecha.split("-")
    año = int(partesFecha[0])
    mes = int(partesFecha[1])
    dia = int(partesFecha[2])
    apertura = float(partes[1])
    alto = float(partes[2])
    bajo = float(partes[3])
    cierre = float(partes[4])
    ajustado = float(partes[5])
    volumen = int(partes[6])
    
    if mes == 3:
        totalMarzo += ajustado
        cantMarzo += 1
    
    if volumen < menorVolumen:
        menorVolumen = volumen
        fechaMenorVolumen = fecha
        
    variacionAbsoluta = abs(apertura - cierre)
    if variacionAbsoluta > mayorVariacion:
        mayorVariacion = variacionAbsoluta
        fechaMayorVariacion = fecha
        
    if alto > mayorPrecio:
        mayorPrecio = alto
        fechaMayorPrecio = fecha
        
    sumatoriaTransaccionDiaria += volumen * ((alto + bajo) / 2)
    cantDias += 1
    
    if mes % 2 == 0 and dia == 20:
        dogecoinsCompradas += 420 / alto
        inversion += 420
    
    elif mes % 2 != 0 and dia == 1:
        dogecoinsCompradas += 333 / bajo
        inversion += 333
    
    ultimoAjustado = ajustado
    
    linea = arch.readline().strip()
    
promedioMarzo = round(totalMarzo / cantMarzo, 4)
promedioTransaccionDiaria = sumatoriaTransaccionDiaria / cantDias / 1_000_000
venta = dogecoinsCompradas * ultimoAjustado
utilidad = venta - inversion
print(f"1) El precio promedio ajustado de marzo es de {promedioMarzo}")
print(f"2) El menor volumen fue de {menorVolumen} en la fecha de {fechaMenorVolumen}")
print(f"3) El dia con la mayor variacion fue el {fechaMayorVariacion} con una variacion de {round(mayorVariacion,4)}")
print(f"4) El valor maximo fue el {fechaMayorPrecio} con un monto de {round(mayorPrecio,6)}")
print(f"5) El promedio anual de transaccion diaria es de {round(promedioTransaccionDiaria,4)} millones de dolares")
print(f"6) Nuestro amigo vendio {round(dogecoinsCompradas,4)} dogecoins por un total de {round(venta,4)} dolares con una inversion de {inversion} obtuvo una utilidad de {round(utilidad,4)} dolares")