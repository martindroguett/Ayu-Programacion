#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 10:26:44 2025

@author: martindroguett
"""
import numpy as np
import random as r

def crearMapa():
    mapa = np.zeros([10,10])
    mapa[0][0] = 1
    
    for i in range(16):
        f = r.randint(0,9)
        c = r.randint(0,9)
        
        while (f == 0 and c == 0):
            f = r.randint(0,9)
            c = r.randint(0,9)
        
        mapa[f][c] = 2
        
    for i in range(11):
        f = r.randint(0,9)
        c = r.randint(0,9)
        
        while (mapa[f][c] != 0):
            f = r.randint(0,9)
            c = r.randint(0,9)
        
        mapa[f][c] = 3
        
    return mapa

def verMapa(mx):
    for f in range(mx.shape[0]):
        
        for c in range(mx.shape[1]):
            if (mx[f][c] == 0):
                print("_", end = " ")
            
            if (mx[f][c] == 1):
                print("X", end = " ")
            
            if (mx[f][c] == 2):
                print("O", end = " ")
            
            if (mx[f][c] == 3):
                print("*", end = " ")
                
        print()

def contar(mx):
    count = 0
    
    for f in range(mx.shape[0]):
        for c in range(mx.shape[1]):
            if(mx[f][c] == 2):
                count += 1
                
    return count
         
mx = crearMapa()

verMapa(mx)

fX = 0
cX = 0

vivo = True

while (2 in mx and vivo):
    mov = input("Ingrese secuencia de movs: ").upper()
    
    for i in mov:
        mx[fX][cX] = 0
        
        if (i == "U"):
            if (fX - 1 >= 0):
                fX -= 1
            else:
                print("El movimiento es inválido")
            
        if (i == "D"):
            if (fX + 1 < mx.shape[0]):
                fX += 1
            else:
                print("El movimiento es inválido")
            
        if (i == "R"):
            if (cX + 1 < mx.shape[1]):
                cX += 1
            else:
                print("El movimiento es inválido")
            
        if (i == "L"):
            if (cX - 1 >= 0):
                cX -= 1
            else:
                print("El movimiento es inválido")
        
        if (mx[fX][cX] == 3):
            vivo = False
            mx[fX][cX] = 1
            break
        
        mx[fX][cX] = 1
         
    verMapa(mx)
    print(f"Monedas restantes: {contar(mx)}")
    print()

if (vivo):
    print("Ganaste")
    
else:
    print("Moriste")
            
    