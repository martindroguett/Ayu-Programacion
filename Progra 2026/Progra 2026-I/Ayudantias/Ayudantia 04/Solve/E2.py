archivo = open("f1.txt","r",encoding="utf-8")
linea = archivo.readline().strip()

#2.
mejorRedbull = ""
mejorPTJRedbull = 0
mejorMcLaren = ""
mejorPTJMcLaren = 0

#3.
mejorPromedio = 0
mejorCorredor = ""

#4.
mejorPTJ2019 = 0
mejor2019 = ""

#5.
peorPTJEspaña = 999
peorEspaña = ""

#6. 
cont2019 = 0
cont2020 = 0
cont2022 = 0
cont2023 = 0
total_carreras = 0
while linea != "":
    partes1 = linea.split(",")
    
    corredor=partes1[0]
    pais=partes1[1]
    carreras = int(partes1[2])
    
    total_carreras += carreras
    
    #1. puntaje promedio jugador
    sumaPuntajes = 0
    
    for i in range(carreras):
        linea = archivo.readline().strip()
        partes2 = linea.split(",")
        
        año = int(partes2[0])
        circuito = partes2[1]
        equipo = partes2[2]
        posicion = int(partes2[3])
        puntaje = int(partes2[4])
        
        #1.	Sumar puntaje de cada carrera para despues promediar
        sumaPuntajes += puntaje
        
        #2. Mejor carrera equipo
        if equipo == "Red Bull" and puntaje > mejorPTJRedbull:
            mejorPTJRedbull = puntaje
            mejorRedbull = linea
        elif equipo == "McLaren" and puntaje > mejorPTJMcLaren:
            mejorPTJMcLaren = puntaje
            mejorMcLaren = linea
        
        #4. Mejor carrera 2019
        if año == 2019 and puntaje > mejorPTJ2019:
            mejorPTJ2019 = puntaje
            mejor2019 = linea
        
        #5. Peor carrera de españa
        if pais == "España" and puntaje < peorPTJEspaña:
            peorPTJEspaña = puntaje
            peorEspaña = linea
            
        #6. porcentaje carreras 2019, 2020, 2022, 2023.
        if año == 2019:
            cont2019+=1
        elif año == 2020:
            cont2020+=1
        elif año == 2022:
            cont2022+=1
        elif año == 2023:
            cont2023+=1
            
    #1. Promedio corredor
    promedioCorredor = sumaPuntajes/carreras
    print(f"Promedio de {corredor} -> {round(promedioCorredor,2)}")
    
    #3. Corredor mejor promedio
    if promedioCorredor > mejorPromedio:
        mejorPromedio = promedioCorredor
        mejorCorredor = corredor
     
    linea = archivo.readline().strip()


print(f"""
2.	La mejor carrera de Redbull y McLaren:
    Red Bull -> {mejorRedbull} 
    Mc Laren -> {mejorMcLaren}
3.	El corredor con el mejor puntaje promedio:
    {mejorCorredor} -> {round(mejorPromedio,2)} puntaje
4.	La mejor carrera del año 2019:
    {mejor2019} 
5.	La peor carrera de España
    {peorEspaña}
6.	El porcentaje de carreras hechas en cada año:
    2019 -> {round(cont2019/total_carreras,2)*100}%
    2020 -> {round(cont2020/total_carreras,2)*100}%
    2022 -> {round(cont2022/total_carreras,2)*100}%
    2023 -> {round(cont2023/total_carreras,2)*100}%
      """)
