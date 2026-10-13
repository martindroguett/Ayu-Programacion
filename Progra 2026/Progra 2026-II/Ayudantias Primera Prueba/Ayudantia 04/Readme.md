# Ayudantia 4

## Ejercicio 1 — Entrevista de Trabajo

Te presentas a una entrevista de trabajo y te piden demostrar que entiendes cómo funcionan las funciones nativas de Python **implementándolas tú mismo**.

### Funciones a implementar

#### 1. Función `len()`

Dado un string, debes devolver el número de caracteres que tiene.

```python
mi_len("hola") -> 4
mi_len("") -> 0
mi_len(" ") -> 1
```

#### 2. Función `strip()`

Dado un string, debes quitarle los espacios en blanco que lo rodeen (espacios, `\n`, `\t`).

```python
mi_strip(" hola ") -> "hola"
mi_strip("hola\n") -> "hola"
mi_strip("no") -> "no"
```

#### 3. Función `replace()`

Dado un string, un carácter a buscar y un carácter de reemplazo, debes reemplazar todas las apariciones del carácter buscado por el de reemplazo.

```python
mi_replace("hola mundo", "o", "0") -> "h0la mund0"
mi_replace("banana", "a", "e") -> "benene"
mi_replace("hola", "x", "y") -> "hola"
```

#### 4. Función `find()`

Dado un string y un substring, debes devolver el índice de la primera aparición del substring, o `-1` si no existe.

```python
mi_find("hola mundo", "mundo") -> 5
mi_find("banana", "ana") -> 1
mi_find("hola", "x") -> -1
mi_find("hola", "") -> 0
```

### Consideraciones

- Recuerda no usar los mismos nombres que las funciones que ya existen en Python.
- No puedes usar las funciones nativas de Python.
- Puedes usar las funciones que hiciste antes, como usar `mi_len()` dentro de tu función `mi_strip()`

---

## Ejercicio 2 — Esta todo malo

A un amigo se le acabó el límite de uso de Claude de la semana y te pide tu ayuda para arreglar su código de programación.

Te envio el archivo `hola.py`, que es un "intento" de solución de la ayudantía 3 (Tiendas Rockstar).

Tu trabajo se compone en tres partes:

1. Revisar el código para encontrar los errores que dejo tu amigo.
2. Si encontraste errores, arreglalos sin reescribir el programa desde cero.
3. Meterle funciones donde tenga sentido.

### Criterios para el punto 3

- Crear mínimo 3 funciones propias con `def` y `return` (no solo `print`).
- El programa debe imprimir exactamente lo mismo que la salida de la ayudantía pasada.

---

## Ejercicio 3 — Sistema Bancario

Haremos una simulacion de un sistema bancario muy simple.
Este banco tiene un limite de 40 cuentas, con sus movimientos separados en diferentes archivos, en archivos estilo `cuenta1.txt`, `cuenta2.txt`, ..., `cuenta40.txt`. Cada archivo tiene el siguiente formato.

<p align="center">codigo,usuario<br>fecha,monto,tipo</p>

El `tipo` puede ser `DEPOSITO` o `GIRO`. El usuario elige el número de cuenta que quiere revisar y opera por menú.

### Menú principal

```text
=== BANCO ===
1. Revisar una cuenta
0. Salir
Opción: 1
Número de cuenta (1-40): 7
```

Si el número no está entre 1 y 40, se pide de nuevo hasta que sea válido.

### Submenú de la cuenta

```text
--- Cuenta 7 (CTA-0007) | Titular: sofi_perez ---
1. Ver saldo
2. Ver cantidad de movimientos
3. Ver promedio de movimientos
4. Volver al menú principal
Opción: 1
Saldo: $45000
```

Al abrir la cuenta se debe mostrar su código y su titular (primera línea del archivo).

### Consideraciones

- Se recomienda no usar variables globales.
- No hay problema si se abren varias veces el mismo archivo, pero recordar cerrarlo usando `arch.close()`
