# Ayudantia 6

## Ejercicio 1 — Liga Civil UCN

El Centro de Estudiantes organizó la **Liga Civil UCN 2026**, un campeonato de fútbol entre 8 equipos. Se jugaron **5 fechas** con **4 partidos por fecha**, así que cada equipo jugó un partido por día.

 Al encargado de anotar los resultados en un Excel se le cayó el celular al water y lo único que se salvó fue un archivo de texto con los marcadores. Como ya es momento de subir los resultados de la liga, es urgente que se solucione este problema, es por esto que te piden a ti que hagas un programa para calcular al equipo ganador.

Los equipos son:
| Equipo       | Nombre                     |
| ------------ | -------------------------- |
| ICCI         | Saxo Team                  |
| ICI          | Los Sierra                 |
| ITI          | Indu Sex                   |
| ICI          | Zarry y los Cuetas         |
| ICCI         | Swifties                   |
| ICCI         | Piccies                    |
| ITI          | Ititis                     |
| ICI          | Ball                       |

### Formato del archivo

Los resultados están en el archivo `partidos.txt`. Cada fecha comienza con una línea `Fecha N` y le siguen sus 4 partidos:

```csv
Fecha N
local,visita,goles_local,goles_visita
```

```csv
Fecha 1
Zarry y los Cuetas,Saxo Team,3,0
Swifties,Piccies,2,0
Ball,Los Sierra,4,3
Indu Sex,Ititis,4,1
Fecha 2
Los Sierra,Indu Sex,3,4
...
```

### Reglas del campeonato

- **Puntaje:** victoria 3 puntos, empate 1 punto, derrota 0 puntos.
- **Orden de la tabla:** primero el equipo con más puntos. Si empatan en puntos, va primero el de mayor **diferencia de goles** (`DiferenciaGoles = GolesFavor - GolesContra`). Si siguen empatados, va primero el que tiene más **goles a favor**.

### Requerimientos

**Por cada fecha:**

1. Mostrar los partidos de la fecha ordenados de más a menos goles, indicando quién ganó o si fue empate.
2. Mostrar la tabla parcial (acumulada hasta esa fecha) ordenada según las reglas, con los puntos, la DiferenciaGoles y los GolesFavor de cada equipo.

**Al terminar el campeonato:**

3. Mostrar la tabla final con los partidos jugados (PJ), ganados (G), empatados (E), perdidos (P), GolesFavor, GolesContra, DiferenciaGoles y puntos de cada equipo, ordenada según las reglas.
4. Mostrar el podio: 1er, 2do y 3er lugar.
5. Mostrar el equipo **más goleador** (más GolesFavor) y el equipo **más goleado** (más GolesContra).
6. Mostrar el promedio de goles por partido.

### Restricciones

- No se puede usar `sort()`, `sorted()`, `max()`, `min()` ni `sum()`.
- Los ordenamientos se deben hacer con **burbuja**. Cada intercambio se debe replicar en **todas** las listas paralelas para no mezclar los datos.
- Se deben crear funciones propias con `def`.

### Consideraciones

- El programa va "conociendo" los equipos conforme los lee del archivo.
- Cada fecha tiene exactamente 4 partidos y cada equipo juega una vez por fecha.
- En la tabla, la condición para intercambiar dos equipos tiene que revisar los puntos, después la DiferenciaGoles y después los GolesFavor.
- Para redondear el promedio usar `round(x, 2)`.