from pathlib import Path
archivo = open("playlist.txt","r",encoding="utf-8")
linea = archivo.readline().strip()
#ID,Cancion,Álbum,Minutos.Segundos,Rating,Año-Mes-Día,CantidadvecesEscuchada
total_canciones = 0
#B.
mayorduracion = 0
cancionlarga = ""
#C.
mayorescuchas = 0
cancion_popular = ""
#D.
sumaRating = 0
contador_populares = 0
#E.
escuchasLosTres = 0
contadorLosTres = 0
sumaRatingLosTres = 0
#F.
cancion_antigua = ""
mayoraño=9999
mayormes=13
mayordia=32
while linea != "":
    
    total_canciones += 1
    
    partes = linea.split(",")
    cancion = partes[1]
    album = partes[2]
    tiempo = partes[3]
    rating = int(partes[4])
    fecha = partes[5]
    escuchas = int(partes[6])
    
    #B. Cancion más larga
    #Como tiempo tiene el formato "minuto.segundos" -> SPLIT
    partes_tiempo = tiempo.split(".")
    minutos = int(partes_tiempo[0])
    segundos = int(partes_tiempo[1])
    duracion = minutos*60 + segundos  #duracion en segundos de cancion
    
    if duracion > mayorduracion:
        mayorduracion=duracion
        cancionlarga=cancion
        
    #C. Canción más escuchada
    if escuchas > mayorescuchas:
        mayorescuchas=escuchas
        cancion_popular=cancion
        
    #D. Rating promedio de canciones escuchadas más de 80 veces
    if escuchas > 80:
        sumaRating += rating
        contador_populares += 1
        
    #E. cantidad de veces que se escuchó alguna canción del álbum 
    #chileno “Los Tres” y el rating promedio de esas canciones.
    if album == "Los Tres":
        escuchasLosTres += escuchas
        contadorLosTres += 1
        sumaRatingLosTres += rating
    
    #F. La canción más antigua.
    #Como fecha tiene el formato: "año-mes-dia" -> SPLIT("-")
    partes_fecha = fecha.split("-")
    año = int(partes_fecha[0])
    mes = int(partes_fecha[1])
    dia = int(partes_fecha[2])
    
    if año == mayoraño: #si están en el mismo año, se verifica si está el mismo mes o antes.
        if mes == mayormes:
            if dia < mayordia:
                cancion_antigua = cancion
                mayoraño=año
                mayormes=mes
                mayordia=dia
        elif mes < mayormes:
            cancion_antigua = cancion
            mayoraño=año
            mayormes=mes
            mayordia=dia
    elif año < mayoraño: # si está en un año anterior, es automaticamente más antigua
        cancion_antigua = cancion
        mayoraño=año
        mayormes=mes
        mayordia=dia
    
    linea = archivo.readline().strip()

print(f"""-------Estadísticas-------
a)  Cantidad de canciones en la playlist: {total_canciones}
b)	Canción de mayor duración: {cancionlarga} -> {mayorduracion} segundos.
c)	Canción más escuchada: {cancion_popular} -> {mayorescuchas} veces.
d)	Rating promedio de las canciones más escuchadas: {round(sumaRating/contador_populares,2)}
e)	Cantidad de veces que se escuchó alguna canción del álbum chileno “Los Tres” y el rating promedio de esas canciones.
    ESCUCHAS TOTALES: {escuchasLosTres}
    PROMEDIO RATING: {sumaRatingLosTres/contadorLosTres} 
f)	La canción más antigua: {cancion_antigua}: {mayoraño}-{mayormes}-{mayordia}
      """)
    