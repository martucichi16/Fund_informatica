# Ejercicio 2
# lista = "array"
vehiculos = {"moto": 10,
             "auto": 20,
             "camioneta": 25,
             "camion": 60,
             "camion_con_acoplado": 90,
             "emmett_brown": 200
             }


def print_ticket(categoria_vehiculo):
    try:
        precio = vehiculos[categoria_vehiculo]
        print("Imprimiendo...")
        print(f"Vehiculo {categoria_vehiculo.upper()}; tarifa: ${precio}\n")
    except KeyError:
        print(f"No se encontro la categoria {categoria_vehiculo}")


def user_menu():
    while True:
        print("Opciones:")
        print("\t1) Moto")
        print("\t2) Auto")
        print("\t3) Camioneta")
        print("\t4) Camion")
        print("\t5) Camion con acoplado")
        print("\t6) Emmett Brown")
        print("(De querer cerrar el programa ingresar \"quit\")\n")

        option = input(">> ")

        if option == "1":
            print_ticket("moto")

        elif option == "2":
            print_ticket("auto")

        elif option == "3":
            print_ticket("camioneta")

        elif option == "4":
            print_ticket("camion")

        elif option == "5":
            print_ticket("camion_con_acoplado")

        elif option == "6":
            print_ticket("emmett_brown")

        elif option == "quit":
            break

        else:
            print("Opción no valida\n")


user_menu()

# Plantearlo con "vehiculos" como lista de diccionarios, donde el diccionario sea
# {"categoria": ..., "precio": ...}

# En este programa pudimos "ordenar" mejor el codigo:
# -Solo dejamos en el contexto global la variable "vehiculos"
# -Evitamos repetir codigo gracias a las funciones
