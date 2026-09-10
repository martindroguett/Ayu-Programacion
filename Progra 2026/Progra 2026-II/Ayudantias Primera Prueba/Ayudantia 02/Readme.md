# Ayudantia 2

## Ejercicio 1 — Ruteo Ciclos

Determina, **sin ejecutar el código**, qué imprime el siguiente programa. Anota el valor de cada variable en cada paso.

```python
a = 5
b = 20
c = 1
d = 0

for i in range(6, 0, -1):
    if i % 2 == 0:
        a += i
    else:
        b -= i

    if a > b:
        d += 1

k = 6
while k > 0:
    if c % 2 == 0:
        a -= k
    else:
        b -= k
    c -= k
    k -= 2

print(a, b, c, d)
```

---

## Ejercicio 2 — El día de Matías Núñez alias Manugo

Matías Núñez es un estudiante de la universidad que se mueve por todo Coquimbo y La Serena en su moto, cumpliendo distintas actividades a lo largo del día. Cada actividad implica recorrer una cierta cantidad de kilómetros, y su moto consume combustible según el tipo de trayecto que haga.

Amablemente, en su necesidad de administrar su consumo de combustible, te pide a ti como alumno de programación escribir un programa en Python que simule el día de sus viajes y calcule cuánto combustible gastó en total.

### Consideraciones del problema

1. El programa debe ir pidiendo, uno a la vez, los **kilómetros recorridos** en cada actividad. El usuario ingresa `-1` cuando Matías termina su día.
2. Por cada actividad (mientras no se ingrese `-1`), el programa debe preguntar el **tipo de trayecto**: `ciudad` o `carretera`.
   - `ciudad` → gasta **0.08 litros por km**
   - `carretera` → gasta **0.05 litros por km**
   - Si el trayecto no es ninguno de los anteriores, se debe preguntar de nuevo hasta que lo sea, o ponga el fin de datos `-1`.
3. Por cada actividad válida, el programa pregunta además si **está lloviendo** (`si`/`no`). Si llueve, el gasto de esa actividad aumenta un 20%.
4. Matías tiene un **límite de combustible diario de 8 litros**. Si una actividad haría que se supere ese límite, el programa debe avisar `"Matías se quedó sin bencina, debe volver a casa"` y terminar el día ahí mismo (sin seguir pidiendo actividades).
5. Al terminar (ya sea porque se acabó la bencina o porque el usuario ingresó `-1`), se imprime el total de kilómetros recorridos, el total de combustible gastado y el gasto mayor de su viaje.

### Restricciones

- Solo se permite usar **ciclos (`while`) y condicionales (`if`/`elif`/`else`)**. No uses `continue`, funciones propias ni listas.

### Ejemplo de ejecución

```
Kilómetros recorridos (-1 para terminar): 23
Tipo de trayecto (ciudad/autopista): ciudad
¿Está lloviendo? (s/n): s
Kilómetros recorridos (-1 para terminar): 15
Tipo de trayecto (ciudad/autopista): autopista
¿Está lloviendo? (s/n): n
Kilómetros recorridos (-1 para terminar): -1

***********DIA DE MANUGO***********
Kilómetros totales: 38.0
Combustible total gastado: 2.96
Mayor gasto en un solo trayecto: 2.208
```

---

## Ejercicio 3 — Hofercito busca a su novia

Hofercito y su novia son dos robots que se encuentran varados en un plano **XY**, de manera que, sin saber cómo encontrarse el uno al otro, deciden llamar a un alumno de la UCN para desarrollar un programa de ciclos y algoritmos que habilite su reencuentro. Sin embargo, su novia es muy floja y tiende a perderse, por lo cual deberás darle instrucciones a Hofercito en su idioma, un **código de movimientos** (un string), donde cada carácter representa una acción, mientras su novia le grita hacia dónde debe dirigirse:

- `S` → Subir (+1 en y)
- `B` → Bajar (-1 en y)
- `D` → derecha (+1 en x)
- `I` → izquierda (-1 en x)
- `X` → calcula e imprime la distancia actual entre Hofercito y su novia (sin mover a nadie, distancia euclidiana)

**Hofercito** parte en `(0, 0)`. **La novia** está perdida: genera su ubicación de manera aleatoria importando `random` (`import random`). El plano va de **0 a 10** en ambos ejes; Hofercito no puede salir de ese rango.

### Reglas

1. El programa recorre el código carácter por carácter, aplicando el movimiento correspondiente a Hofercito, validando que no se salga del plano (0 a 10) antes de aplicar cada movimiento.
2. Después de cada movimiento, se revisa si Hofercito llegó a la posición de su novia. Si es así, se imprime `"¡Hofer encontró a su Novia!"`.
3. Además, después de cada movimiento, la novia le "grita" indicaciones a Hofercito según hacia dónde le falta acercarse (derecha/izquierda, subir/bajar).
4. Si no se encuentran con un código, se sigue pidiendo códigos nuevos (Hofercito mantiene su posición entre uno y otro) hasta ingresar un código vacío (`""`), momento en el que se imprime la distancia final.

### Recomendación

- Ocupa el comando **break** en caso de encontrar a la novia de Hofer, cortando el ciclo.

### Restricciones

- Solo `while`, `for` e `if`/`elif`/`else`. No uses `split`, `continue`, funciones propias ni listas.

### Ejemplo de ejecución

```
Ingresa el codigo de movimientos: SSDD
La novia grita: ¡Ve a la derecha!
La novia grita: ¡Sube!
Ingresa el codigo de movimientos: X
La distancia es: 2.8284271247461903
La novia grita: ¡Ve a la derecha!
La novia grita: ¡Sube!
Ingresa el codigo de movimientos: SSDD
¡Hofer encontró a su novia! en la posicion (4,5)
```
