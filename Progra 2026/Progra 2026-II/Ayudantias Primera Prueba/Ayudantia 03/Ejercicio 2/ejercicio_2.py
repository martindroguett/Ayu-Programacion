# EJERCICIO 2 
print("=== Bienvenido a la Calculadora de Terremotos ===")
print("¡Felices Fiestas Patrias!")
print()

arch = open("terremotos.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

total_17 = 0
total_18 = 0
total_19 = 0

total_javier = 0
total_catalina = 0
total_martin = 0
total_sofia = 0

record = 0
record_nombre = ""
record_fecha = ""
record_lugar = ""

while linea != "":
    partes = linea.split(",")
    fecha = partes[0]
    cantidad = int(partes[1])
    nombre = partes[2]
    lugar = partes[3]
    #Se usa denuevo el .split ya que debo separar dia y mes
    fecha_partes = fecha.split("-")
    dia = int(fecha_partes[0])
    mes = int(fecha_partes[1])
    #mes septiembre
    if mes == 9:
        if dia == 17:
            total_17 += cantidad
        elif dia == 18:
            total_18 += cantidad
        elif dia == 19:
            total_19 += cantidad

    if nombre == "Javier":
        total_javier += cantidad
        
    elif nombre == "Catalina":
        total_catalina += cantidad
        
    elif nombre == "Martin":
        total_martin += cantidad
        
    elif nombre == "Sofia":
        total_sofia += cantidad

    if cantidad > record:
        record = cantidad
        record_nombre = nombre
        record_fecha = fecha
        record_lugar = lugar

    linea = arch.readline().strip()

arch.close()

print(f"Terremotos el 17 de septiembre: {total_17}")
print(f"Terremotos el 18 de septiembre: {total_18}")
print(f"Terremotos el 19 de septiembre: {total_19}")

if total_17 > total_18 and total_17 > total_19:
    print("El día más terremotero es el 17 de septiembre")
elif total_18 > total_19:
    print("El día más terremotero es el 18 de septiembre")
else:
    print("El día más terremotero es el 19 de septiembre")

print()
print(f"Récord en un día: {record_nombre} se tomó {record} terremotos el {record_fecha} en {record_lugar}")

campeon = "Javier"
max_total = total_javier
if total_catalina > max_total:
    campeon = "Catalina"
    max_total = total_catalina
    
if total_martin > max_total:
    campeon = "Martin"
    max_total = total_martin
    
if total_sofia > max_total:
    campeon = "Sofia"
    max_total = total_sofia

print(f"Campeón del terremoto: {campeon} con {max_total} terremotos en total")
