def buscarAgregar(elemento, lista):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

def imprimirPerros(perrosOctuple, perrosAntirrabica, perrosKc):
    print("--Octuple")
    imprimirLista(perrosOctuple)
    print("--Antirrabica--")
    imprimirLista(perrosAntirrabica)
    print("--KC--")
    imprimirLista(perrosKc)

def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i])
        
arch = open("perros.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

vacunas = []
perrosOctuple = []
perrosAntirrabica = []
perrosKc = []

masLongevo = ""
edadMasLongevo = -9999999

while linea != "PRECIOS":
    partes = linea.split("-")
    nombre = partes[0]
    meses = int(partes[1])    
    años = meses // 12
    
    necesariaOctuple = 3
    necesariaAntirrabica = 2
    necesariaKc = 1
    
    for _ in range(años - 1):
        necesariaOctuple += 1
        necesariaAntirrabica += 1
        necesariaKc += 1

    dosisOctuple = int(partes[2])
    dosisAntirrabica = int(partes[3])
    dosisKc = int(partes[4])
    
    if dosisOctuple < necesariaOctuple:
        perrosOctuple.append(nombre)
    if dosisAntirrabica < necesariaAntirrabica:
        perrosAntirrabica.append(nombre)
    if dosisKc < necesariaKc:
        perrosKc.append(nombre)
    
    if meses > edadMasLongevo:
        edadMasLongevo = meses
        masLongevo = nombre
    
    linea = arch.readline().strip()

precioOctuple = int(arch.readline().strip())
precioAntirrabica = int(arch.readline().strip())
precioKc= int(arch.readline().strip())

imprimirPerros(perrosOctuple, perrosAntirrabica, perrosKc)

print(f"El perro mas longevo es: {masLongevo} con {edadMasLongevo // 12} año(s) y {edadMasLongevo % 12} mes(es)")
ingresos = precioOctuple * len(perrosOctuple) + precioAntirrabica * len(perrosAntirrabica) + precioKc * len(perrosKc)
print(f"Posibles ingresos por vacunacion: {ingresos}")
