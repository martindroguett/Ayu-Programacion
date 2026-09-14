# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 12:52:54 2025

@author: frome
"""
#1
A=[]
A.append(3)
A.append(5)
A.append(7)
A.append(9)
A.append(11)
for i in range(len(A)):
    print(A[i])

#2
B=[]
for i in range(1,51):
    B.append(i)
for i in range(0,50):
    if(B[i]%2!=0):
        print(B[i])

#2A
C=[]
for i in range(len(B)):
    if(B[i]%3==0):
        C.append(B[i])

#2B
suma=0
contador=0
for i in range(len(C)):
    suma+=C[i]
    contador+=1 
promedio=suma/contador

#2C
for i in range(len(C)):
    C.pop()

#3
arr=[1,2,3,4,5]
for i in range(len(arr)-1,0,-1):
    print(arr[i])
    
#4
nombres = ["Ana", "Luis", "Pedro", "María", "Juan", "Sofía"]
name = input("Ingrese un nombre: ")
for i in range(len(nombres)):
    if(nombres[i]==name):
        print("El nombre SI está en la lista!")
        break

# o también ...
#for n in nombres: 
#   if n==name:
#       print("El nombre SI esta en la lista")
#       break

#5
F=[]    
for i in range(9,63,2):
    F.append(i)
#5A
for i in range(len(F)):
    if F[i]%3==0:
        F[i]=0
#5B
for i in range(len(F)):
    if F[i]==0:
        F[i+2]="WOW"
print(F)
#5C
for i in range(len(F)):
    if F[i]=="WOW":
        F[i-2]="MISH"
print(F)
#5D
for i in range(len(F)):
    if F[i]!="WOW" and F[i]!="MISH" and F[i]=="ERROR": #ESTO DA ERROR
        F[i+3]="ERROR"
print(F)


#SOLUCION A 5D: AGREGAR and i+3<len(F)-1.  
#al avanzar 3 casillas se llega a una posición fuera de la lista, ->index out of range.
#al agregar i+3<len(F)-1 al if evita que se haga el "salto" incorrte, o más bien, que se intente cambiar el valor de una casilla que está fuera del rango de la lista.
#Solo podrá hacerlo mientras el "salto" te mantenga dentro de la lista.
for i in range(len(F)):
    if F[i]!="WOW" and F[i]!="MISH" and F[i]=="ERROR" and i+3<len(F)-1:
        F[i+3]="ERROR"
print(F)