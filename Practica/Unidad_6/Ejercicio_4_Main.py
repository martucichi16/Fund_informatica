from Ejercicio_4_Clases import Cliente
from Ejercicio_4_Clases import TarjetaDebito
from Ejercicio_4_Clases import TarjetaCredito

category_gold = "GOLD"
category_platinum = "PLATINUM"
category_black = "BLACK"

dc = TarjetaDebito("1522 1255 1201 0012 3256", category_platinum, "04/05", "08/24", "007")
cc = TarjetaCredito("1522 1255 1201 0012 3256", category_platinum, "04/05", "08/24", "007", 10000)

cliente = Cliente("Martina", "Cichi", 44816202, 1139585826, "Rosales 143", category_platinum, dc)
# print(cliente.id)

print(cliente)

cliente.agregar_tarjeta_credito(cc)

print(cliente)


# Definir el menu
def backoffice():
    print("~~~ BANCO DIGITAL ~~~")
    print("A continuacion ingrese los datos solicitados del nuevo cliente")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    documento = input("Documento: ")
    telefono = input("Telefono: ")
    direccion_completa = input("Direccion Completa: ")
    categoria = input("Categoria: ")

    client = Cliente(nombre, apellido, documento, telefono, direccion_completa, categoria)

    while True:
        print("\nMenú del cliente:")
        print("1) Mostrar la informacion del cliente creado")
        print("2) Agregar tarjeta de debito")
        print("3) Agregar tarjeta de credito")
        print("4) Acceder a info. de la tarjeta de debito")
        print("5) Acceder a info. de la tarjeta de credito")
        print("6) Modificar categoria")
        print("7) Aumentar limite de compra de la tarjeta de credito")
        print("8) Cancelar la tarjeta de credito")
        print("9) Dar de baja al cliente")
        print("[Si se quiere salir del programa ingrese \"salir\"]\n")

        opcion = input(">>> ")

        if opcion == "1":
            print("\n")
            print(client)

        elif opcion == "2":
            print("\nIngrese la informacion solicitada acerca de la nueva tarjeta de debito")
            numero = input("Numero: ")
            categoria = input("Categoria: ")
            emision = input("Fecha de emision: ")
            vencimiento = input("Fecha de vencimiento: ")
            cod_seguridad = input("Codigo de seguridad: ")

            t_debito = TarjetaDebito(numero, categoria, emision, vencimiento, cod_seguridad)

            client.agregar_tarjeta_debito(t_debito)

        elif opcion == "3":
            print("\nIngrese la informacion solicitada acerca de la nueva tarjeta de debito")
            numero = input("Numero: ")
            categoria = input("Categoria: ")
            emision = input("Fecha de emision: ")
            vencimiento = input("Fecha de vencimiento: ")
            cod_seguridad = input("Codigo de seguridad: ")
            limite_compra = int(input("Limite de compra: "))

            t_credito = TarjetaCredito(numero, categoria, emision, vencimiento, cod_seguridad, limite_compra)

            client.agregar_tarjeta_credito(t_credito)

        elif opcion == "4":
            print(client.tarjeta_debito)

        elif opcion == "5":
            print(client.tarjeta_credito)

        elif opcion == "6":
            nueva_categoria = input("Ingrese la nueva categoria: ")
            client.modificar_categoria(nueva_categoria)
            print("La categoria ha sido 2"
                  "modificada exitosamente")

        elif opcion == "7":
            client.aumentar_limite_credito()

        elif opcion == "8":
            client.cancelar_tc()

        elif opcion == "9":
            client.baja()

        elif opcion == "salir":
            print("Finalizacion del programa")
            break

        else:
            print("Opcion invalida")


print("\n")
print("\n------------------------------------------------------------------------")
backoffice()
