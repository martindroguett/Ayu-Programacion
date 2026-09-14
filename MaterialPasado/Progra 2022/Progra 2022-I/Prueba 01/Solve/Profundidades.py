
refugio = input("Ingrese A para Norte o B para Sur: ").upper()
while refugio != "A" and refugio != "B":
    refugio = input("Error, Ingrese A para Norte o B para sur: ").upper()
    
while refugio != "FIN":
    cantHabitables = 0
    cantInhabitables = 0
    cantRefugios = 0

    mayorFactor = -1
    refugioConveniente = ""
    
    distanciaMasConveniente = 0
    
    arch = open(refugio + ".txt","r",encoding= "utf-8")
    linea = arch.readline().strip()
        
    while linea != "":
        partes = linea.split(",")
        nombre = partes[0]
        distancia = int(partes[1])
        capacidad = int(partes[2])
        suministros = int(partes[3])
        radiacion = partes[4].lower()
        actividad = partes[5].lower()
        
        if refugio == "A":
            distancia -= 200
        else:
            distancia += 200
            
        #Pregunta 1
        if capacidad >= 20 and radiacion == "protegido" and actividad == "true":
            factor = (1800/distancia) + (12 * suministros / 90)
            if factor > mayorFactor:
                mayorFactor = factor
                refugioConveniente = nombre
                distanciaMasConveniente = distancia
            
        #Pregunta 2
        if radiacion == "protegido" and capacidad >= 30:
            cantHabitables += 1
        #Pregunta 3
        else:
            cantInhabitables += 1
        cantRefugios += 1
        
        linea = arch.readline().strip()

    print(f"1) El refugio más conveniente es {refugioConveniente} con un factor de {mayorFactor}")
    print(f"2) Hay {cantHabitables} refugios habitables")
    porcentajeInhabitable = 100 * (cantInhabitables / cantRefugios)
    print(f"3) Hay {cantInhabitables} refugios inhabitables equivalentes a {round(porcentajeInhabitable,2)} % del sector analizado")
    
    #Pregunta 4
    for i in range(0,41,10):
        nudos = i + 1
        horas = int(distanciaMasConveniente // nudos)
        minutos = int((distanciaMasConveniente % nudos) * 60 / nudos)
        print(f"4) Para llegar a {refugioConveniente} faltan {horas} horas y  {minutos} minutos a {nudos} nudos")
    
    refugio = input("Ingrese A para Norte o B para Sur: ").upper()
    while refugio != "FIN" and refugio != "A" and refugio != "B":
        refugio = input("Error, Ingrese A para Norte o B para sur: ").upper()