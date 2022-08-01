# Ejercicio 3
ordenes = []

while True:
    print("\nFarmacia - Opciones")
    print("\t1) Agregar")
    print("\t2) Listar")
    print("\t3) Salir")

    option = input("\nEliga una opcion:\n>> ")

    if option == "1":
        print("\nNombre del medicamento")
        medicamento = input(">> ")

        print("Nombre del laboratorio")
        lab = input(">> ")

        print("Cantidad")
        cantidad = input(">> ")

        item = {}

        item["medicamento"] = medicamento
        item["laboratorio"] = lab
        item["cantidad"] = cantidad

        ordenes.append(item)

    elif option == "2":
        print(ordenes)

    elif option == "3":
        break

    else:
        print(f"La opcion {option} es incorrecta, vuelva a intentarlo")

# No hacemos el try / except porque ya lo salvamos con el else
