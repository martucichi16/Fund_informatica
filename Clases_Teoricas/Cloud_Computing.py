import requests

# Clase 11

# On-premise: servicios en la infraestructura de la empresa

# Link:

url = "http://www.google.com"
response = requests.get(url)

print("Respuesta: ", response)
print("Tipo: ", type(response))

# C:/Users/user/Desktop/Martu/index_google.html
# Poner en el buscador y trae ell archivo html del url

status_code = response.status_code

print("Estado: ", status_code)
# Este numero da informacion acerca de la request
# 200 = funciono

# Ejemplo:
# if status_code == 200:
#   ...
# else:
#   ...

if status_code == 200:
    content = response.content
    print(content)
else:
    print("Error en la solicitud")

# URI = estructura, URL = especifico de una direccion

# Estructura de la url:
# http://server/query
# ?clave=valor
# &clave=valor
# &clave=valor

# http o https es el protocolo con el que se escribe y depende de si está encriptado o no
# server = maquina donde está guardado la información/data del servidor y brinda servicio todo el tiempo
#
# A veces dentro de ese & habrá un apikey o token --- Depende de cada api, lo indica en la documentacion de la api

# ---------------------------------------------------------------------------------------------------------------------
# APIs de terceros

url_api = "https://newsapi.org/v2/top-headlines?country=ar&apiKey=5d468ee9e76840978b4ac9b7bf8f240e"

response_api = requests.get(url_api)

estado_api = response_api.status_code
print("Estado: ", estado_api)

json = response_api.json()

print(json)

print("Cantidad de articulos:", json["totalResults"])

articulos = json["articles"]

for articulo in articulos:
    print(articulo["title"])


# Parametros para el llamado de la API
# Existe una mejor manera de "armar" la url, dado que es mas claro, a traves del uso de parametors

url_sin_params = "https://newsapi.org/v2/top-headlines"
args = {"country": "ar", "apiKey": "5d468ee9e76840978b4ac9b7bf8f240e"}

response_params = requests.get(url_sin_params, params=args)

url_completa = response_params.url

print("URL completa: ", url_completa)

# Usar url_completa (armado con args) funciona de la misma manera que si usaramos la url del principio


# -------------------------------------------------------------------------------------------------------------------
