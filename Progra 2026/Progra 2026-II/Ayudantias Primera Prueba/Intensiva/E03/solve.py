#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:55:42 2026

@author: martindroguett
"""

arch = open("curso.txt","r",encoding="utf-8")

linea = arch.readline().strip()

partes = linea.split(";")

print(f"{partes[0]} | {partes[1]}")

linea = arch.readline().strip()

#Cálculos globales

mejorNota = 0
mejorNotaNombre = ""

mejorNota2 = 0
mejorNota2Nombre = ""

aprobados = 0
alumnos = 0

masControlesRojos = 0
masControlesRojosNombre = "" 

controlMasBajo = 8
controlMasBajoNombre = ""

while(linea != ""):
    
    partes = linea.split(";")
    
    rut = partes[1]
    nombre = partes[2]

    alumnos += 1
    
    NC = 0
    NP = 0

    sumaControles = 0
    cantidadControles = 0
    
    linea = arch.readline().strip()
    partes = linea.split(";")
    
    tipo = partes[0]

    menorControl = 8

    controlesRojos = 0
    
    while (tipo != "A" and tipo != ""):

        nota = partes[1]

        if (partes[1] == "NSP"):
            nota = 1
                        
        else: 
            nota = float(partes[1])

        if (tipo == "C"):

            if (nota < controlMasBajo and partes[1] != "NSP"):
                controlMasBajo = nota
                controlMasBajoNombre = nombre

            if (nota < menorControl):
                menorControl = nota

            sumaControles += nota
            cantidadControles += 1

            if (nota < 4):
                controlesRojos += 1

        if (tipo == "P"):
            if (NP == 0):
                NP += nota * 0.45
            else:
                NP += nota * 0.55
        
        linea = arch.readline().strip()
        partes = linea.split(";")
        tipo = partes[0]

    if (cantidadControles > 1):
        NC = (sumaControles - menorControl)/(cantidadControles - 1)
    else:
        NC = sumaControles

    notaFinal = NP * 0.7 + NC * 0.3

    if (notaFinal > mejorNota):
        mejorNota2 = mejorNota
        mejorNota2Nombre = mejorNotaNombre

        mejorNota = notaFinal
        mejorNotaNombre = nombre

    elif (notaFinal > mejorNota2):
        mejorNota2 = notaFinal
        mejorNota2Nombre = nombre

    if (NC < 4 or NP < 3.3):
        estado = "Reprobado"
    elif (NP < 4):
        estado = "Recalificación"
    else:
        estado = "Aprobado"

    if (estado == "Aprobado"):
        aprobados += 1

    if (controlesRojos > masControlesRojos):
        masControlesRojos = controlesRojos
        masControlesRojosNombre = nombre


    print("Alumno:",nombre)
    print("Nota controles:", NC)
    print("Nota pruebas:", NP)
    print("Nota Final:", notaFinal)
    print("Estado:", estado)

    print("="*20)

print("Mejores notas:")
print(f"1. {mejorNotaNombre} con nota {mejorNota}")
print(f"2. {mejorNota2Nombre} con nota {mejorNota2}")

print("-"*30)

print(f"Porcentaje de aprobados: {aprobados * 100 /alumnos}%")

print("-"*30)

print(f"{masControlesRojosNombre} tiene más controles rojos con {masControlesRojos} controles")

print("-"*30)

print(f"{controlMasBajoNombre} tiene el control más bajo de todos con nota {controlMasBajo}")

        
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        