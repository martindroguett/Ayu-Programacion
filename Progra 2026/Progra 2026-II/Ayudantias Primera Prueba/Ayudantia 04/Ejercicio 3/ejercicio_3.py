# ejercicio_3.py - solucion pauta Ejercicio 3 Banco de 40 Cuentas (Ayudantia 4)
# El numero de cuenta vive solo en el main y se pasa por parametro (sin globales).


def ruta_cuenta(n):
    return f"cuenta{n}.txt"

def get_codigo(n):
    arch = open(ruta_cuenta(n), "r", encoding="utf-8")
    codigo = arch.readline().strip().split(",")[0]
    arch.close()
    return codigo


def get_titular(n):
    arch = open(ruta_cuenta(n), "r", encoding="utf-8")
    titular = arch.readline().strip().split(",")[1]
    arch.close()
    return titular


def get_saldo(n):
    arch = open(ruta_cuenta(n), "r", encoding="utf-8")
    arch.readline()
    saldo = 0
    linea = arch.readline().strip()
    while linea != "":
        partes = linea.split(",")
        monto = int(partes[1])
        if partes[2] == "DEPOSITO":
            saldo += monto
        else:
            saldo -= monto
        linea = arch.readline().strip()
    arch.close()
    return saldo


def get_cantidad(n):
    arch = open(ruta_cuenta(n), "r", encoding="utf-8")
    arch.readline()
    cantidad = 0
    linea = arch.readline().strip()
    while linea != "":
        cantidad += 1
        linea = arch.readline().strip()
    arch.close()
    return cantidad


def get_promedio(n):
    arch = open(ruta_cuenta(n), "r", encoding="utf-8")
    arch.readline()
    suma = 0
    cantidad = 0
    linea = arch.readline().strip()
    while linea != "":
        partes = linea.split(",")
        suma += int(partes[1])
        cantidad += 1
        linea = arch.readline().strip()
    arch.close()
    return suma // cantidad

def mostrar_menu_inicio():
    opcion = ""
    while opcion != "0":
        print("Elija una opcion:")
        print("1. Revisar una cuenta")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            revisar_cuenta()
        elif opcion == "0":
            print("Saliendo...")
        else:
            print("Opcion incorrecta.")

def revisar_cuenta():
    num = input("Número de cuenta (1-40): ").strip()
    while int(num) < 1 or int(num) > 40:
        num = input("Número inválido. Número de cuenta (1-40): ").strip()
    print(f"--- Cuenta {num} ({get_codigo(num)}) | Titular: {get_titular(num)} ---")

    opcion = ''
    while opcion != "4":
        mostrar_menu_cuenta()
        opcion = input("Opción: ").strip()
        if opcion == "1":
            print(f"Saldo: ${get_saldo(num)}")
        elif opcion == "2":
            print(f"Movimientos: {get_cantidad(num)}")
        elif opcion == "3":
            print(f"Promedio: ${get_promedio(num)}")
        elif opcion != "4":
            print("Opción inválida.")
    print("Volviendo al menu...")



def mostrar_menu_cuenta():
    print("1. Ver saldo")
    print("2. Ver cantidad de movimientos")
    print("3. Ver promedio de movimientos")
    print("4. Volver al menú principal")

def main():
    print("=== BANCO ===")
    mostrar_menu_inicio()


main()