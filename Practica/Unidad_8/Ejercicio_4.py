"""
import requests

class Videojuego:

    def __init__(self, nombre, deal_id):
        self.nombre = nombre
        self.deal_id = deal_id

    # def obtener_mejor_deal(self):



def buscar_deal(nombre_juego):
    url_game = "https://www.cheapshark.com/api/1.0/games"
    args = {"title": nombre_juego}

    try:
        response = requests.get(url_game, args)

        return response["cheapestDealID"]



    except:
        print("No se ha encontrado el juego solicitado")


def info_deal(deal_id):
    url_deal = "https://www.cheapshark.com/api/1.0/deals"
    args = {"dealID": deal_id}

    try:
        response = requests.get(url_deal, args)

        return f"Titulo: {response['title']}" \
               f"\nPrecio normal: {response['normalPrice']}" \
               f"\nPrecio de la oferta: {response['salePrice']}"

    except:
        print("Hubo un error al buscar el deal solicitado")


# --------------------------------------------------------------------------------------------------------
# Menu

def menu():
    while True:
        print("¡¡¡Bienvenido a nuestro startup de deals de videojuegos!!!")
        print("A continuacion se despliega el menu de opciones")
        print("Ingrese el nombre del juego a buscar, y de desear cerrar el programa ingrese \"salir\"")

        game_title = input(">> ")

        if game_title == "salir":
            print("Cerrando el programa...")
            break

        else:
            deal = buscar_deal(game_title)
            print(info_deal(deal))


menu()
"""
