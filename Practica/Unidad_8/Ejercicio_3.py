import requests

# Ejercicio 3

url_cocktail_name = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
url_ingredient = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="
url_id = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="

# Hacerlo con parametros


def buscar_trago_nombre():
    print("\nIngrese el trago a buscar")
    trago = input(">> ").lower()

    url_search_cocktail = url_cocktail_name + trago

    response = requests.get(url_search_cocktail)

    print(response.json())


# Busqué margarita y mojito y funciono, pero como hago para saber los targos que existen?


def buscar_por_ingrediente():
    print("\nIngrese el ingrediente del cocktail buscar")
    ingredient = input(">> ").title()

    url_search_ingredient = url_ingredient + ingredient

    response = requests.get(url_search_ingredient)

    print(response.json())


def buscar_cocktail_id():
    print("\nIngrese el id del cocktail a buscar")
    id = input(">> ")

    url_search_id = url_id + id

    response = requests.get(url_search_id)

    print(response.json())


'''
buscar_trago_nombre()

print("\n")
buscar_por_ingrediente()

print("\n")
buscar_cocktail_id()
'''

def main_menu():
    print("Bienvenidos a nuestro bar, seleccione a continuación cómo desea llevar a cabo la busqueda de su coktail:")

    while True:
        print("1) Buscar trago segun nombre")
        print("2) Buscar trago segun ingrediente")
        print("3) Buscar trago segun id")
        print("[De querer salir del menu ingrese \"Salir\"]\n")

        option = input(">> ")

        if option == "1":
            buscar_trago_nombre()
            print("\n")

        elif option == "2":
            buscar_por_ingrediente()
            print("\n")

        elif option == "3":
            buscar_cocktail_id()
            print("\n")

        elif option.title() == "Salir":
            break

        else:
            print("Opcion no valida")


main_menu()


# ¿Cómo puedo ver toda la data de la api? Es decir, toda la lista de tragos sin aplicar ningun filtro
# Una vez que pueda obtener esa data, podria hacer que en cada funcion de busqueda se imprima solo la data importante y
# de manera más estetica (tal vez a traves de un objeto "Trago" y sobreescribiendo el __str__)

'''
Como lo habia hecho antes:

url_cocktail_name = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

def buscar_trago_nombre():
    print("\nIngrese el trago a buscar")
    trago = input(">> ").lower()

    url_search_cocktail = url_cocktail_name + trago

    response = requests.get(url_search_cocktail)

    print(response.json())
    

En lugar de agregar el trago en esta funcion, puedo definir parametros, lo cual es más claro

-Para hacer con parametros guardamos como url hasta el ?
'''
