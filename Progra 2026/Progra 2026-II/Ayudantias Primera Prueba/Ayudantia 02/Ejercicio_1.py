a = 5
b = 20
c = 1
d = 0

for i in range(6, 0, -1):# 6, 5, 4, 3, 2 y 1
    if i % 2 == 0:
        a += i
    else:
        b -= i

    if a > b:
        d += 1
        
#Despues del for: a = 17, b = 11, c = 1, d = 3.
