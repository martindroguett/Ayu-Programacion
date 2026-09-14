
diaIngresado = input("Ingrese el dia de la semana: (-1 para terminar) ").lower()

while diaIngresado != "-1" and diaIngresado != "lunes" and diaIngresado != "martes" and diaIngresado != "miercoles" and diaIngresado != "jueves" and diaIngresado != "viernes" and diaIngresado != "sabado" and diaIngresado != "domingo":
    diaIngresado = input("Ingrese el dia de la semana: (-1 para terminar) ").lower()

totalIngresos = 0
cantDiasIngresados = 0

nombreId333 = ""

while diaIngresado != "-1":
    arch = open("tarifas.txt", "r", encoding= "utf-8")
    linea = arch.readline().strip()
    
    tarifaBase = 0
    tarifaPorMin = 0
    
    cantDiasIngresados += 1
    
    while linea != "":
        partes = linea.split(",")
        diaActual = partes[0].lower()
        tarifaBaseActual = int(partes[1])
        tarifaPorMinActual = int(partes[2])
        
        if diaActual == diaIngresado:
            tarifaBase = tarifaBaseActual
            tarifaPorMin = tarifaPorMinActual
        
        linea = arch.readline().strip()
        
    print(f"Para el dia {diaIngresado} la tarifa base es de ${tarifaBase} y la tarifa por minuto es de ${tarifaPorMin}")
    
    arch = open("alquileres.txt", "r", encoding= "utf-8")
    linea = arch.readline().strip()
    
    mayor = -1
    idMayor = ""
    
    menor = 9999999
    idMenor = ""
    
    totalAlquileres = 0
    cantAlquileres = 0
    
    cant2000 = 0
    
    while linea != "":
        partes = linea.split(",")
        id = partes[0]
        nombre = partes[1]
        duracion = int(partes[2])
        dia = partes[3].lower()
        
        if dia == diaIngresado:
            costoAlquiler = tarifaBase + tarifaPorMin * duracion
            print(f"El cliente {nombre} alquilo con el ID {id} por {duracion} minutos y debe pagar ${costoAlquiler}")
            
            if costoAlquiler > mayor:
                mayor = costoAlquiler
                idMayor = id
            
            if costoAlquiler < menor:
                menor = costoAlquiler
                idMenor = id
            
            totalAlquileres += costoAlquiler
            cantAlquileres += 1
            
            if costoAlquiler < 2000:
                cant2000 += 1
                
            totalIngresos += costoAlquiler
            
            if id == "N333":
                nombreId333 = nombre
        
        linea = arch.readline().strip()
    
    print("---------------------------------------------------------------------------------------")
    print(f"El cliente que alquiló con el ID {idMayor} pagó la mayor cantidad de dinero, que es de ${mayor}")
    print(f"El cliente que alquiló con el ID {idMenor} pagó la menor cantidad de dinero, que es de ${menor}")
    promedioAlquileres = totalAlquileres / cantAlquileres
    print(f"El promedio de los alquileres del dia {diaIngresado} es de ${round(promedioAlquileres,2)}")
    porcentaje2000 = 100 * (cant2000 / cantAlquileres)
    print(f"El porcentaje de alquileres menores a $2000 es de {round(porcentaje2000,2)}%")
    print("---------------------------------------------------------------------------------------")

    diaIngresado = input("Ingrese el dia de la semana: (-1 para terminar) ").lower()
    while diaIngresado != "-1" and diaIngresado != "lunes" and diaIngresado != "martes" and diaIngresado != "miercoles" and diaIngresado != "jueves" and diaIngresado != "viernes" and diaIngresado != "sabado" and diaIngresado != "domingo":
        diaIngresado = input("Ingrese el dia de la semana: (-1 para terminar) ").lower()

if cantDiasIngresados == 0:
    print("No se ingresaron días")
else:
    print("---------------------------------------------------------------------------------------")
    print(f"El total de ingresos de los dias preguntados es de ${totalIngresos}")
    promedioIngresos = totalIngresos / cantDiasIngresados
    print(f"El promedio de los ingresos de los dias preguntados es de ${promedioIngresos}")
    #BONUS
    print(f"Nombre ID N333: {nombreId333}")