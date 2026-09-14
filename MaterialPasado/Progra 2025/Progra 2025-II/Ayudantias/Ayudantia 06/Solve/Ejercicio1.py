# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 17:41:55 2025

@author: frome
"""
listaNombre1=[]
listaNombre2=[]
listaRachas=[]

def lecturaArchivo(listaNombre1,listaNombre2,listaRachas):
    archivo = open("rachas.txt","r",encoding="utf-8")
    linea = archivo.readline()
    while linea!="":
        partes=linea.split(",")
        nombre1=partes[0]
        nombre2=partes[1]
        racha=int(partes[2])
        listaNombre1.append(nombre1)
        listaNombre2.append(nombre2)
        listaRachas.append(racha)
        
        linea = archivo.readline()
        
        
lecturaArchivo(listaNombre1,listaNombre2,listaRachas)

#Para ejercicio 1)
mayorRacha=-1
mayorNombre1=""
mayorNombre2=""

#Para ejercicio 2)
menorRacha=9999999
menorNombre1=""
menorNombre2=""

#Para ejercicio 3)
sumaRachas=0
cantidadRachas=0
for i in range(len(listaRachas)):
    #Para ejercicio 1)
    if mayorRacha < listaRachas[i]:
        mayorRacha=listaRachas[i]
        mayorNombre1=listaNombre1[i]
        mayorNombre2=listaNombre2[i]
        
    #Para ejercicio 2)
    if menorRacha > listaRachas[i]:
        menorRacha=listaRachas[i]
        menorNombre1=listaNombre1[i]
        menorNombre2=listaNombre2[i]
        
    #Para ejercicio 3)
    sumaRachas+=listaRachas[i]
    cantidadRachas+=1
        

print(f"1)La pareja con la mayor racha es {mayorNombre1} y {mayorNombre2} con {mayorRacha} días de racha.")
print(f"2)La pareja con la menor racha es {menorNombre1} y {menorNombre2} con {menorRacha} días de racha.")
promedioRachas = round(sumaRachas/cantidadRachas,1)
print(f"3)Número promedio de días de racha: {promedioRachas}")

#Para ejercicio 4)
print("4)Rachas sanas:")
for i in range(len(listaRachas)):
    if promedioRachas > listaRachas[i]:
        print(f"->{listaNombre1[i]} y {listaNombre2[i]} con {listaRachas[i]} días de racha")
        