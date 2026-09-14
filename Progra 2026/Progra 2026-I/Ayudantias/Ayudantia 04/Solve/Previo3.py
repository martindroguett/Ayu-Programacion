archivo = open("temperaturas_regiones.txt","r",encoding="utf-8")
linea = archivo.readline().strip()

menorTempGlobal = 99999
ciudadFria = ""

menorTempRegion = 9999
regionFria = ""

while linea != "":
    partes = linea.split(";")
    region = partes[0]
    cant_ciudades= int(partes[1])

    mayorTempRegion = -99999
    ciudadCalurosa = ""

    sumaTempRegion = 0
    cantidadTempRegion = 0
    for i in range(cant_ciudades):
        linea = archivo.readline()
        partes_ciudad = linea.split(",")
        
        ciudad = partes_ciudad[0]
        cantidad_partes = len(partes_ciudad)
        
        sumaTemperaturasCiudad = 0
        for j in range(1,cantidad_partes):
            temperatura = float(partes_ciudad[j])
            
            sumaTemperaturasCiudad += temperatura
            
            if temperatura > mayorTempRegion:
                mayorTempRegion = temperatura
                ciudadCalurosa = ciudad
            if temperatura < menorTempGlobal:
                menorTempGlobal = temperatura
                ciudadFria = ciudad
                
            sumaTempRegion += temperatura
            cantidadTempRegion += 1
        
        promedioTemperaturaCiudad = sumaTemperaturasCiudad/(cantidad_partes-1)
        print(f"Promedio de {ciudad}: {promedioTemperaturaCiudad}°C")
        
    promedioRegion = round(sumaTempRegion/cantidadTempRegion,2)
    if promedioRegion < menorTempRegion:
        menorTempRegion = promedioRegion
        regionFria = region
        
    print(f"Ciudad más calurosa de {region} -> {ciudadCalurosa} con {mayorTempRegion}°C")
        
    print(f"Temperatura promedio de {region}: {promedioRegion}")
    
    
    linea = archivo.readline()

print(f"Ciudad mas fria del texto: {ciudadFria} con {menorTempGlobal}°C")
print(f"La región más fría fue {regionFria} con promedio {menorTempRegion}°C")