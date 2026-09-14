
añoIngresado = int(input("Ingrese un año específico (2022 a 2024): "))
while añoIngresado < 2022 or añoIngresado > 2024:
    añoIngresado = int(input("Ingrese un año específico (2022 a 2024): "))
    
arch = open("resultados.txt","r", encoding= "utf-8")
linea = arch.readline().strip()

duracionTotal = 0
cantPartidas = 0

puntajeTotal = 0

mayorPuntaje = 0
nombreMayorPuntaje = ""

segundoMayorPuntaje = 0
nombreSegundoMayorPuntaje = ""

ultimoJugador = ""

cantPartidas2022 = 0
cantPartidas2023 = 0
cantPartidas2024 = 0

cantPartidasAñoIngresado = 0

while linea != "":
    partes = linea.split(";")
    
    partesJugador = partes[0].split(",")
    nombre = partesJugador[0]
    puntaje = int(partesJugador[1])
    
    partesDatos = partes[1].split(",")
    año = int(partesDatos[0])
    duracion = int(partesDatos[1])
    
    #Pregunta 1
    puntajeTotal += puntaje
    duracionTotal += duracion
    cantPartidas += 1

    #Pregunta 2
    if puntaje > mayorPuntaje:
        segundoMayorPuntaje = mayorPuntaje
        nombreSegundoMayorPuntaje = nombreMayorPuntaje
        mayorPuntaje = puntaje
        nombreMayorPuntaje = nombre
    if puntaje < mayorPuntaje and puntaje > segundoMayorPuntaje:
        segundoMayorPuntaje = puntaje
        nombreSegundoMayorPuntaje = nombre
    
    #Pregunta 4
    if año == añoIngresado:
        ultimoJugador = nombre
        cantPartidasAñoIngresado += 1
    
    #Pregunta 5
    if año == 2022:
        cantPartidas2022 += 1
    elif año == 2023:
        cantPartidas2023 += 1
    else:
        cantPartidas2024 += 1
    
    linea = arch.readline().strip()


promedioPuntaje = puntajeTotal / cantPartidas
print(f"- Puntaje promedio: {promedioPuntaje}")
promedioDuracion = duracionTotal / cantPartidas
print(f"- Duración promedio: {round(promedioDuracion,1)}")
print(f"- Jugador con mayor puntaje: {nombreMayorPuntaje} con {mayorPuntaje} puntos")
print(f"- Jugador con segundo mayor puntaje: {nombreSegundoMayorPuntaje} con {segundoMayorPuntaje} puntos")

if añoIngresado % 2 == 0:
    if cantPartidasAñoIngresado > 0:
        print(f"- Último jugador del año {añoIngresado}: {ultimoJugador}")
    else:
        print(f"- No hay registros del año {añoIngresado}")

añoMayorCant = 0
if cantPartidas2022 > cantPartidas2023 and cantPartidas2022 > cantPartidas2024:
    añoMayorCant = 2022
elif cantPartidas2023 > cantPartidas2022 and cantPartidas2023 > cantPartidas2024:
    añoMayorCant = 2023
else:
    añoMayorCant = 2024
print(f"- Año con mayor cantidad de partidas: {añoMayorCant}")

