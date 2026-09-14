
arch = open("codigo_enigma.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

numActual = 1

oracion = ""

while linea != "endwar":
    
    if numActual % 2 != 0:
        partes = linea.split("?")
        partesSeparador = partes[0].split(":")
        separador = partesSeparador[1]
        partesPosicion = partes[1].split("=")
        posicion =int(partesPosicion[1])
    
    else:
        partes = linea.split(separador)
        oracion += partes[posicion]
    
    numActual += 1
    linea = arch.readline().strip()

print(oracion)
