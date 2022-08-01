# Ejercicio 1

class Restaurante:

    def __init__(self, nombre, gastronomia, horarios, menu, is_open=False):
        self.nombre = nombre
        self.tipo_gastronomia = gastronomia
        self.is_open = is_open
        self.open_daily = horarios
        self.menu = menu

    def describe_restaurante(self):
        print(f"El restaurante {self.nombre} sirve comida de tipo {self.tipo_gastronomia}")

    def open_restaurante(self):
        print("¡¡¡El restaurante está abierto al público!!!")
        self.is_open = True

    def close_restaurante(self):
        print(f"Lo lamentamos pero el restaurante {self.nombre} ha cerrado.")
        self.is_open = False

    def see_menu(self):
        print(f"Menu del restaurante {self.nombre}")
        for plato in self.menu:
            print("\t-", plato)


fabric = Restaurante("Fabric", "oriental", "De 12:00 hs a 00:00hs", ["Rolls", "Tiraditos", "Rollito primavera"])

museo_del_jamon = Restaurante("El museo del jamón", "española", "De 9:00hs a 23:00hs", ["Tortilla de papa",
                              "Mejillones al ajillo", "Casuela de mariscos"])

juanito = Restaurante("Juanitos", "mexicana", "De 20:00hs a 2:00hs", ["Tacos", "Burrito", "Quesadilla"])

restaurantes = [fabric, museo_del_jamon, juanito]


def main_menu():

    while True:

        print("Elija un restaurante:")

        print("0) Salir")

        numero_opcion = 1
        for restaurante in restaurantes:
            print(f"{str(numero_opcion)}) {restaurante.nombre}")
            numero_opcion += 1

        try:
            option = int(input(">>> "))

        except ValueError:
            print("Opcion invalida")

        else:

            if option == 0:
                break

            elif option <= len(restaurantes):

                print(f"\nLa gastronomia del restaurante {restaurantes[option-1].nombre} se caracteriza por comida "
                  f"{restaurantes[option-1].tipo_gastronomia} y en este momento se encuentra "
                  f"{'abierto' if restaurantes[option-1].is_open else 'cerrado'}")

                while True:
                    print("\n¿Qué más quiere saber sobre el restaurante?")
                    print("1) Horarios")
                    print("2) Menu")
                    print("De querer salir del restaurante ingrese \"salir\"")

                    option_2 = input(">>> ")

                    if option_2 == "1":
                        print("\n", restaurantes[option - 1].open_daily)

                    elif option_2 == "2":
                        print("\n")
                        restaurantes[option - 1].see_menu()

                    elif option_2 == "salir":
                        print("\n")
                        break

                    else:
                        print("Opción no válida")

            else:
                print("\nOpcion no valida, vuelva a intentarlo\n")


museo_del_jamon.open_restaurante()

main_menu()

laundry = Restaurante("The Laundry", "americana", "20:00hs a 2:00hs", ["Hamburgesa americana", "Papas con cheddar",
                       "Hamburguesa veggie"])

restaurantes.append(laundry)

print("\nSe ha agregado un nuevo restaurante y nuestro menú se actualizó")
main_menu()
