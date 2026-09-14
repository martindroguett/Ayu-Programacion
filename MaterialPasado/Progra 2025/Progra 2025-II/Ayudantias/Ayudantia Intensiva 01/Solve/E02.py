#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 00:26:11 2025

@author: martindroguett
"""

presupuesto = int(input("Ingrese su presupuesto: "))

while (presupuesto < 1000): #Control de error
    print("El ingreso inicial debe ser mayor o igual a $1000")
    presupuesto = int(input("Ingrese su presupuesto: "))

linea = input("Ingrese el destino (Fin para terminar): ").upper()

aux = ""

#Contadores y algoritmos
mayor = 0
mayorN1 = ""
mayorN2 = ""

menor = 10**10
menorN1 = ""
menorN2 = ""

viajes = 0
gastoFinal = 0

while (linea != "FIN" and presupuesto >= 1000): #Cuando se cumplen ambas podemos trabajar
    
    if (";" in linea): #Consideración del separador (OPCIONAL)
        partes = linea.split(";") #Separamos el string
        
        ciudad = partes[0]
        dias = int(partes[1])
        costoDiario = int(partes[2])
        
        if (ciudad in aux): #Consideración de la ciudad (OPCIONAL)
            print("La ciudad ya fue visitada")
            
        else: #Si llegamos acá significa que todo está bien
        
            costoTotal = dias * costoDiario
            
            if (presupuesto - costoTotal >= 0): #Si alcanza el presupuesto
                presupuesto -= costoTotal
                
                print(f"{ciudad}: ${costoTotal}")
                
                aux += ciudad #Para verificar si existe o no
                aux += " "
                
                viajes += 1
                gastoFinal += costoTotal
                
                if (costoTotal > mayor): #Mayor
                    mayor = costoTotal
                    mayorN1 = ciudad
                    
                elif (costoTotal == mayor): #Si hay empate
                    mayorN2 = ciudad
                    
                if (costoTotal < menor): #Menor
                    menor = costoTotal
                    menorN1 = ciudad
                    
                elif (costoTotal == menor): #Si hay empate
                    menorN2 = ciudad
                
            else:
                print("El viaje sería muy caro!")
        
    else:
        print("La línea no es válida")
    
    if (presupuesto >= 1000):
        print(f"Presupuesto disponible: {presupuesto}")
        linea = input("Ingrese el destino (Fin para terminar): ").upper()
    
print()
print(f"La ciudad más cara es {mayorN1} con un coste de ${mayor}")

if (mayorN2 != ""):
    print(f"{mayorN2} también costó lo mismo!")

print(f"La ciudad más barata es {menorN1} con un coste de ${menor}")

if (menorN2 != ""):
    print(f"{menorN2} también costó lo mismo!")
    
promedio = gastoFinal / viajes

print(f"El promedio de costo por viaje es de ${round(promedio,1)}")

print(f"El presupuesto restante es de ${presupuesto}")