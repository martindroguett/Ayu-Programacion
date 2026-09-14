# Variables globales para comparar
mayor_descanso = 0
funcionario_descanso = ""
mayor_trabajo = 0
funcionario_mas_horas = ""
menor_trabajo = 0
funcionario_menos_horas = ""

# --- Abrir funcionarios.txt ---
archivo_func = open("funcionarios.txt", "r", encoding="utf-8")
linea_func = archivo_func.readline().strip()

while linea_func != "":
    linea_func = linea_func.strip()
    if linea_func != "":
        partes_func = linea_func.split(",")
        if len(partes_func) >= 2:
            id_func = partes_func[0].strip()
            nombre_func = partes_func[1].strip()

            # Variables del funcionario actual
            contador_eventos = 0
            entrada = ""
            salida_colacion = ""
            regreso_colacion = ""
            salida_turno = ""
            hora_prev = -999  # Para verificar duplicados

            # --- Abrir registro.txt para este funcionario ---
            archivo_reg = open("registro.txt", "r", encoding="utf-8")
            linea_reg = archivo_reg.readline()

            while linea_reg != "":
                linea_reg = linea_reg.strip()
                if linea_reg != "":
                    partes_reg = linea_reg.split(";")
                    if len(partes_reg) >= 3:
                        fecha = partes_reg[0].strip()
                        hora = partes_reg[1].strip()
                        id_reg = partes_reg[2].strip()

                        # Solo procesar si es el mismo funcionario
                        if id_reg == id_func:
                            # Convertir hora a segundos usando split
                            partes_hora = hora.split(":")
                            h_seg = int(partes_hora[0])*3600 + int(partes_hora[1])*60 + int(partes_hora[2])

                            # Verificar duplicado: ignorar si diferencia < 30 s
                            if h_seg - hora_prev >= 30:
                                contador_eventos = contador_eventos + 1
                                hora_prev = h_seg  # actualizar última hora válida

                                if contador_eventos == 1:
                                    entrada = hora
                                elif contador_eventos == 2:
                                    salida_colacion = hora
                                elif contador_eventos == 3:
                                    regreso_colacion = hora
                                elif contador_eventos == 4:
                                    salida_turno = hora
                linea_reg = archivo_reg.readline()
            archivo_reg.close()

            # Verificar cantidad de registros
            if contador_eventos < 4:
                print(f'{nombre_func} | ADVERTENCIA: tiene sólo {contador_eventos} registros' )
            else:
                # Convertir horas a segundos usando split
                partes = entrada.split(":")
                h1 = int(partes[0])*3600 + int(partes[1])*60 + int(partes[2])                
                partes = salida_colacion.split(":")
                h2 = int(partes[0])*3600 + int(partes[1])*60 + int(partes[2])                
                partes = regreso_colacion.split(":")
                h3 = int(partes[0])*3600 + int(partes[1])*60 + int(partes[2])                
                partes = salida_turno.split(":")
                h4 = int(partes[0])*3600 + int(partes[1])*60 + int(partes[2])
                
                # Calcular horas trabajadas y descanso
                jornada = (h2 - h1) + (h4 - h3)
                descanso = h3 - h2

                print(nombre_func, "| Horas trabajadas:", round(jornada/3600,2))

                # Comparar con los máximos/mínimos globales
                if descanso > mayor_descanso:
                    mayor_descanso = descanso
                    funcionario_descanso = nombre_func
                if jornada > mayor_trabajo:
                    mayor_trabajo = jornada
                    funcionario_mas_horas = nombre_func
                    
                if funcionario_menos_horas == '':
                    menor_trabajo = jornada
                    funcionario_menos_horas = nombre_func
                elif jornada < menor_trabajo:
                    menor_trabajo = jornada
                    funcionario_menos_horas = nombre_func

    linea_func = archivo_func.readline().strip()
archivo_func.close()

# --- Reporte global ---
print("\n=== RESUMEN FINAL ===")
print("Funcionario con descanso más largo:", funcionario_descanso)
print("Funcionario que trabajó más horas:", funcionario_mas_horas)
print("Funcionario que trabajó menos horas:", funcionario_menos_horas)
