# Materia: Listas
# Ejercicio 1: Farmacia Turno de Invierno


# ------------------------------------------------------------
# Verifica si un código pertenece al rango válido de un grupo.
# Retorna 1 si es válido, 0 si no lo es.
# ------------------------------------------------------------
def es_codigo_valido(grupo, codigo):
    valido = 0

    if grupo == "analgesico":
        if codigo >= 100 and codigo <= 199:
            valido = 1

    elif grupo == "antibiotico":
        if codigo >= 200 and codigo <= 299:
            valido = 1

    elif grupo == "vitamina":
        if codigo >= 300 and codigo <= 399:
            valido = 1

    return valido


# ------------------------------------------------------------
# Determina el grupo al que pertenece un código.
# ------------------------------------------------------------
def obtener_grupo(codigo):
    grupo = "invalido"

    if codigo >= 100 and codigo <= 199:
        grupo = "analgesico"

    elif codigo >= 200 and codigo <= 299:
        grupo = "antibiotico"

    elif codigo >= 300 and codigo <= 399:
        grupo = "vitamina"

    return grupo


# ------------------------------------------------------------
# Busca un código dentro de una lista.
# Retorna la posición si lo encuentra.
# Retorna -1 si no lo encuentra.
# ------------------------------------------------------------
def buscar_codigo(lista, codigo):
    posicion = -1

    for i in range(len(lista)):
        if lista[i] == codigo:
            posicion = i
            return posicion

    return posicion


# ------------------------------------------------------------
# Retira un código desde una lista usando pop.
# Retorna 1 si pudo retirarlo.
# Retorna 0 si no estaba disponible.
# ------------------------------------------------------------
def retirar_codigo(lista, codigo):
    retirado = 0

    posicion = buscar_codigo(lista, codigo)

    if posicion != -1:
        lista.pop(posicion)
        retirado = 1

    return retirado


# ------------------------------------------------------------
# Lee el inventario y separa los medicamentos válidos
# en tres listas: analgésicos, antibióticos y vitaminas.
# ------------------------------------------------------------
def leer_inventario(nombre_archivo):
    analgesicos = []
    antibioticos = []
    vitaminas = []

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    grupo_actual = ""

    linea = archivo.readline().strip()

    while linea != "":
        partes = linea.split(",")

        # Si la línea tiene 3 partes, es un encabezado:
        # grupo,minimo,maximo
        if len(partes) == 3:
            grupo_actual = partes[0]

        # Si no es encabezado, entonces es un código.
        else:
            codigo = int(linea)

            if es_codigo_valido(grupo_actual, codigo) == 1:

                if grupo_actual == "analgesico":
                    analgesicos.append(codigo)

                elif grupo_actual == "antibiotico":
                    antibioticos.append(codigo)

                elif grupo_actual == "vitamina":
                    vitaminas.append(codigo)

        linea = archivo.readline().strip()

    archivo.close()

    return analgesicos, antibioticos, vitaminas


# ------------------------------------------------------------
# Lee una receta y guarda todos sus códigos en una lista.
# ------------------------------------------------------------
def leer_receta(nombre_archivo):
    receta = []

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    linea = archivo.readline().strip()

    while linea != "":
        codigo = int(linea)
        receta.append(codigo)

        linea = archivo.readline().strip()

    archivo.close()

    return receta


# ------------------------------------------------------------
# Valida si el nombre de receta existe.
# Retorna 1 si es válido.
# Retorna 0 si no es válido.
# ------------------------------------------------------------
def receta_valida(nombre_receta):
    valida = 0

    if nombre_receta == "receta_1":
        valida = 1

    elif nombre_receta == "receta_2":
        valida = 1

    elif nombre_receta == "receta_3":
        valida = 1

    return valida


# ------------------------------------------------------------
# Asocia el nombre lógico de la receta con su archivo .txt.
# ------------------------------------------------------------
def obtener_archivo_receta(nombre_receta):
    archivo = ""

    if nombre_receta == "receta_1":
        archivo = "receta_1.txt"

    elif nombre_receta == "receta_2":
        archivo = "receta_2.txt"

    elif nombre_receta == "receta_3":
        archivo = "receta_3.txt"

    return archivo


