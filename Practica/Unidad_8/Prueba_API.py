import requests

url = "https://api.spoonacular.com/recipes/complexSearch"

params = {"apiKey": "bebbf46b8c6c4453b8b051dfca6f3f73", "diet": "vegetarian"}
# La apikey te la pide la api como autorizacion

# https://api.spoonacular.com/recipes/complexSearch?apiKey=...&diet=vegetarian
# separado /: path
# separado ? y &: query

request_url = requests.get(url, params=params)
json = request_url.json() # te devuelve el json de lo que pediste

print(json)

# 1- Url base (sin parametros)
# 2- Params
# 3- request.get
# 4- json
