import math

arch = open("datos.txt","r",encoding="utf-8")
linea = arch.readline().strip()

mayorTemp = -99999
zonaMayorTemp = 0
regionMayorTemp = 0
cuidadMayorTemp = ""

cuidadMayor = -9999
cuidadMasCalida = ""

menorRegion = 999999
regionMasFria = ""

mayorDesviacion = 0
cuidadMayorDesviacion = ""

cantMenos1 = 0

while linea != "":
    partes = linea.split(",")
    region = partes[0]
    cantCiudades = int(partes[1])
    
    #Pregunta 3
    sumPromedios = 0
    
    for _ in range(cantCiudades):
        linea = arch.readline().strip()
        partes = linea.split(",")
        ciudad = partes[0]
        cantTemperaturas = int(partes[1])
        
        sumaTemperaturas = 0
        
        for i in range(2, len(partes)):
            temperatura = float(partes[i])
            sumaTemperaturas += temperatura
            
            #Pregunta 2
            if temperatura > mayorTemp:
                mayorTemp = temperatura
                zonaMayorTemp = i - 1
                regionMayorTemp = region
                cuidadMayorTemp = ciudad
                
            #Pregunta 6
            if temperatura < -1:
                cantMenos1 += 1
        
        promedioTemperaturas = sumaTemperaturas / cantTemperaturas
        sumPromedios += promedioTemperaturas
        
        #Pregunta 4
        if promedioTemperaturas > cuidadMayor:
            cuidadMayor = promedioTemperaturas
            cuidadMasCalida = ciudad
            
        #Pregunta 5
        sumatoria = 0
        for i in range(2, len(partes)):
            temperatura = float(partes[i])
            sumatoria += (temperatura - promedioTemperaturas)**2
        
        desviacionEstandar = math.sqrt(sumatoria / cantTemperaturas)
        
        if desviacionEstandar > mayorDesviacion:
            mayorDesviacion = desviacionEstandar
            cuidadMayorDesviacion = ciudad

        arch2 = open("intervalos.txt","r",encoding="utf-8")
        linea2 = arch2.readline().strip()
        
        estado = ""
        
        while linea2 != "":
            partes = linea2.split(",")
            cuidadIntervalo = partes[0]
            minimo = float(partes[1])
            maximo = float(partes[2])
            
            #Pregunta 1
            if ciudad == cuidadIntervalo:
                if promedioTemperaturas < maximo and promedioTemperaturas > minimo:
                    estado = "NORMAL"
                elif promedioTemperaturas > maximo:
                    estado = "CÁLIDA"
                else:
                    estado = "FRÍA"
            linea2 = arch2.readline().strip()
            
        print(f"El estado de la cuidad {ciudad} es {estado}")
    
    #Pregunta 3
    promedioRegion = sumPromedios / cantCiudades
    
    if promedioRegion < menorRegion:
        menorRegion = promedioRegion
        regionMasFria = region

    linea = arch.readline().strip()

print(f"La zona más cálida es la N° {zonaMayorTemp}, {cuidadMayorTemp}, {regionMayorTemp} con {mayorTemp}°")
print(f"La región más fría es {regionMasFria} con {round(menorRegion,2)}°")
print(f"La ciudad más cálida es {cuidadMasCalida} con {round(cuidadMayor,2)}°")
print(f"La ciudad con más variabilidad de temperatura es {cuidadMayorDesviacion} con {round(mayorDesviacion,2)}°")
print(f"La cantidad de sensores fríos: {cantMenos1}")