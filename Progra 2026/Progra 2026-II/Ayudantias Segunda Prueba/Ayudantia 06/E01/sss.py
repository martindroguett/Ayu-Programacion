def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbujaFecha(goles, ganadores):
    
    for a in range(len(goles) - 1):
        for b in range(a+1, len(goles)):
            
            if goles[a] < goles[b]:
                intercambiar(goles, a, b)
                intercambiar(ganadores, a, b)

def revisarFecha(arch, fecha):
    
    goles = []
    ganadores = []
    
    for i in range(4):
        linea = arch.readline().strip()
        partes = linea.split(",")
        
        equipo1 = partes[0]
        goles1 = int(partes[2])
        
        equipo2 = partes[1]
        goles2 = int(partes[3])
        
        goles.append(goles1 + goles2)
        
        if goles1 > goles2:
            ganador = equipo1
        
        elif goles2 > goles1:
            ganador = equipo2
        
        else:
            ganador = "Empate"
        
        mensaje = f"Partido {i + 1}: {equipo1} ({goles1}) VS {equipo2} ({goles2}) -> {ganador}"
        ganadores.append(mensaje)
        
    burbujaFecha(goles, ganadores)
        
    for i in range(4):
        print(f"({goles[i]}) {ganadores[i]}")
        
    print("=" * 20)
    

arch = open("partidos.txt","r",encoding="utf-8")

linea = arch.readline().strip()

equipos = []
ganados = []
empates = []
perdidos = []
golesFavor = []
golesContra =[]

while linea != "":
    fecha = linea
    revisarFecha(arch, fecha)
        
    
    linea = arch.readline().strip()