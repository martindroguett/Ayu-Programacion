#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 23:48:07 2025

@author: martindroguett
"""

import numpy as np

boeing = np.zeros([36,6])
airbus = np.zeros([36,6])

corridasAirbus = [0]*36
corridasBoeing = [0]*36

posiciones = ["A","B","C","D","E","F"]

def buscarAgregar(lista, elemento):
    
    if (elemento not in lista):
        lista.append(elemento)
        
    return lista.index(elemento)

def agregar(f, c, costo, nave):
    if (nave == "Airbus A321"):
        airbus[f][c] += 1
        
        corridasAirbus[f] += costo
        
    else: 
        boeing[f][c] += 1
        
        corridasBoeing[f] += costo
  
def usos(nave, mx):
    ventana = 0
    centro = 0
    pasillo = 0 
    
    for f in range(36):
        for c in range(6):
            if (posiciones[c] == "A" or posiciones[c] == "F"):
                ventana += int(mx[f][c])
                
            elif (posiciones[c] == "B" or posiciones[c] == "E"):
                centro += int(mx[f][c])
            
            else:
                pasillo += int(mx[f][c])
                
    print(f"--- {nave} ---")
    print(f"Ventana: {ventana}")
    print(f"Centro: {centro}")
    print(f"Pasillo: {pasillo}")
    
def mayor(l1,l2):
    airbus = 0
    for i in l1:
        airbus += i
        
    boeing = 0
    for i in l2:
        boeing += i
        
    if (airbus > boeing):
        print(f"2) El Airbus generó mayores ingresos con ${airbus}")
    elif (boeing > airbus):
        print(f"2) El Boeing generó mayores ingresos con ${boeing}")
    else:
        print(f"Ambos generaron los mismos ingresos: ${boeing}")
            
def noOcupados(nave, mx):
    print(f"-{nave}:",end=" ")
    
    for f in range(36):
        for c in range(6):
            if (mx[f][c] == 0):
                print(f"{f + 1}{posiciones[c]}", end = " ")
    print()
    
def menosIngresos(nave, l):
    menor = 10**10
    corrida = 0
    
    for i in range(len(l)):
        if (l[i] < menor):
            menor = l[i]
            corrida = i + 1
            
    print(f"--- {nave} ---")
    print(f"La corrida que menos ingresos generó: {corrida}")

arch = open("pasajes.txt","r",encoding="utf-8")
linea = arch.readline().strip()

while (linea != ""):
    partes = linea.split(",")
    
    asiento = partes[0].split(" ")
    
    corrida = int(asiento[0])
    pos = asiento[1]
    
    costo = int(partes[1])
    
    nave = partes[2]
    
    f = corrida - 1
    c = buscarAgregar(posiciones, pos)
    
    agregar(f,c,costo,nave)
    
    linea = arch.readline().strip()
    
print("1) Uso según ubicación: ")
usos("Airbus A321", airbus)
usos("Boeing 737", boeing)

mayor(corridasAirbus,corridasBoeing)

print("3) Asientos no ocupados: ")
noOcupados("Airbus A321", airbus)
noOcupados("Boeing 737", boeing)

print("4) Corrida con menos ingresos generados: ")
menosIngresos("Airbus A321", corridasAirbus)
menosIngresos("Boeing 737", corridasBoeing)