# ------------------------------------------------------------
# Revisa una receta completa.
#
# Crea tres listas:
# entregados: medicamentos que sí estaban disponibles.
# no_disponibles: códigos válidos que no estaban en inventario.
# invalidos: códigos que no pertenecen a ningún grupo.
# ------------------------------------------------------------
def revisar_receta(receta, analgesicos, antibioticos, vitaminas):
    entregados = []
    no_disponibles = []
    invalidos = []

    for i in range(len(receta)):
        codigo = receta[i]
        grupo = obtener_grupo(codigo)

        if grupo == "invalido":
            invalidos.append(codigo)

        elif grupo == "analgesico":
            retirado = retirar_codigo(analgesicos, codigo)

            if retirado == 1:
                entregados.append(codigo)
            else:
                no_disponibles.append(codigo)

        elif grupo == "antibiotico":
            retirado = retirar_codigo(antibioticos, codigo)

            if retirado == 1:
                entregados.append(codigo)
            else:
                no_disponibles.append(codigo)

        elif grupo == "vitamina":
            retirado = retirar_codigo(vitaminas, codigo)

            if retirado == 1:
                entregados.append(codigo)
            else:
                no_disponibles.append(codigo)

    return entregados, no_disponibles, invalidos


# ------------------------------------------------------------
# Determina el grupo con mayor cantidad de medicamentos entregados.
# ------------------------------------------------------------
def determinar_grupo_mas_entregado(entregados):
    cont_analgesico = 0
    cont_antibiotico = 0
    cont_vitamina = 0

    for i in range(len(entregados)):
        codigo = entregados[i]
        grupo = obtener_grupo(codigo)

        if grupo == "analgesico":
            cont_analgesico = cont_analgesico + 1

        elif grupo == "antibiotico":
            cont_antibiotico = cont_antibiotico + 1

        elif grupo == "vitamina":
            cont_vitamina = cont_vitamina + 1

    mayor = cont_analgesico
    grupo_mayor = "analgesico"
    empate = 0

    if cont_antibiotico > mayor:
        mayor = cont_antibiotico
        grupo_mayor = "antibiotico"
        empate = 0

    elif cont_antibiotico == mayor and mayor > 0:
        empate = 1

    if cont_vitamina > mayor:
        mayor = cont_vitamina
        grupo_mayor = "vitamina"
        empate = 0

    elif cont_vitamina == mayor and mayor > 0:
        empate = 1

    if mayor == 0:
        grupo_mayor = "ninguno"

    elif empate == 1:
        grupo_mayor = "empate"

    return grupo_mayor


# ------------------------------------------------------------
# Muestra el resultado final de la revisión de una receta.
# ------------------------------------------------------------
def mostrar_resultado(receta, entregados, no_disponibles, invalidos):
    medicamentos_solicitados = len(receta)
    codigos_validos = len(receta) - len(invalidos)
    medicamentos_entregados = len(entregados)
    medicamentos_no_disponibles = len(no_disponibles)
    codigos_invalidos = len(invalidos)

    grupo_mas_entregado = determinar_grupo_mas_entregado(entregados)

    print()
    print("Medicamentos solicitados:", medicamentos_solicitados)
    print("Códigos válidos solicitados:", codigos_validos)
    print("Medicamentos entregados:", medicamentos_entregados)
    print("Medicamentos no disponibles:", medicamentos_no_disponibles)
    print("Códigos inválidos:", codigos_invalidos)

    print()
    print("Lista de entregados:", entregados)
    print("Lista de no disponibles:", no_disponibles)
    print("Lista de inválidos:", invalidos)

    print()
    print("Grupo más entregado:", grupo_mas_entregado)

    if medicamentos_no_disponibles == 0:
        print("Estado: Receta completa")
    else:
        print("Estado: Receta incompleta")


# ------------------------------------------------------------
# Pregunta si el usuario desea revisar otra receta.
# Solo acepta si o no.
# ------------------------------------------------------------
def preguntar_continuar():
    opcion = input("¿Desea revisar otra receta? (Si - No): ").lower()

    while opcion != "si" and opcion != "no":
        print("Opción inválida")
        opcion = input("¿Desea revisar otra receta? (Si - No): ").lower()

    return opcion


# ------------------------------------------------------------
# Programa principal.
# ------------------------------------------------------------
def main():
    analgesicos, antibioticos, vitaminas = leer_inventario("inventario.txt")

    print("Bienvenido al sistema de Farmacia Turno de Invierno")
    print()

    continuar = "si"
    

    while continuar == "si":
        nombre_receta = input("Ingrese receta a revisar: ").lower()

        while receta_valida(nombre_receta) == 0:
            print("Opción inválida")
            print()
            nombre_receta = input("Ingrese receta a revisar: ").lower()

        archivo_receta = obtener_archivo_receta(nombre_receta)

        receta = leer_receta(archivo_receta)

        entregados, no_disponibles, invalidos = revisar_receta(
            receta,
            analgesicos,
            antibioticos,
            vitaminas
        )

        mostrar_resultado(
            receta,
            entregados,
            no_disponibles,
            invalidos
        )
        # Se imprime una línea en blanco para ordenar visualmente la salida.
        
        print()
        
        continuar = preguntar_continuar()
        
        # Se imprime una línea en blanco para ordenar visualmente la salida.
        
        print()

    print("Sistema finalizado")


main()