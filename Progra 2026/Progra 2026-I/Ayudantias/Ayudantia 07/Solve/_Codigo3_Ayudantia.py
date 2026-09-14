# Lista con espacio y letras del abecedario.
# Cada posición representa un código.

abecedario = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]

# Lista de números que representa el mensaje codificado.
codigo = [6, 5, 12, 9, 3, 9, 4, 1, 4, 5, 19,0,22, 1, 19,0,2, 9, 5, 14,0,5, 14, 3, 1, 13, 9, 14, 1, 4, 15]

# Variable donde se irá formando el mensaje final.
mensaje = ""

# Recorremos la lista de códigos.
for i in range(len(codigo)):

    # Obtenemos el número que está en la posición i.
    posicion = codigo[i]

    # Usamos ese número como índice para buscar la letra en el abecedario.
    letra = abecedario[posicion]

    # Agregamos la letra al mensaje.
    mensaje = mensaje + letra

# Convertimos la primera letra a mayúscula para que el mensaje quede bien escrito.
mensaje = mensaje[0].upper() + mensaje[1:]

# Mostramos el mensaje descodificado.
print(mensaje)