# Ejercicio 5 | cities

eeuu = {
    "country": "Estados Unidos",
    "cities": ['New Your', 'Miami'],
    "currency": "U$s",
    "language": "Ingles"
}

costa_rica = {
    "country": "Costa Rica",
    "cities": ['San Jose', 'Santa Teresa'],
    "currency": "CRC",
    "language": "Español"
}

mexico = {
    "country": "Mexico",
    "cities": ['Acapulco', 'DF'],
    "currency": "MX",
    "language": "Español"
}

countrys = [eeuu, costa_rica, mexico]
suecia_ok = False
df_exist = False
vist_cities = []

for country in countrys:
    if country['country'] == 'Suecia':
        suecia_ok = True

    for city in country['cities']:
        vist_cities.append(city)
        if city == 'DF':
            print(f"La ciudad DF existe en destinos a visitar - {city}")

print(f"Existe Suecia: {suecia_ok}")
print(f"Todas las ciudades a visitar: \n {vist_cities}")

# ---------------------------------------------------------------------------------------------------------
print("\n----------------------------------")
# Get: https://www.w3schools.com/python/ref_dictionary_get.asp
# .get(key) : devuelve el valor que está "guardado" en esa key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

# ¿Cual es la diferencia entre pedir un valor a traves de una clave con el get y hacerlo a traves de []?

# La diferencia es que si le pido una key que no existe, el get() devuelve un mensaje/valor (el cual hay que
# pasarle como 2do argumento) mientras que si lo hago con [] va a devolver un error
a = car.get("price", "No se sabe el precio")

print(a)

try:
    car["price"]
except Exception as e:
    print("Error de tipo:", type(e).__name__)
else:
    print(car["price"])

# Borrar elementos de lista: podemos buscar el indice del elemento que queremos borrar, y despues
# pasar ese indice por un pop para que lo borre
