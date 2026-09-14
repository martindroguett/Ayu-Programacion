#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 23:57:44 2025

@author: martindroguett
"""

arch = open("oleur.txt","r",encoding="utf-8") #Abrimos el archivo
linea = arch.readline().strip() #Leemos la línea

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Recorreremos esto para descifrar el mensaje

#Ciclo para analizar la línea
while (linea != ""):
    mensaje = linea
    
    linea = arch.readline().strip() #Leemos la pista
    
    pista = linea
    
    test = "" #El mensaje que estaremos probando
    
    while (test == ""): #Una vez cambie oficialmente, dejamos de buscar
    
    
        for i in range(26): #Tenemos 26 posibles claves
            
            #Recorremos el mensaje letra por letra
            for j in mensaje:
                
                if (j == " "): #Si es un espacio nos lo saltamos solamente
                    test += " "
                    continue
                
                posicion = 0 #Buscamos la posicion de la letra del mensaje en el abc
                
                for k in abc:
                    
                    if (j == k):
                        break; #Si encontramos la coincidencia terminamos el ciclo
                    
                    posicion += 1 #De lo contrario avanzamos de posición
                
                #Ahora entonces agregamos a test la letra en la posición {posicion - i}
                
                posicionFinal = posicion - i
                
                if (posicionFinal < 0):
                    posicionFinal += 26 #Si es -1, la letra deberia original deberia ser z
                    
                posicionActual = 0 #Partimos desde el inicio
                for l in abc:
                
                    if (posicionFinal == posicionActual):
                        test += l #Agregamos la letra cuando encontramos la coincidencia
                        break #Y salimos del ciclo
                        
                    posicionActual += 1
                
            if (pista in test): #Si la pista esta en la frase que encontramos
                print(test)
                print(f"La clave de desplazamiento de esta línea fue {i}")
                break #Salimos del ciclo while
            else:
                test = "" #Si no, probamos otra vez
                
    linea = arch.readline().strip() #Pasamos a la siguiente línea
                
                
        
        