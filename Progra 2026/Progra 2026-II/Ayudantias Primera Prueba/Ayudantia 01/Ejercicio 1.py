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