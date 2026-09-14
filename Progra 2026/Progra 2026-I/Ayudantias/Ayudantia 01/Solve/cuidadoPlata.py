
clpAUsd = 920
clpAEur = 1070
usdAEur = 0.88
eurAUsd = 1.14

print("Conversor de dinero")
print("1) CLP a USD")
print("2) CLP a EUR")
print("3) USD a CLP")
print("4) USD a EUR")
print("5) EUR a CLP")
print("6) EUR a USD")

opcion = int(input("Selecciona una opción: "))
monto = float(input("Ingresa el monto a convertir: "))

if opcion == 1:
    montoConvertido = monto / clpAUsd
    monedaOrigen = "CLP"
    monedaDestino = "USD"
elif opcion == 2:
    montoConvertido = monto / clpAEur
    monedaOrigen = "CLP"
    monedaDestino = "EUR"
elif opcion == 3:
    montoConvertido = monto * clpAUsd
    monedaOrigen = "USD"
    monedaDestino = "CLP"
elif opcion == 4:
    montoConvertido = monto * usdAEur
    monedaOrigen = "USD"
    monedaDestino = "EUR"
elif opcion == 5:
    montoConvertido = monto * clpAEur
    monedaOrigen = "EUR"
    monedaDestino = "CLP"
else:
    montoConvertido = monto * eurAUsd
    monedaOrigen = "EUR"
    monedaDestino = "USD"

print()
print("===CONVERSION REALIZADA===")
print(f"{monto} {monedaOrigen} equivalen a {round(montoConvertido,2)} {monedaDestino}")

if monedaDestino == "USD" and montoConvertido < 5000:
    print("Puede que vayan con muy poca plata")
