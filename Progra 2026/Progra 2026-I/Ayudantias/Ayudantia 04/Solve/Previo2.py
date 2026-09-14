archivo = open("paises.txt","r",encoding="utf-8")
linea = archivo.readline().strip()
contador_paises = 0
contador_valores = 0

mayor = -999999
menor = 999999

paisMayor = ""
mayorSumaPais = 0

while linea != "":
    partes = linea.split(",")
    pais = partes[0]
    cant_valores = int(partes[1])

    contador_paises += 1
    
    sumaValoresPais = 0
    
    for i in range(cant_valores):
        linea = archivo.readline()
        valor = int(linea)
        
        contador_valores += 1
        
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor
            
        sumaValoresPais += valor
    
    if sumaValoresPais > mayorSumaPais:
        mayorSumaPais = sumaValoresPais
        paisMayor = pais
        
    linea = archivo.readline()

print("---------RESUMEN---------")
print(f"Mayor valor dentro del texto: {mayor}")
print(f"Menor valor dentro del texto: {menor}")
print(f"Pais con la mayor suma: {paisMayor} -> {mayorSumaPais}")