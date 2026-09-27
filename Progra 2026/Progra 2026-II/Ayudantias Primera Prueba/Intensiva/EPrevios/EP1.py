mayor = -101
mayor2 = -101

for i in range(6):
    
    num = int(input("Ingrese númmero: "))
    
    if (num > mayor):
        mayor2 = mayor
        mayor = num
        
    elif (num != mayor and num > mayor2):
        mayor2 = num
        
print(mayor)
print(mayor2)