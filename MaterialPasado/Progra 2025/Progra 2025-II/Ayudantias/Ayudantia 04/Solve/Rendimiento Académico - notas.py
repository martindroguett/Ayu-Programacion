archivo = open("notas.txt", "r", encoding="utf-8")

# Leer primera línea: nombre de asignatura y cantidad de paralelos
linea = archivo.readline().strip()
partes = linea.split(",")
asignatura = partes[0]
cantidad_paralelos = int(partes[1])

print("Asignatura:", asignatura)
print()

# Acumuladores generales
total_alumnos = 0
total_aprobados = 0
suma_notas = 0.0

# Para identificar el mejor paralelo
mejor_promedio = -1
docente_mejor = ""

# Leer paralelos
for i in range(cantidad_paralelos):      
    # Línea con paralelo, docente, cantidad alumnos
    linea = archivo.readline().strip()
    partes = linea.split(",")
    paralelo = partes[0]
    docente = partes[1].strip()
    cantidad_alumnos = int(partes[2])

    # Línea con notas
    linea = archivo.readline().strip()
    partes = linea.split(",")
    
    aprobados = 0
    suma_paralelo = 0.0
    
    for j in range(cantidad_alumnos):
        nota = float(partes[j])
        suma_paralelo = suma_paralelo + nota
        if nota >= 4.0:
            aprobados = aprobados + 1


    # Calcular tasa de aprobación de este paralelo
    tasa_aprob_paralelo = round(aprobados * 100.0 / cantidad_alumnos,2)
    promedio_paralelo = round(suma_paralelo / cantidad_alumnos,1)
    print(f'{paralelo} | {docente} | Tasa aprobación: {tasa_aprob_paralelo}% | Promedio: {promedio_paralelo}')

    # Acumular en asignatura
    total_alumnos = total_alumnos + cantidad_alumnos
    total_aprobados = total_aprobados + aprobados
    suma_notas = suma_notas + suma_paralelo

    # Revisar si este paralelo es el mejor promedio
    if promedio_paralelo > mejor_promedio:
        mejor_promedio = promedio_paralelo
        docente_mejor = docente

archivo.close()

# Resultados finales
tasa_aprob_asignatura = total_aprobados * 100.0 / total_alumnos
promedio_asignatura = suma_notas / total_alumnos

print()
print("Tasa de aprobación total de la asignatura:", round(tasa_aprob_asignatura, 2), "%")
print("Promedio general de la asignatura:", round(promedio_asignatura, 1))
print("Profesor con mejor promedio:", docente_mejor)
