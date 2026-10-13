

def mi_len(texto):

    num = 0
    for char in texto:
        num += 1

    return num

print(mi_len(" ")) # 1

def mi_strip(texto):
    temp = ""

    largo = mi_len(texto)
    if largo == 0:
        return ""

    inicio = 0
    while inicio < largo and (texto[inicio] == "\t" or texto[inicio] == " " or texto[inicio] == "\n"):
        inicio += 1

    if inicio == largo:
        return ""

    fin = largo - 1

    while texto[fin] == "\t" or texto[fin] == " " or texto[fin] == "\n":
        fin -= 1

    for i in range(inicio, fin + 1):
        temp += texto[i]

    return temp

print(mi_strip("   hola\n"))
print(mi_strip("")) # ""
print(mi_strip("   ")) # ""

def mi_replace(texto, buscar, reemplazar):

    temp = ""
    for char in texto:

        if char == buscar:
            temp += reemplazar
        else:
            temp += char

    return temp

print(mi_replace("hola mundo", "o", "0"))

def mi_find(texto, subtexto):

    if subtexto == "":
        return 0

    largo_texto = mi_len(texto)
    largo_sub = mi_len(subtexto)

    if largo_sub > largo_texto:
        return -1

    for i in range(largo_texto - largo_sub + 1):
        calza = True
        for j in range(largo_sub):
            if texto[i + j] != subtexto[j]:
                calza = False
                break
        if calza:
            return i

    return -1

print(mi_find("hola mundo", "mundo")) # 5
print(mi_find("banana", "ana")) # 1
print(mi_find("hola", "x")) # -1
print(mi_find("hola", "")) # 0
