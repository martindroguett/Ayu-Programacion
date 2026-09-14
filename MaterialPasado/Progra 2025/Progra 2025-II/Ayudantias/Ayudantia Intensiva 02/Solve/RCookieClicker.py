#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 11:38:37 2025

@author: martindroguett
"""

arch = open("config.txt","r",encoding="utf-8")
linea = arch.readline().strip()

cantMax = int(linea)

linea = arch.readline().strip()
precioGalleta = int(linea)

artefactos = []

linea = arch.readline().strip()

while (linea != ""):
    artefactos.append(linea)
    
    linea = arch.readline().strip()
    
#============================================================   

def calculoGPP(l):
    gpp = 1
    
    for i in l:
        partes = i.split(",")     
        g = int(partes[2])
        
        gpp += g
        
    return gpp
      
def calculoCT(l):
    ct = 0
    
    for i in l:
        partes = i.split(",")     
        c = int(partes[3])
        
        ct += c
        
    return ct
    
   
accion = "_"    

galletas = 0
monedas = 0
gpp = 1
costeTotal = 0

misArtefactos = []

while (accion != "FIN"):
    print(f"Galletas: {galletas} | Monedas: {monedas} | Galletas por pulsación: {gpp} | Coste total: {costeTotal}")
    print("1. Vender galletas")
    print("2. Ver artefactos")
    print("3. Comprar artefactos")
    print("4. Vender artefactos")
    accion = input("> ").upper().strip()
    print()
    
    if (accion == "1"):
        venta = int(input("¿Cuantas galletas deseas vender?: "))
        
        if (venta > galletas):
            print("No se pueden vender más galletas de las que tienes!")
        
        else:
            galletas -= venta
            monedas += venta * precioGalleta
            
        print()
    
    if (accion == "2"):
        print("--- Tus artefactos ---")

        for i in misArtefactos:
            partes = i.split(",")
            
            nombre = partes[0]
            precio = int(partes[1])
            g = int(partes[2])
            cpp = int(partes[3])
            
            cpg = cpp/g
            
            print(f"{nombre} | Precio: {precio} | Galletas/Pulsación: {g} | Coste: {cpp} | Coste/Galleta: {cpg}")
            print()
            
    if (accion == "3"):
        print("--- Comprar artefactos ---")
        count = 1
        
        for i in artefactos:
            partes = i.split(",")
            
            nombre = partes[0]
            precio = int(partes[1])
            g = int(partes[2])
            cpp = int(partes[3])
            
            print(f"{count}. {nombre} | Precio: {precio} | Galletas/Pulsación: {g} | Coste: {cpp}")
            count += 1
        
        print()
        print(f"Monedas disponibles: {monedas}")
        print(f"Espacio dispobile: {cantMax - len(misArtefactos)}")
        
        print()
        
        if (cantMax - len(misArtefactos) > 0):
            venta = int(input("Ingrese el número del artefacto: "))
            
            index = venta - 1
            artefacto = artefactos[index]
            
            partes = artefacto.split(",")
            
            nombre = partes[0]
            precio = int(partes[1])
            
            if (precio > monedas):
                print("No te alcanza")
            else:
                misArtefactos.append(artefacto)
                print(f"Compraste {nombre}")
                monedas -= precio
            
        else: 
            print("No tienes espacio suficiente")
            
        print()    

    if (accion == "4"):
        print("--- Vender artefacto ---")
        print("--- Tus artefactos ---")

        count = 1
        for i in misArtefactos:
            partes = i.split(",")
            
            nombre = partes[0]
            precio = int(partes[1])

            print(f"{count}. {nombre} | Precio compra: {precio}")
            print()
        
        venta = int(input("Ingrese el artefacto que quieres vender: "))
        
        index = venta - 1
        
        artefacto = misArtefactos[index]
        
        partes = artefacto.split(",")
        nombre = partes[0]
        precio = int(partes[1])
        
        misArtefactos.pop(index)
        
        monedas += int(precio*0.9)
        
        print(f"Vendiste {nombre} por {int(precio*0.9)} monedas!")
        
        print()

    if (accion == ""):
        if (costeTotal > monedas):
            print("No puedes generar!")
        
        else:
            galletas += gpp
            monedas -= costeTotal
    
    gpp = calculoGPP(misArtefactos)
    costeTotal = calculoCT(misArtefactos)
    
    
    

    