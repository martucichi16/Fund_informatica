# Ejercicio 4
lavanderia = []
precio_por_prenda = 3
# debe ser fácil de cambiar en el futuro

while True:
    print("Elija opcion:")
    print("\t1) Lavanderia")
    print("\t2) Recepcion")
    print("(De querer finalizar el programa ingrese \"quit\")")
    opcion = input(">> ")

    if opcion == "quit":
        break

    elif opcion == "1":
        print("\nNumero de habitacion:")
        habitacion = input(">> ")

        print("Cantidad de prendas:")
        cant_prendas = input(">> ")

        print("Fecha de servicio:")
        fecha = input(">> ")

        item = dict()
        item["numero_de_habitacion"] = habitacion
        item["cantidad_de_prendas"] = cant_prendas
        item["fecha_de_servicio"] = fecha

        lavanderia.append(item)
        print("\n")
    else:
        print("\nElija opcion:")
        print("\ta) Buscar informacion de huesped")
        print("\tb) Eliminar huesped de lavanderia")

        opcion_recepcion = input(">> ")

        if opcion_recepcion == "a":
            print("\nNumero de habitacion a buscar:")
            hab_buscada = input(">> ")
            total_prendas = 0
            servicios_ofrecidos = 0
            info_huesped = {}
            for servicio in lavanderia:
                if servicio["numero_de_habitacion"] == hab_buscada:
                    total_prendas += int(servicio["cantidad_de_prendas"])
                    servicios_ofrecidos += 1
                else:
                    continue

                info_huesped["habitacion"] = hab_buscada
                info_huesped["precio"] = precio_por_prenda
                info_huesped["servicios"] = servicios_ofrecidos
                info_huesped["total_a_cobrar"] = total_prendas * precio_por_prenda

            print(info_huesped)
            print("\n")
        else:
            print("\nNumero de habitacion a eliminar:")
            hab_buscada = input(">> ")

            lavanderia_2 = []
            for servicio in lavanderia:
                if servicio["numero_de_habitacion"] != hab_buscada:
                    lavanderia_2.append(servicio)

            lavanderia = lavanderia_2
            print(f"Los servicios de la habitacion {hab_buscada} han sido eliminados de la lista de tickets "
                  f"de lavanderia")
            print(f"Tickets actualizados: {lavanderia}")

            print("\n")
