import numpy as np
def get_price(gate, time):
    parts = time.split(':')
    hour = int(parts[0])
    if hour == 7 or hour == 19:
        return high_prices[gates.index(gate)]
    return low_prices[gates.index(gate)]

def swap(li, a, b):
    aux = li[a]
    li[a] = li[b]
    li[b] = aux
    
file = open('padron.txt', encoding='utf-8')
line = file.readline().strip()

clients = []
license_plates = []
clients_balance = []

while line != '': 
    parts = line.split(',')
    client = parts[0]
    license_plate = parts[1]
    clients.append(client)
    license_plates.append(license_plate)
    clients_balance.append(0)
    line = file.readline().strip()

#Autopista,ID_Pórtico,Tramo/Ubicación,Sentido,Tarifa_Base_Fuera_de_Punta_CLP,Tarifa_Base_Punta_CLP
file = open('porticos.txt', encoding='utf-8')
line = file.readline().strip()

freeways = []
u_freeways = []
gates = []
low_prices = []
high_prices = []

while line != '': 
    parts = line.split(',')
    freeway = parts[0]
    gate = parts[1]
    gate_name = parts[2]
    low_price = round(float(parts[4]))
    high_price = round(float(parts[5]))
    if not freeway in u_freeways:
        u_freeways.append(freeway)
    freeways.append(freeway)
    gates.append(gate)
    low_prices.append(low_price)
    high_prices.append(high_price)
    line = file.readline().strip()
# Fecha,Hora,Patente,ID_Portico
# 2026-01-01,00:40:31,GGPF26,PA3
file = open('registro-televia.txt', encoding='utf-8')
line = file.readline().strip()

freeways_use = np.zeros([len(u_freeways),12])
freeways_balance = np.zeros([len(u_freeways),12])
while line != '': 
    parts = line.split(',')
    date = parts[0].split('-')
    month = int(date[1])
    time = parts[1]
    license_plate = parts[2]
    gate = parts[3]
    price = get_price(gate,time)
    freeways_use[u_freeways.index(freeways[gates.index(gate)])][month-1] += 1 
    freeways_balance[u_freeways.index(freeways[gates.index(gate)])][month-1] += price
    if license_plate in license_plates:
        clients_balance[license_plates.index(license_plate)] += price

    line = file.readline().strip()

for a in range(len(clients)-1):
    for b in range(a+1, len(clients)):
        if clients_balance[a] < clients_balance[b]:
            swap(clients_balance, a, b)
            swap(clients, a, b)
            swap(license_plates, a, b)
print('1) Top 5 clientes que más gastan: ')
for i in range(5):
    print(f'  - {clients[i]}: ${clients_balance[i]}')
    
max_income = -1
max_month = -1
min_freeway = ''
for column in range(12):
    sum_ = 0
    min_income = 10**10
    min_row = -1
    for row in range(len(u_freeways)):
        sum_ += freeways_balance[row][column]
        if freeways_balance[row][column] < min_income:
            min_income = freeways_balance[row][column]
            min_row = row
    if sum_ > max_income:
        max_income = sum_
        max_month = column + 1
        min_freeway = u_freeways[min_row]
print(f'2) El mes {max_month} fue el de mayores ingresos (${max_income}) y la autopista que menos ingresos generó ese mes fue {min_freeway}')
print('3) Tránsito promedio mensual')
for row in range(len(u_freeways)):    
    sum_ = 0
    max_use = -10**10
    for column in range(12):
        sum_ += freeways_use[row][column]
        if freeways_use[row][column] > max_use:
            max_use = freeways_use[row][column]
    print(u_freeways[row].upper(), round(sum_/12))
    print('   Mes(es) más transitado(s):')
    for c in range(12):
        if freeways_use[row][c] == max_use:
            print('    - ',c+1)