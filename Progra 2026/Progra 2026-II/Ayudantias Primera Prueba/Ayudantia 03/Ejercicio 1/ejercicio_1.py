# EJERCICIO 1
print("=== Bienvenido al Ranking Anime ===")
#Forma de abrir el archivo .txt
arch = open("calificaciones.txt", "r", encoding="utf-8")
#Lee la primer linea del TXT
linea = arch.readline().strip()

suma_snk = 0
cant_snk = 0
suma_hxh = 0
cant_hxh = 0
suma_bc = 0
cant_bc = 0
suma_dn = 0
cant_dn = 0

nota_min = 999
usuario_min = ""
anime_min = ""
#Se usa el linea !="": para que cuando se acaben las lineas del archivo termine el while
while linea != "":
    #Se separa la linea en parte dividiendola por la , 
    partes = linea.split(",")
    anime = partes[0]
    nota = float(partes[1])
    usuario = partes[2]
    #Se usa el [n] para indicar la pocision del dato de la linea
    if anime == "Shingeki no Kyojin":
        suma_snk += nota
        cant_snk += 1
    
    elif anime == "Hunter x Hunter":
        suma_hxh += nota
        cant_hxh += 1
        
    elif anime == "Black Clover":
        suma_bc += nota
        cant_bc += 1
        
    elif anime == "Death Note":
        suma_dn += nota
        cant_dn += 1

    if nota < nota_min:
        nota_min = nota
        usuario_min = usuario
        anime_min = anime

    linea = arch.readline().strip()
#Cerrar el archivo
arch.close()

prom_snk = suma_snk / cant_snk
prom_hxh = suma_hxh / cant_hxh
prom_bc = suma_bc / cant_bc
prom_dn = suma_dn / cant_dn

print(f"Shingeki no Kyojin -> {cant_snk} calificaciones | promedio: {round(prom_snk, 2)}")
print(f"Hunter x Hunter -> {cant_hxh} calificaciones | promedio: {round(prom_hxh, 2)}")
print(f"Black Clover -> {cant_bc} calificaciones | promedio: {round(prom_bc, 2)}")
print(f"Death Note -> {cant_dn} calificaciones | promedio: {round(prom_dn, 2)}")
print()
print(f"Calificación más baja: {usuario_min} le puso {nota_min} a {anime_min}")
