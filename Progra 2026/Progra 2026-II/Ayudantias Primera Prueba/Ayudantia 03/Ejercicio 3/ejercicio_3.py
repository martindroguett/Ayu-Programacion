# EJERCICIO 3
print("=== Sistema de Control de Tiendas Rockstar Games ===")
print()

gan_gta5 = 0
gan_gta6 = 0
gan_rdr2 = 0
gan_sa = 0

ventas_web = 0
ventas_local = 0
gan_web = 0
gan_local = 0

venta_cara = 0
venta_cara_juego = ""
venta_cara_tienda = ""
venta_cara_fecha = ""
venta_cara_codigo = ""
#For para poder abrir los 5 archivos, que nos indican
for i in range(1, 6):
    arch = open(f"tienda{i}.txt", "r", encoding="utf-8")
    nombre_tienda = arch.readline().strip()
    linea = arch.readline().strip()

    ventas_tienda = 0
    gan_tienda = 0
    web_tienda = 0
    local_tienda = 0
    #While para recorrar las lineas de cada archivo
    while linea != "":
        partes = linea.split(",")
        juego = partes[0]
        fecha = partes[1]
        precio = int(partes[2])
        codigo = partes[3]

        codigo_partes = codigo.split("-")
        plataforma = codigo_partes[0]

        ventas_tienda += 1
        gan_tienda += precio

        if plataforma == "WEB":
            web_tienda += 1
            ventas_web += 1
            gan_web += precio
        else:
            local_tienda += 1
            ventas_local += 1
            gan_local += precio

        if juego == "GTA V":
            gan_gta5 += precio
            
        elif juego == "GTA VI":
            gan_gta6 += precio
            
        elif juego == "Red Dead Redemption 2":
            gan_rdr2 += precio
            
        elif juego == "GTA San Andreas":
            gan_sa += precio

        if precio > venta_cara:
            venta_cara = precio
            venta_cara_juego = juego
            venta_cara_tienda = nombre_tienda
            venta_cara_fecha = fecha
            venta_cara_codigo = codigo

        linea = arch.readline().strip()

    arch.close()
    print(f"{nombre_tienda} | Ventas: {ventas_tienda} (WEB: {web_tienda}, LOCAL: {local_tienda}) | Ganancia: ${gan_tienda}")
    #Se imprime el resumen de la tienda , termina el while y regresa al for.
    # para seguir con la otra tienda. 
print()
print("=== RESUMEN GENERAL ===")

mejor_juego = "GTA V"
mejor_gan = gan_gta5
if gan_gta6 > mejor_gan:
    mejor_juego = "GTA VI"
    mejor_gan = gan_gta6
    
if gan_rdr2 > mejor_gan:
    mejor_juego = "Red Dead Redemption 2"
    mejor_gan = gan_rdr2
    
if gan_sa > mejor_gan:
    mejor_juego = "GTA San Andreas"
    mejor_gan = gan_sa

print(f"Juego que generó más ganancia: {mejor_juego} (${mejor_gan})")
print(f"WEB -> {ventas_web} ventas | ${gan_web}")
print(f"LOCAL -> {ventas_local} ventas | ${gan_local}")
print(f"Venta más cara: {venta_cara_juego} a ${venta_cara} en {venta_cara_tienda} el {venta_cara_fecha} ({venta_cara_codigo})")
