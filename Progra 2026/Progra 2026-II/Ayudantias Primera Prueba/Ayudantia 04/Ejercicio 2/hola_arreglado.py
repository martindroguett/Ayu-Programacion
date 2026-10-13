# hola_arreglado.py - solucion pauta Ejercicio 2 (Ayudantia 4)
# Errores corregidos del hola.py original:
# 1. range(1, 5) -> range(1, 6): faltaba la tienda5
# 2. readline() sin strip -> se agrega .strip() en nombre y lineas
# 3. precio quedaba como string -> se convierte con int()
# 4. plataforma = codigo completo -> se separa por "-" con get_plataforma()
# 5. == "web" en minuscula -> es "WEB" en mayusculas
# 6. == "gta V" con mal case -> es "GTA V"
# 7. acumuladores por tienda fuera del for -> se mueven dentro del for
# 8. gan_tienda =+ precio -> debe ser gan_tienda += precio (acumular)
# 9. print por tienda sin f -> se arma con mostrar_resumen() que imprime por dentro
# Punto 3: logica repetida (parsear venta, resumen por tienda, mejor juego)
# se convierte en funciones con def y return.


def get_plataforma(codigo):
    partes = codigo.split("-")
    plataforma = partes[0]
    return plataforma


def mostrar_resumen(nombre, ventas, web, local, ganancia):
    print(f"{nombre} | Ventas: {ventas} (WEB: {web}, LOCAL: {local}) | Ganancia: ${ganancia}")


def get_mejor_juego(gan_gta5, gan_gta6, gan_rdr2, gan_sa):
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
    return mejor_juego


def get_mayor_ganancia(juego, gan_gta5, gan_gta6, gan_rdr2, gan_sa):
    if juego == "GTA VI":
        return gan_gta6
    elif juego == "Red Dead Redemption 2":
        return gan_rdr2
    elif juego == "GTA San Andreas":
        return gan_sa
    else:
        return gan_gta5


def mostrar_venta_top(juego, precio, tienda, fecha, codigo):
    print(f"Venta más cara: {juego} a ${precio} en {tienda} el {fecha} ({codigo})")


def mostrar_resumen_general(mejor_juego, mejor_gan, ventas_web, gan_web, ventas_local, gan_local):
    print()
    print("=== RESUMEN GENERAL ===")
    print(f"Juego que generó más ganancia: {mejor_juego} (${mejor_gan})")
    print(f"WEB -> {ventas_web} ventas | ${gan_web}")
    print(f"LOCAL -> {ventas_local} ventas | ${gan_local}")


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

venta_mayor = 0
venta_mayor_juego = ""
venta_mayor_tienda = ""
venta_mayor_fecha = ""
venta_mayor_codigo = ""

for i in range(1, 6):
    arch = open(f"tienda{i}.txt", "r", encoding="utf-8")
    nombre_tienda = arch.readline().strip()
    linea = arch.readline().strip()

    ventas_tienda = 0
    gan_tienda = 0
    web_tienda = 0
    local_tienda = 0

    while linea != "":
        partes = linea.split(",")
        juego = partes[0]
        fecha = partes[1]
        precio = int(partes[2])
        codigo = partes[3]

        plataforma = get_plataforma(codigo)

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

        if precio > venta_mayor:
            venta_mayor = precio
            venta_mayor_juego = juego
            venta_mayor_tienda = nombre_tienda
            venta_mayor_fecha = fecha
            venta_mayor_codigo = codigo

        linea = arch.readline().strip()

    arch.close()
    mostrar_resumen(nombre_tienda, ventas_tienda, web_tienda, local_tienda, gan_tienda)

mejor_juego = get_mejor_juego(gan_gta5, gan_gta6, gan_rdr2, gan_sa)
mejor_gan = get_mayor_ganancia(mejor_juego, gan_gta5, gan_gta6, gan_rdr2, gan_sa)

mostrar_resumen_general(mejor_juego, mejor_gan, ventas_web, gan_web, ventas_local, gan_local)
mostrar_venta_top(venta_mayor_juego, venta_mayor, venta_mayor_tienda, venta_mayor_fecha, venta_mayor_codigo)
