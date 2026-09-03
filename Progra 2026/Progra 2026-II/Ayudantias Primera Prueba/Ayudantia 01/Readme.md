# Ayudantia 1

<img align="right" width=180px alt="Aura farming" src="https://media.tenor.com/GQAsycjoZG8AAAAi/scuba-scuba-cat.gif" />

## Ejercicio 1 — Ruteo

Determina, **sin ejecutar el código**, qué imprime el siguiente programa. Anota el valor de cada variable en cada paso.

```py
aura = 67
labubu = 4
sigma = aura % labubu
skibidi = aura // labubu

if aura > 50 and sigma != 0:
    aura -= sigma
    labubu += skibidi

if labubu % 2 == 0:
    skibidi *= 2
elif aura > 60:
    skibidi += 10
else:
    skibidi = 0

if skibidi > 20:
    sigma = skibidi - labubu
if sigma < 10:
    labubu += 1
else:
    labubu -= 4

nivel = aura / labubu

if nivel > 5 and sigma == 12:
    rango = "novato"
elif nivel >= 3:
    rango = "leyenda"
else:
    rango = "mid"

nombre = "67"
nombre = nombre * 2

print(aura, labubu, sigma, skibidi)
print(f"{nombre} es {rango} con nivel {nivel}")
```

## Ejercicio 2 — Compras

Javier Catalán es un fan de ir al mall. Cada día hace la misma rutina, revisa siempre los mismos 6 productos y decide cuáles lleva y cuáles no. Los precios que estima son:

| Producto              | Precio     |
| --------------------- | ---------- |
| Cartas Pokémon        | $250.000   |
| Matcha latte          | $7.000     |
| Donas                 | $15.000    |
| Merch Kuromi          | $50.000    |
| Accesorios de vóleibol| $120.000   |
| Ropa                  | $200.000   |

Su tarjeta Visa aplica un descuento sobre el **total acumulado**, según el tramo que alcance. Se aplica solo el descuento más alto que corresponda:

| Total acumulado      | Descuento |
| -------------------- | --------- |
| $50.000 o más        | 5%        |
| $100.000 o más       | 10%       |
| $200.000 o más       | 15%       |

### Requerimientos

- Consultar a Javier qué productos desea llevar.
- Aplicar el descuento según el total acumulado.
- Mostrar por pantalla el total acumulado y el precio final tras el descuento.

### Ejemplo

```text
Lleva cartas Pokémon? (s/n): n
Lleva matcha latte? (s/n): s
Lleva donas? (s/n): s
Lleva merch Kuromi? (s/n): s
Lleva accesorios de vóleibol? (s/n): n
Lleva ropa? (s/n): n

Total acumulado: $72.000
Descuento aplicado: 5%
Precio final: $68.400
```

## Ejercicio 3 — Revisión
 
Catalina está evaluando los controles de los estudiantes de programación. La rúbrica asigna una nota dependiendo de los ejercicios que cada estudiante resolvió, así que les pide a los propios estudiantes que hagan un programa que agilice este proceso. El control contó con 3 ejercicios.
 
Para calcular la nota se debe considerar lo siguiente:
 
| Ejercicios resueltos             | Nota |
| -------------------------------- | ---- |
| Ninguno                          | 1.0  |
| Primer ejercicio                 | 3.0  |
| Segundo ejercicio                | 3.0  |
| Tercer ejercicio                 | 3.0  |
| Primer y segundo ejercicio       | 4.5  |
| Primer y tercer ejercicio        | 5.0  |
| Segundo y tercer ejercicio       | 5.5  |
| Primer, segundo y tercer ejercicio | 7.0 |
  
### Requerimientos
 
- Preguntar el nombre del estudiante.
- Preguntar qué ejercicios resolvió.
- Utilizar `or` y `and`.
- Imprimir qué nota obtuvo.

### Ejemplo
 
```text
Ingresa el nombre del estudiante: Martín
 
Resolvió el primer ejercicio? (s/n): n
Resolvió el segundo ejercicio? (s/n): s
Resolvió el tercer ejercicio? (s/n): s
 
Martín obtuvo un 5.5
```