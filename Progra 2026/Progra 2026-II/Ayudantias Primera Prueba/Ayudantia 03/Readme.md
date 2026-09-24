# Ayudantia 3

## Ejercicio 1 — Ranking Anime

Un grupo de compañeros de la UCN creó una página donde los usuarios califican sus animes favoritos con notas del **1.0 al 5.0**. Por ahora solo se pueden calificar 4 animes: **Shingeki no Kyojin**, **Hunter x Hunter**, **Black Clover** y **Death Note**. Cada uno ha recibido muchas calificaciones de distintos usuarios, y te piden un programa que analice los resultados.

Las calificaciones se guardan en el archivo `calificaciones.txt` con el siguiente formato:

```csv
anime,calificacion,usuario
```

```csv
Shingeki no Kyojin,4.8,otaku_rodri
Black Clover,3.2,asta_grita
Death Note,4.3,light_yagami
Hunter x Hunter,5.0,gon_freecss
Black Clover,2.7,sasha_patata
...
```

### Requerimientos

- Mostrar un mensaje de bienvenida.
- Abrir y leer el archivo `calificaciones.txt`.
- Mostrar la cantidad de calificaciones y el promedio de cada anime.
- Mostrar la calificación **más baja** de todo el archivo, indicando el usuario y el anime.

### Ejemplo

```text
=== Bienvenido al Ranking Anime ===
Shingeki no Kyojin -> 6 calificaciones | promedio: 4.52
Hunter x Hunter -> 6 calificaciones | promedio: 4.27
Black Clover -> 6 calificaciones | promedio: 3.03
Death Note -> 6 calificaciones | promedio: 3.93

Calificación más baja: hater_del_hiatus le puso 1.3 a Hunter x Hunter
```

## Ejercicio 2 — Calculadora de Terremotos

Se vienen las Fiestas Patrias y un grupo de amigos lleva años anotando cuántos **terremotos** se toma cada uno en las fondas. Quieren saber de una vez por todas qué día se toma más y quién es el verdadero campeón del terremoto. Los amigos son: **Javier**, **Catalina**, **Martin** y **Sofia**.

Los registros se guardan en el archivo `terremotos.txt` con el siguiente formato:

```csv
dia-mes-año,cantidad,nombre,lugar
```

```csv
18-09-2024,4,Javier,Fonda La Pampilla
18-09-2024,2,Catalina,Fonda La Pampilla
17-09-2024,1,Martin,Ramada El Copihue
19-09-2024,3,Sofia,Fonda Los Huasos
...
```

> **Nota:** el archivo tiene registros de varios años y también de otros días (como el 16 o el 20). Para comparar días solo se consideran el **17, 18 y 19 de septiembre**, sin importar el año.

### Requerimientos

- Mostrar un mensaje de bienvenida.
- Abrir y leer el archivo `terremotos.txt`.
- Separar la fecha para obtener el día y el mes.
- Calcular el total de terremotos tomados los días 17, 18 y 19 de septiembre, y mostrar cuál de los tres días fue el más terremotero.
- Mostrar quién tomó más terremotos **en un solo día**, indicando la fecha y el lugar.
- Mostrar la persona que tomó más terremotos **considerando todos los días**.

### Ejemplo

```text
=== Bienvenido a la Calculadora de Terremotos ===
¡Felices Fiestas Patrias!

Terremotos el 17 de septiembre: 8
Terremotos el 18 de septiembre: 25
Terremotos el 19 de septiembre: 19
El día más terremotero es el 18 de septiembre

Récord en un día: Javier se tomó 7 terremotos el 18-09-2025 en Ramada El Copihue
Campeón del terremoto: Javier con 16 terremotos en total
```

## Ejercicio 3 — Control de Tiendas Rockstar

**Rockstar Games** abrió 5 tiendas oficiales y necesita un programa para controlar sus ventas. Cada tienda vende sus juegos más famosos: **GTA V**, **GTA VI** (en preventa), **Red Dead Redemption 2** y **GTA San Andreas**. Las ventas pueden hacerse en la **tienda física** o en la **página web** de cada tienda.

Cada tienda tiene su propio archivo: `tienda1.txt`, `tienda2.txt`, `tienda3.txt`, `tienda4.txt` y `tienda5.txt`. La primera línea contiene el nombre de la tienda y las siguientes líneas son las ventas:

```csv
nombre_tienda
juego,fecha,precio,codigo
```

```csv
Rockstar Store Los Santos
GTA V,02/03/2026,19990,LOCAL-4821
GTA VI,05/03/2026,69990,WEB-7730
Red Dead Redemption 2,07/03/2026,29990,LOCAL-1183
GTA San Andreas,10/03/2026,9990,LOCAL-6502
...
```

El `codigo` tiene el formato `plataforma-numero`, donde la plataforma puede ser `WEB` (venta por la página) o `LOCAL` (venta en la tienda física).

### Requerimientos

- Mostrar un mensaje de bienvenida.
- Abrir y leer los 5 archivos.
- Separar el código para saber si la venta fue `WEB` o `LOCAL`.
- Por cada tienda, mostrar su nombre, cantidad de ventas (cuántas `WEB` y cuántas `LOCAL`) y su ganancia total.
- Mostrar el juego que generó **más ganancia** entre todas las tiendas.
- Mostrar la cantidad de ventas y ganancia de cada plataforma.
- Mostrar la venta **más cara**, indicando juego, tienda, fecha y código.

### Ejemplo

```text
=== Sistema de Control de Tiendas Rockstar Games ===

Rockstar Store Los Santos | Ventas: 8 (WEB: 3, LOCAL: 5) | Ganancia: $259920
Rockstar Store Liberty City | Ventas: 9 (WEB: 3, LOCAL: 6) | Ganancia: $264910
Rockstar Store Vice City | Ventas: 9 (WEB: 2, LOCAL: 7) | Ganancia: $249910
Rockstar Store San Fierro | Ventas: 8 (WEB: 3, LOCAL: 5) | Ganancia: $190920
Rockstar Store Las Venturas | Ventas: 7 (WEB: 3, LOCAL: 4) | Ganancia: $239930

=== RESUMEN GENERAL ===
Juego que generó más ganancia: GTA VI ($634910)
WEB -> 14 ventas | $699860
LOCAL -> 27 ventas | $505730
Venta más cara: GTA VI a $74990 en Rockstar Store Liberty City el 14/03/2026 (WEB-6093)
```
