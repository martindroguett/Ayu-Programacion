#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 09:47:36 2025

@author: martindroguett
"""

arch = open("parentesis.txt","r",encoding="utf-8")

linea = arch.readline().strip()

while (linea != ""):
    partes = linea.split(" ")
    
    esValido = True
    
    apertura = []
    
    for i in partes:
        
        if (i == "(" or i == "{" or i == "["):
            apertura.append(i)
            
        if (i == ")"):
            if (len(apertura) != 0 and apertura[-1] != "("):
                esValido = False
            elif (len(apertura) != 0):
                apertura.pop(-1)
            else:
                esValido = False
            
                
        if (i == "}"):
            if (len(apertura) != 0 and apertura[-1] != "{"):
                esValido = False
            elif (len(apertura) != 0):
                apertura.pop(-1)
            else:
                esValido = False
                
        if (i == "]"):
            if (len(apertura) != 0 and apertura[-1] != "["):
                esValido = False
            elif (len(apertura) != 0):
                apertura.pop(-1)
            else:
                esValido = False
            
    if (esValido):
        print(f"{linea} -> es Válido")
        
    else:
        print(f"{linea} -> no es Válido")
            
    linea = arch.readline().strip()