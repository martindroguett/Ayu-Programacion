# 1. Función para verificar si un RUT es autorizado
# Retorna 1 si lo encuentra, 0 si no lo encuentra
def es_autorizado(rut_a_buscar):
    archivo_alumnos = open("alumnos.txt", "r")
    encontrado = 0 # Usamos un número como bandera (centinela)
    
    linea = archivo_alumnos.readline().strip()
    while linea != "":
        rut_oficial = linea
        if rut_oficial == rut_a_buscar:
            encontrado = 1
        
        linea = archivo_alumnos.readline().strip()
            
    archivo_alumnos.close()
    return encontrado

# 2. Función para calcular los costos de intrusos
def calcular_costo_intrusos():
    archivo_consumo = open("consumo.txt", "r")
    minutos_intrusos = 0
    
    linea = archivo_consumo.readline().strip()
    while linea != "":
        # Separamos los datos de la línea
        datos = linea.split(",")
        rut_actual = datos[0]
        minutos_actuales = int(datos[1])
        
        # Llamamos a la función anterior y revisamos si retornó 0
        autorizado = es_autorizado(rut_actual)
        
        if autorizado == 0:
            print("Alerta: El RUT", rut_actual, "no está autorizado.")
            minutos_intrusos = minutos_intrusos + minutos_actuales
            
        linea = archivo_consumo.readline().strip()
        
    archivo_consumo.close()
    
    # Calculamos el costo total
    total_dinero = minutos_intrusos * 0.5
    return total_dinero

# --- PROGRAMA PRINCIPAL ---
print("--- INICIANDO AUDITORÍA MICROSOFT-UCN ---")

resultado_final = calcular_costo_intrusos()

print("---------------------------------------")
print("El costo total de los accesos ilegales es:")
print("$", resultado_final, "USD")
print("---------------------------------------")