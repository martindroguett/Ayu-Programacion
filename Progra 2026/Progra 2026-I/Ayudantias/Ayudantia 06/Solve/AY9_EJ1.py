# 1. Función para verificar el largo
def verificar_largo(password):
    if len(password) >= 10:
        return True
    else:
        return False

# 2. Función para contar caracteres especiales
def contener_especiales(password):
    especiales = "*_!@#"
    contador = 0
    for caracter in password:
        if caracter in especiales:
            contador = contador + 1
    return contador

# 3. Función para verificar si tiene números (sin usar isdigit)
def tiene_numeros(password):
    numeros = "0123456789"
    for caracter in password:
        if caracter in numeros:
            return True
    return False

# 4. Función CEREBRO: Une todas las anteriores
def analizar_fortaleza(password):
    puntaje = 0
    
    # Sumar puntos por largo
    if verificar_largo(password):
        puntaje = puntaje + 2
        
    # Sumar puntos por especiales (máximo 3)
    puntos_especiales = contener_especiales(password)
    if puntos_especiales > 3:
        puntos_especiales = 3
    puntaje = puntaje + puntos_especiales
    
    # Sumar puntos por números
    if tiene_numeros(password):
        puntaje = puntaje + 1
        
    return puntaje

# --- PROGRAMA PRINCIPAL ---
print("--- BIENVENIDO AL EVALUADOR DE MICROSOFT UCN ---")

puntaje_final = 0

# El ciclo se repite si el puntaje es de "Seguridad Baja" (0 a 2)
while puntaje_final <= 2:
    pass_usuario = input("\nIngrese su contraseña para analizar: ")
    puntaje_final = analizar_fortaleza(pass_usuario)
    
    if puntaje_final <= 2:
        print(f"Puntaje: {puntaje_final}")
        print("Veredicto: Seguridad Baja: No cumple los estándares. Intente de nuevo.")
    elif puntaje_final <= 4:
        print(f"Puntaje: {puntaje_final}")
        print("Veredicto: Seguridad Media: Aceptable pero mejorable.")
    else:
        print(f"Puntaje: {puntaje_final}")
        print("Veredicto: Seguridad Alta: Contraseña robusta.")

print("\nGracias por usar nuestro sistema de seguridad.")