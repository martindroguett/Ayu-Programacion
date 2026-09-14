#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 10:55:20 2025

@author: martindroguett
"""
def convertir(p):
    lista = []
    
    for i in p:
        lista.append(i)
    
    return lista

palabra = input("Ingrese palabra secreta: ").upper()

listaP = convertir(palabra)

intento = ""

count = 6

while (intento != palabra and count != 0):
    intento = input("Ingrese intento: ").upper()
    aux = convertir(palabra)
    
    listaI = convertir(intento)
    
    resultado = []
    
    for i in range(len(listaI)):
        
        if (listaI[i] in aux):
            if (listaI[i] == listaP[i]):
                resultado.append("V")
            else: 
                resultado.append("A")
                
            aux.remove(listaI[i])
            
        else:
            resultado.append("G")
            
    print(resultado)
    print(listaI)
    print()
    count -= 1
            
if (intento == palabra):
    print("Ganaste")
    
else: 
    print("Perdiste")
            
    
