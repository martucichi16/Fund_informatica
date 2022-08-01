import requests

# APIS - Cloud Computing

# Arquitectura API RESTful

# JSON (JavaScript Object Notation): todos los lenguajes se comunican con este formato, no solo JS)
# Los objetos en JSON se escriben como los diccionarios en python

# Backend: poco amigable, hacen la funcionalidad
# Base de datos
# Frontend: diseño, interfaz con el usuario

# ¿Como se comunican las APIs? A traves de un contrato
# El contrato está definido por una request y una response
# Request:
# Response:

# Ejercicio 1
persona = {
  "nombre": "Mike",
  "apellido": "Matheu",
  "sexo": "Male",
  "edad": "53",
  "dirección": "Av. Mugga Way 934",
  "estado": "Canberra",
  "pais": "Australia",
  "gustos_musicales": ["Aerosmith", "Metalica", "Dream Theater", "Deep Purple"]
}

print(persona)
print("Tipo: ", type(persona))


# --------------------------------------------------------------------------------------------------------------------
# Ejercicio 3 express
def buscar_trago_nombre():
    print("\nIngrese el trago a buscar")
    trago = input(">> ").lower()
    response_cocktail = requests.get("http://www.thecocktaildb.com/api/json/v1/1/search.php", params={"s": trago})
    json = response_cocktail.json()

    # print(json) (*)

    print(f"Trago: {json['drinks'][0]['strDrink']}")
    print(f"Instrucciones: {json['drinks'][0]['strInstructions']}")
    print(f"Clasificacion: {json['drinks'][0]['strAlcoholic']}")


buscar_trago_nombre()

# (*) Probar en Postman: url base
