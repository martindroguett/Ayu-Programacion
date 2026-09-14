#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 23:08:12 2025

@author: martindroguett
"""

#Archivo Partidas
archP = open("partidas.txt","r",encoding="utf-8")
lineaP = archP.readline().strip()

partidasProcesadas = 0

#Contadores y algoritmos
mayorKills = 0
mayorKillsP = ""

mayorRounds = 0
mayorRoundsP = ""

mayorEquipo = 0
mayorEquipoN = ""

empates = 0

#Ciclo que se encarga de analizar las partidas
while (lineaP != ""):
    partesP = lineaP.split(";")
    
    idPartida = partesP[0]
    equipo1 = partesP[1]
    equipo2 = partesP[2]
    rounds = int(partesP[3])
    
    #CONTADORES:
    kills1 = 0
    kills2 = 0
    
    mejor1 = 0
    mejor2 = 0
    
    #VERIFICANDO EQUIPOS: 
    
    existe1 = False
    existe2 = False #Ambos falsos porque no sabemos si existen
        
        #Archivo Equipos - lo volvemos a abrir cada vez para verificar si existen los equipos
    archE = open("equipos.txt","r",encoding="utf-8")
    lineaE = archE.readline().strip()
    
        #Ciclo que se encarga de analizar los equipos
    while (lineaE != ""):
        if (lineaE == equipo1): #Si lo encontramos si existe
            existe1 = True
        
        if (lineaE == equipo2):
            existe2 = True
            
        lineaE = archE.readline().strip()
            
    if (not existe1): #Si es falso
        print(f"El equipo {equipo1} no existe.")
    
    if (not existe2):
        print(f"El equipo {equipo2} no existe.")
        
    if (existe1 and existe2): #Si ambos existen hacemos el análisis y sumamos partida
        partidasProcesadas += 1
        roundsV = 0
        
        if (rounds > mayorRounds):
            mayorRounds = rounds
            mayorRoundsP = idPartida
        
        #Ciclo que se encarga de analizar los rounds
        for i in range(rounds): 
            roundE1 = int(partesP[4 + 2*i]) #Partimos desde la parte 4, luego la 6, luego la 8...
            roundE2 = int(partesP[4 + 2*i + 1]) #Partimos desde la parte 5, luego la 7, luego la 9...
            
            if (roundE1 < 0 or roundE2 < 0):
                continue #Se salta la ronda. También puede hacerse con un if-else
            
            kills1 += roundE1
            kills2 += roundE2
            
            roundsV += 1
            
            if (roundE1 > mejor1): #Mayores kills
                mejor1 = roundE1
                
            if (roundE2 > mejor2):
                mejor2 = roundE2
                
            if (roundE1 > mayorEquipo):
                mayorEquipo = roundE1
                mayorEquipoN = equipo1
            
            if (roundE2 > mayorEquipo):
                mayorEquipo = roundE2
                mayorEquipoN = equipo2
            
        #ACA YA CALCULAMOS TODAS LAS KILLS
        
        killsTotales = kills1 + kills2
        
        if (killsTotales > mayorKills):
            mayorKills = killsTotales
            mayorKillsP = idPartida
        
        if (kills1 > kills2):
            print(f"El ganador de la partida {idPartida} es {equipo1}")
        
        elif (kills2 > kills1):
            print(f"El ganador de la partida {idPartida} es {equipo2}")
        
        else:
            print(f"Hubo un empate en la partida {idPartida}")
            empates += 1
            
        print(f"La mejor ronda de {equipo1} tuvo {mejor1} kills")
        print(f"La mejor ronda de {equipo2} tuvo {mejor2} kills")
        
        if (roundsV != 0):
            promedioKills = killsTotales / roundsV
            print(f"El promedio de kills de la partida fue de {round(promedioKills,1)} kills por round")
        
        
    print("="*30)
    lineaP = archP.readline().strip()
    
#Acá ya procesamos todas las partidas

print(f"La cantidad de partidas procesadas es de {partidasProcesadas}")
print(f"La partida con más kills fue {mayorKillsP} con {mayorKills} kills")
print(f"La partida con más rounds fue {mayorRoundsP} con {mayorRounds} rounds")
print(f"El equipo que tuvo el mejor round fue {mayorEquipoN} con {mayorEquipo} kills")
print(f"Hubo un total de {empates} empates")

