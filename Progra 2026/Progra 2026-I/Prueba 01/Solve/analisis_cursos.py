
arch = open("cursos.txt","r", encoding= "utf-8")

mayor_promedio = -1
curso_mayor_promedio = ""
codigo_mayor_promedio = ""

menor_promedio = 99999
curso_menor_promedio = ""
codigo_menor_promedio = ""

cantidad_cursos_f = 0

cantidad_cursos_maxima = 0

for i in range(3):
    linea = arch.readline().strip()

while linea != "":
    partes = linea.split(",")
    codigo = partes[0]
    curso = partes[1]
    paralelo = partes[2]
    horario = partes[3]

    partes_horario = horario.split(" ")
    bloque = partes_horario[1].strip()

    linea = arch.readline().strip()
    partes = linea.split(",")
    cant_estudiantes = int(partes[0])

    suma_notas = 0
    for i in range(1, cant_estudiantes * 2 + 1, 2):
        rut = partes[i]
        nota = float(partes[i+1])
        suma_notas += nota
    
    promedio_curso = suma_notas / cant_estudiantes

    if promedio_curso > mayor_promedio:
        mayor_promedio = promedio_curso
        curso_mayor_promedio = curso
        codigo_mayor_promedio = codigo
    
    if promedio_curso < menor_promedio:
        menor_promedio = promedio_curso
        curso_menor_promedio = curso
        codigo_menor_promedio = codigo

    if bloque == "F":
        cantidad_cursos_f += 1
    
    if cant_estudiantes == 20:
        cantidad_cursos_maxima += 1
    print(f"{curso} [{paralelo}] ({codigo}) - Promedio {round(promedio_curso,1)}")

    linea = arch.readline().strip()

print("==== Mayor promedio encontrado ====")
print(f"{curso_mayor_promedio} ({codigo_mayor_promedio}) => {round(mayor_promedio,1)}")
print("==== Menor promedio encontrado ====")
print(f"{curso_menor_promedio} ({codigo_menor_promedio}) => {round(menor_promedio,1)}")
print(f"==== Cantidad de cursos en bloque F: {cantidad_cursos_f} ====")
print(f"==== Cantidad de cursos con capacidad máxima: {cantidad_cursos_maxima} ====")
