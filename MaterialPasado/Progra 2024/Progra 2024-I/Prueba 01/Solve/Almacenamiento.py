
arch = open("archivos.txt","r",encoding= "utf-8")
linea = arch.readline().strip()

cantCorruptos = 0
cantArchivos = 0

utilizadoVideos = 0

tamañoSistema = 0
cantSistema = 0

while linea != "":
    partes = linea.split(";")
    nombre = partes[0]
    extension = nombre.split(".")[1]
    tamaño = int(partes[1])
    fechaC = partes[2]
    añoC = int(fechaC.split("/")[2])
    fechaM = partes[3]
    añoM = int(fechaM.split("/")[2])
    atributo = partes[4]
    
    cantArchivos += 1
    
    if añoC - añoM == 1:
        cantCorruptos += 1

    else:
        if extension == "avi" or extension == "mov" or extension == "mpeg":
            utilizadoVideos += tamaño / 1000

        if atributo == "system":
            tamañoSistema += tamaño
            cantSistema += 1
            
    linea = arch.readline().strip()

porcentajeCorruptos = 100 * (cantCorruptos / cantArchivos)
print(f"1) Porcentaje de archivos corruptos: {round(porcentajeCorruptos,2)}%")
print(f"2) Tamaño utilizado por archivos de video: {round(utilizadoVideos,3)} MB")
promedioArchivos = tamañoSistema / cantSistema
print(f"3) Tamaño promedio de archivos del sistema: {round(promedioArchivos,2)} KB")