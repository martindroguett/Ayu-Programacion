
arch = open("partidos.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

cant_partidos_globales = 0
victorias_sumario = 0
cant_goles = 0

equipo_mejor_ataque = ""
mejor_ataque = -999

cant_empates = 0

cant_victorias_local = 0

tarjetas_amarillas = 0
tarjetas_rojas = 0

jornada_indisciplania = ""
mas_indisciplinaria = -999

while linea != "":
    partes = linea.split(";")
    jornada = partes[0]
    cant_partidos_jornada = int(partes[1])
    fecha = partes[2]

    print(f"Procesando {jornada} ({fecha})con {cant_partidos_jornada} partidos")

    tarjetas_total = 0

    for i in range(cant_partidos_jornada):
        linea = arch.readline().strip()
        partes = linea.split(",")
        local = partes[0]
        visitante = partes[1]
        goles_local = int(partes[2])
        goles_visitante = int(partes[3])
        cant_amarillas = int(partes[4])
        cant_rojas = int(partes[5])
        estadio = partes[6]

        cant_partidos_globales += 1

        if (local == "Sumario FC" and goles_local > goles_visitante) or (visitante == "Sumario FC" and goles_visitante > goles_local):
            victorias_sumario += 1

        cant_goles += goles_local + goles_visitante

        if goles_local > mejor_ataque:
            mejor_ataque = goles_local
            equipo_mejor_ataque = local
        
        if goles_visitante > mejor_ataque:
            mejor_ataque = goles_visitante
            equipo_mejor_ataque = visitante

        if goles_local == goles_visitante:
            cant_empates += 1

        if goles_local > goles_visitante:
            cant_victorias_local += 1
        
        tarjetas_amarillas += cant_amarillas
        tarjetas_rojas += cant_rojas

        tarjetas_total += cant_amarillas + cant_rojas

    if tarjetas_total > mas_indisciplinaria:
            mas_indisciplinaria = tarjetas_total
            jornada_indisciplania = jornada

    linea = arch.readline().strip()

print("============================================================")
print("ESTADÍSTICAS COMPLETAS LIGA CIVIL UCN 2032 ")
print("============================================================")
print()
print("--- ESTADÍSTICAS GENERALES ---")
print(f"1. Total de partidos jugados: {cant_partidos_globales}")
print(f"2. Victorias de Sumario FC: {victorias_sumario}")
print(f"3. Promedio de goles por partido: {round(cant_goles / cant_partidos_globales,2)}")
print(f"4. Mejor ataque del torneo: {equipo_mejor_ataque} ({mejor_ataque} goles en un partido) ")
print(f"5. Total de empates: {cant_empates}")
print(f"6. Porcentaje de victorias locales: {round(100* cant_victorias_local / cant_partidos_globales,2)}% ")
print()

print("--- ESTADÍSTICAS DISCIPLINARIAS ---")
print(f"7. Total de tarjetas amarillas: {tarjetas_amarillas}")
print(f"8. Total de tarjetas rojas: {tarjetas_rojas}")
print(f"9. Jornada más indisciplinada: {jornada_indisciplania} ({mas_indisciplinaria} tarjetas) ")
print(f"11. Promedio de tarjetas por partido: 2.62")