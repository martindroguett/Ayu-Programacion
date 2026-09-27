# Ayudantía intensiva 1 de programación 2026-II

Contacto: martin.droguett@alumnos.ucn.cl

## Ejercicios Previos

### Ejercicio 1: Segundo mayor

Escribe un programa que lea 6 números enteros e imprima el mayor y el segundo mayor. Los números pueden ser entre [-100, 100] y repetirse.

**Ejemplo**

```
Entrada: 4, 9, -2, 9, 7, 1
Salida:  Mayor: 9, segundo mayor: 7
```

### Ejercicio 2: La persona mayor y la menor

Escribe un programa que lea el nombre y la edad de 5 personas, y muestre el nombre y la edad de la persona mayor y de la menor. Si hay empate, se queda la primera persona ingresada.

**Ejemplo**

```
Entrada: Ana 10, Beto 20, Cami 30, Dani 40, Eli 50
Salida:  Mayor: Eli (50 años)
         Menor: Ana (10 años)
```

### Ejercicio 3: Promedio de notas

Escribe un programa que lea notas hasta que se ingrese un `0`. Las notas fuera del rango 1.0 a 7.0 se ignoran mostrando un mensaje. Al final muestra el promedio de las notas válidas y cuántas fueron rojas (menores a 4.0).

**Ejemplo**

```
Entrada: 6.0, 3.5, 8.0, 4.0, 5.5, 0
Salida:  Nota inválida
         Promedio: 4.75
         Notas rojas: 1
```

### Ejercicio 4: Dígitos

Escribe un programa que lea un número entero y muestre cuántos dígitos tiene y cuánto suman.

**Ejemplos**

| Entrada | Salida |
|---|---|
| `4507` | `Dígitos: 4, suma: 16` |
| `-305` | `Dígitos: 3, suma: 8` |
| `0` | `Dígitos: 1, suma: 0` |

### Ejercicio 5: Primo

Escribe un programa que lea un número entero e indique si es primo.

**Ejemplos**

| Entrada | Salida |
|---|---|
| `1` | `1 no es primo` |
| `2` | `2 es primo` |
| `9` | `9 no es primo` |
| `13` | `13 es primo` |

### Ejercicio 6: Contar vocales

Escribe un programa que lea una frase y cuente cuántas vocales tiene (mayúsculas y minúsculas).

**Ejemplo**

```
Entrada: Hola Mundo, HOLA soy Python
Salida:  Vocales: 8
```

### Ejercicio 7: Temperaturas

Escribe un programa que lea las temperaturas de 8 días (enteros) y muestre cuántas veces subió la temperatura respecto al día anterior y cuál fue la racha más larga de subidas consecutivas.

**Ejemplo**

```
Entrada: 12, 14, 15, 13, 16, 18, 20, 21
Salida:  Subidas: 6
         Racha más larga: 4
```

### Ejercicio 8: Notas por alumno

**Archivo:** `notas.txt`

Cada alumno aparece en una línea con su nombre y cuántas notas tiene. Luego vienen esas notas, una por línea.

```
Juan,3
4.5
6.0
6.0
Ana,2
7.0
6.5
Luis,0
Pedro,4
3.0
4.5
2.5
5.0
```

Escribe un programa que muestre el promedio de cada alumno y quién tuvo el mejor promedio.

**Salida esperada**

```
Juan: 5.5
Ana: 6.75
Luis: sin notas
Pedro: 3.75
Mejor promedio: Ana con 6.75
```

### Ejercicio 9: Ventas por día

**Archivo:** `ventas.txt`

Las líneas que empiezan con `F` indican una fecha. Las que empiezan con `P` son productos vendidos ese día, con el formato `P;producto;precio;cantidad`.

```
F;23/09/2026
P;Pan;1500;2
F;24/09/2026
P;Pan;1500;3
P;Leche;1100;2
F;25/09/2026
P;Pan;1500;1
P;Queso;4200;1
P;Leche;1100;4
```

Escribe un programa que muestre el total vendido cada día y cuál fue el día con más ventas.

**Salida esperada**

```
23/09/2026: $3000
24/09/2026: $6700
25/09/2026: $10100
Día con más ventas: 25/09/2026 ($10100)
```

---

## Ruteo
``` python
k = input('k?: ')
t = int(input('t?: '))
p = 1
q = 0
s = ''
while t != 0:
    if t < 0:
        s = s + '-'
        t = int(input('t?: '))
        continue
    if t % 2 == 0 and t > p:
        p = t // 2
        s = s + 'P'
    elif t % 3 == 0 or t == p:
        q = q + t
        s = s + 'Q'
    else:
        p = p + 1
    if q > 10:
        break
    t = int(input('t?: '))
for i in range(1, q, 4):
    i = i * 2
    p = p + i
if k == 3:
    s = s + '!'
else:
    s = k + s
print(f'{s} {p}{q // 4} {q / 4}')
```

Asuma los siguientes valores para los inputs, en orden:
``` txt
3
6
-4
9
5
4
3
8
0
```

| k | t | p | q | s | i |
|---|---|---|---|---|---|
| _ | _ | _ | _ | _ | _ | 

## Lectura de Archivos
El profesor Eugenio guardó todas las notas del semestre en el archivo `curso.txt`. Escribe un programa que lea el archivo y calcule la situación final de cada alumno y algunas estadísticas del curso.
 
### Formato del archivo
 
La primera línea indica el curso y el semestre. Después vienen los alumnos, cada uno seguido de sus notas.
 
| Línea | Formato | Ejemplo |
|---|---|---|
| Encabezado (solo la primera línea) | `curso;semestre` | `Programación;2026-2` |
| Alumno | `A;rut;nombre` | `A;21.345.678-9;Camila Rojas` |
| Control | `C;nota` | `C;5.5` |
| Prueba | `P;nota` | `P;4.5` |
 

### Consideraciones 
- No se indica cuántas notas tiene cada alumno. Sus notas terminan cuando aparece el siguiente alumno o se acaba el archivo.
- Los controles y las pruebas pueden venir mezclados.
- Una nota puede ser `NSP` (no se presentó), y en ese caso cuenta como 1.0.
- Todo alumno tiene al menos un control y al menos una prueba.

### Reglas
- **Nota de controles (NC):** promedio de los controles, eliminando el peor. Si el alumno tiene un solo control, su NC es ese control.
- **Nota de pruebas (NP):** `(NP1 * 0.45 + NP2 * 0.55)`.
- **Nota final:** `(NP * 0.7 + NC * 0.3)`
- **NP:** Si se encuentra entre 3.3 y 3.9 debe ir a Recalificación. Si es inferior a 3.3, reprueba inmediatamente.
- **NC:** si NC es inferior a 4.0, reprueba inmediatamente.
- **Empates:** si hay empate en cualquier comparación, se considera al alumno que aparece primero en el archivo.

### Requisitos
1. Mostrar el nombre del curso y el semestre.
2. Para cada alumno, mostrar su NC, NP, nota final y estado.
3. El alumno con la mejor nota final y el que tiene la segunda mejor.
4. El porcentaje de aprobación del curso.
5. El alumno con más controles rojos y cuántos tiene.
6. El control más bajo de todo el curso **sin contar los NSP**, y a quién pertenece.