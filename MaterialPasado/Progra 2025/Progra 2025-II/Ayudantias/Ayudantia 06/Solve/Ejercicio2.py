# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 16:54:25 2025

@author: frome
"""

#baseDatosAlumnos.txt
#nombre_alumno,paralelo,carrera,promedioNotas
listaNombres=[]
listaParalelos=[]
listaCarreras=[]
listaPromedios=[]
opcion=2
def lecturaArchivos():
    archivo = open("baseDatosAlumnos.txt","r",encoding="utf-8")
    linea = archivo.readline()
    while linea!="" :
        partes=linea.split(",")
        nombre=partes[0]
        paralelo=partes[1]
        carrera=partes[2]
        promedio=float(partes[3])
        listaNombres.append(nombre)
        listaParalelos.append(paralelo)
        listaCarreras.append(carrera)
        listaPromedios.append(promedio)
        
        linea=archivo.readline()
        
def printMenu():
    print("--------------")
    print("1)Buscar alumno")
    print("2)Mostrar todos los alumnos")
    print("3)Mostrar alumnos ICCI")
    print("4)Informe")
    print("5)Eliminar alumno de sistema")
    print("6)SALIR")

def buscarAlumno(nombre):
    for i in range(len(listaNombres)):
        if(listaNombres[i].lower()==nombre):
            print(listaNombres[i],listaParalelos[i],listaCarreras[i],listaPromedios[i])
            break

def printAlumnos():
    for i in range(len(listaNombres)):
        print(listaNombres[i],listaParalelos[i],listaCarreras[i],listaPromedios[i])
      
def printICCI():
    for i in range(len(listaCarreras)):
        if(listaCarreras[i]=="ICCI"):
            print(listaNombres[i],listaParalelos[i],listaCarreras[i],listaPromedios[i])
            
def informeAlumnos():
    print("¡Informe de alumnos!")
    
    #SELECCION DE LA PEOR NOTA
    print("-Peor nota: ")
    menorNota=9999
    nombreEstudiante=""
    
    #CONTAR ALUMNOS POR CARRERA
    iccis=0
    itis=0
    icis=0
    
    #PORCENTAJE DE APROBACION: CANTIDAD DE APROBADOS / CANTIDAD DE ALUMNOS
    azules=0
    
    #PROMEDIO TOTAL = SUMATORIA DE TODAS LAS NOTAS / CANTIDAD DE ALUMNOs
    sumaNotas=0
    
    for i in range(len(listaCarreras)): #POR CADA ALUMNO
        #SELECCION DE LA PEOR NOTA
        if(listaPromedios[i]<menorNota):
            menorNota=listaPromedios[i]
            nombreEstudiante=listaNombres[i]
            
        #CONTAR ALUMNOS POR CARRERA    
        if listaCarreras[i]=="ICCI" :
            iccis+=1
        elif listaCarreras[i]=="ITI":
            itis+=1
        elif listaCarreras[i]=="ICI":
            icis+=1
            
        #PORCENTAJE DE APROBACION: CANTIDAD DE APROBADOS / CANTIDAD DE ALUMNOS
        if(listaPromedios[i]>=4):
            azules+=1
            
        #PROMEDIO TOTAL = SUMATORIA DE TODAS LAS NOTAS / CANTIDAD DE ALUMNOs  
        sumaNotas+=listaPromedios[i]
        
        
    print(f"{nombreEstudiante} con un promedio {menorNota}")
    
    
    print("-Cantidad de estudiantes por carrera:")
    print("ICCI: ",iccis)
    print("ITI: ",itis)
    print("ICI: ",icis)
    
    totalAlumnos = iccis+itis+icis    
    porcentajeAprobacion = round((azules/totalAlumnos)*100,1)
    print(f"Porcentaje de aprobación: {porcentajeAprobacion}%")
    
    promedioTotal = round(sumaNotas/totalAlumnos,1)
    print(f"El promedio de notas de la asignatura es {promedioTotal}")
    
def eliminarAlumno(nombre):
    for i in range(len(listaNombres)):
        if(listaNombres[i]==nombre):
            listaNombres.pop(i)
            listaCarreras.pop(i)
            listaParalelos.pop(i)
            listaPromedios.pop(i)
            break
    
lecturaArchivos()

opcion=0
while(opcion!=6):
    printMenu()
    opcion = int(input("Ingrese una opción:"))
    if(opcion==1):
        nombre = input("Ingrese nombre del alumno a buscar: ")
        buscarAlumno(nombre.lower())
    elif(opcion==2):
        printAlumnos()
    elif(opcion==3):
        printICCI()
    elif(opcion==4):
        informeAlumnos()
    elif(opcion==5):
        nombre = input("Ingrese nombre del alumno a eliminar: ")
        eliminarAlumno(nombre)
    elif(opcion==6):
        print("Saliendo...")
    else:
        print("Elija opcion válida")
        