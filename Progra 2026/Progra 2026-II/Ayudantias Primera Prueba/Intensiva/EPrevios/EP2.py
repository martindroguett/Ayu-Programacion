mayor = -1
nombreMayor = ""

menor=99999
nombreMenor=""

for i in range(5):
    
    persona = input("Ingrese los datos de la persona: ")
    partes = persona.split(" ")
    
    nombre = partes[0]
    
    edad = int(partes[1])
    
    
    if (edad > mayor):
        mayor = edad
        nombreMayor = nombre
        
    if (edad<menor):
        menor=edad
        nombreMenor=nombre