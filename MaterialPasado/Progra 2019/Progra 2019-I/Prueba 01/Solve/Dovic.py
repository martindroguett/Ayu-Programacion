
arch = open("payroll.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

cantTrabajadores = 0

mayorSueldoG = -1
nombreMayorSueldoG = ""

mayorSueldoV = -1
nombreMayorSueldoV = ""

menorUtilidadS = 9999999
nombreMenorUtilidadS = ""

mayorUtilidadS = -1
nombreMayorUtilidadS = ""

cantBajas = 0
cantBajasConP = 0

cantMujeresG = 0
cantG = 0

while linea != "":
    partes = linea.split("-")
    cuidad = partes[0]
    ventas = int(partes[1])
    cantEmpleados = int(partes[2])
    prioridad = partes[3]
    
    sumSueldo = 0
    
    #Pregunta 2
    cantTrabajadores += cantEmpleados
    
    for _ in range(cantEmpleados):
        linea = arch.readline().strip()
        partes = linea.split(";")
        nombre = partes[0]
        sexo = partes[1].lower()
        sueldo = int(partes[2])
        edad = int(partes[3])
        cargo = partes[4].lower()
        
        if cargo == "gerente":
            #Pregunta 3.1
            if sueldo > mayorSueldoG:
                mayorSueldoG = sueldo
                nombreMayorSueldoG = nombre
                
            #Pregunta 6
            if sexo == "f":
                cantMujeresG += 1
            cantG += 1
        
        #Pregunta 3.2
        if cargo == "vendedor" and sueldo > mayorSueldoV:
            mayorSueldoV = sueldo
            nombreMayorSueldoV = nombre
            
        sumSueldo += sueldo
    
    #Pregunta 1
    utilidad = ventas - 1.1 * sumSueldo
    
    if utilidad <= 0:
        print(f"{cuidad} ({prioridad}) Perdidas. Se recomienda cerrar")
    else:
        print(f"{cuidad} ({prioridad}) Utilidades. Se recomienda mantener")
        
    #Pregunta 4.1
    if utilidad < menorUtilidadS:
        menorUtilidadS = utilidad
        nombreMenorUtilidadS = cuidad
    
    #Pregunta 4.2
    if utilidad > mayorUtilidadS:
        mayorUtilidadS = utilidad
        nombreMayorUtilidadS = cuidad
    
    #Pregunta 5
    if prioridad.lower() == "baja":
        cantBajas += 1
    if prioridad.lower() == "baja" and utilidad <= 0:
        cantBajasConP += 1
            
    linea = arch.readline().strip()

print(f"2) El total de trabajadores es {cantTrabajadores}")
print(f"3.1) El Gerente con sueldo más alto es {nombreMayorSueldoG} con {mayorSueldoG}")
print(f"3.2) El Vendedor con el sueldo más alto es {nombreMayorSueldoV} con {mayorSueldoV}")
print(f"4.1) La sucursal con menor utilidad es {nombreMenorUtilidadS} con {menorUtilidadS}")
print(f"4.2) La sucursal con mayor utilidad es {nombreMayorUtilidadS} con {mayorUtilidadS}")
porcentajeBajasConP = 100 * (cantBajasConP / cantBajas)
print(f"5) El porcentaje de sucursales de prioridad baja con problemas es de un {porcentajeBajasConP}%")
porcentajeMujeresG = 100 * (cantMujeresG / cantG)
print(f"6) El porcentaje de gerentes mujeres es de {porcentajeMujeresG}%")