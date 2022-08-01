import requests
import random

url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"

http_rsp = requests.get(url)

# Si imprimo la responde esto me va mostrar el status de la responde
print(http_rsp)

# Necesitamos ocnvertirlo a json para tener una lista con los diccionarios
print(http_rsp.json())
print(type(http_rsp.json()))

for book in http_rsp.json():
    print(f"Book name: {book['name']}")
    print(f"Book city: {book['city']}")
    print("\n")


# -------------------------------------------------------------------------------------------------------

class Novela:

    def __init__(self, nombre, origen):
        self.nombre = nombre
        self.origen = origen
        self.__id = random.randint(0, 1000000)

    def __str__(self):
        return f"\n\t~~~~~~ NOVELA ~~~~~~\n" \
               f"\tTitulo de la novela: {self.nombre}\n" \
               f"\tOrigen: {self.origen}\n"


novelas_rsp = http_rsp.json()  # Lo ocnvertimos a json porque sino Python no puede trabajar con ese formato

novelas = []

for novela in novelas_rsp:
    novela_obj = Novela(novela["name"], novela["city"])
    novelas.append(novela_obj)
    print(novela_obj)


# Menu
def user_menu():
    while True:
        print("Menú Novelas")
        print("1) Listar novelas")
        print("2) Agregar novela")
        print("3) Salir")

        opcion = input(">> ")

        if opcion == "1":
            for novel in novelas:
                print(novel)

        elif opcion == "2":
            print("\n")
            print("Ingrese los datos solicitados de la nueva novela")
            nombre_novela = input("Nombre: ")
            origen_novela = input("Ciudad de origen: ")

            novelas.append(Novela(nombre_novela, origen_novela))

            print("\n")

        elif opcion == "3":
            break

        else:
            print("\n¡¡¡Opción no válida, vuelva a intentarlo!!!\n")


user_menu()
