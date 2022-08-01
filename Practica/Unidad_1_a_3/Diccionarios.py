# Estructuras de datos

# Datos como str, int o float son datos primitivos
# En cambio las estructuras de datos ya son más complejas

# DICCIONARIOS: colección de key-values (clave-valor), donde cada key tiene asociado un valor
# Puede tener infinitas clave-valor

diccionario = {"clave1": "valor1", "clave2": "valor2"}

print("Los diccionarios se componen siempre de la siguiente manera:", diccionario)
print("Se le puede pedir valores a traves de la clave:", diccionario["clave1"])

print("\n-------------------------------------")
# Los diccionarios suelen escribirse separando las claves-valor en distintas lineas:
martina = {"nombre": "Martina",
           "edad": 18,
           "altura": 1.62,
           "peso": "53 kg."}

print(martina["edad"])
martina["dni"] = 44816202
print("Se le puede agregar una clave-valor:", martina)

# Agregar lo del pdf

# METODOS
# diccionario.values(): devuelve una lista de los valores del diccionario, sin las claves
print("A través del método .values() podemos acceder a los valores del diccionario:", martina.values())

# diccionario.keys(): devuelve una lista de las claves del diccionario, sin los valores
print("A través del método .keys() podemos acceder a las claves del diccionario:", martina.keys())

# diccionario.items(): devuelve una lista de
print("Con .items() obtenemos una lista de tuplas con cada clave y valor:\n", martina.items())

# diccionario.get(): es una manera alternativa de pedirle un valor a traves de su clave (ver archivo Ej_5...)
print("Ademas de poder obtener un valor escribiendo diccionario[key] podemos hacerlo a través del "
      "método .get():",  {martina.get("edad")})


print("\n------------------------------------------------------")

# Ejercicio 1 --> recorrer diccionarios
usuario = {"nombre": "Luis",
           "apellido": "Rodriguez",
           "dni": "31549875",
           "rol": "asistente",
           "sucursal": "005"}

print("Diccionario \"usuario\":", usuario)
print("\n---------------------------")

for data in usuario.items():
    if data[0] == "dni":
        print(f"{data[0].upper()}: {data[1].title()}")
    else:
        print(data[0].title(), ":", data[1].title())
print("---------------------------")


# Otra manera de hacerlo y mucho más clara:
for key, value in usuario.items():
    if key == "dni":
        print(f"{key.upper()}: {value.title()}")
    else:
        print(f"{key.title()}: {value.title()}")
print("---------------------------\n")

# Nombrar todas las variables con minuscula

# Ejercicio 2
animals_lista = ["perro", "gato", "hamster"]  # MUTABLES
animals_tupla = ("paloma", "cacatua", "loro")  # INMUTABLES
animals_conjunto = {"tigre", "pantera", "leon"}  # En ingles los conjuntos se llaman sets; no se repiten
animals_dicc = {"pez": "fish", "elefante": "elephant", "delfin": "dolphin"}  # En otros lenguajes los llaman mapas


print("Iniciamos con la LISTA de animales")
print("La lista contiene:", animals_lista, type(animals_lista))
animals_lista.append("python")
print("Le pudimos agregar un nuevo elemento:", animals_lista)
print("\n")


print("Seguimos con la TUPLA de animales")
print("La tupla contiene:", animals_tupla, type(animals_tupla))
print("Las tuplas son inmutables, por lo que no se le puede agregar elementos")
print("\n")


print("Seguimos con el CONJUNTO de animales")
print("El conjunto contiene:", animals_conjunto, type(animals_conjunto))
animals_conjunto.add("python")
print("Le pudimos agregar un nuevo elemento con el .add() (lo agrega en un lugar random):\n", animals_conjunto)
animals_conjunto.add("python")
animals_conjunto.add("python")
animals_conjunto.add("python")
print("Si queremos añadir un elemento que está repetido, no se va a volver a agregar:\n", animals_conjunto)
print("\n")


print("Terminamos con el DICCIONARIO de animales")
print("El diccionario contiene:", animals_dicc, type(animals_dicc))
animals_dicc["piton"] = "python"
print("Le pudimos agregar un nuevo clave-elemento:", animals_dicc)
print("\n")

print("----------------------------------------------------")

# Ejercicio 3 --> ya lo resolvimos en el punto 1

# Ejercicio 4
encuesta = {'anonimo1': '6', 'anonimo2': '9', 'anonimo3': '5', 'anonimo4':
            'x', 'anonimo5': 'x', 'anonimo6': '8', 'anonimo7': '3',
            'anonimo8': '10', 'anonimo9': '4', 'anonimo10': '5', 'anonimo11':
            'x', 'anonimo12': '2', 'anonimo13': '7', 'anonimo14': '5',
            'anonimo15': '2', 'anonimo16': '8', 'anonimo17': '10'}

no_contestaron = 0
encuesta_limpia = {}
for key, value in encuesta.items():
    if value == "x":
        no_contestaron += 1
    else:
        encuesta_limpia[key] = value

print(f"Los empleados que no contestaron fueron {no_contestaron}")
print(f"Nueva encuesta, solo con respuestas: {encuesta_limpia}")
print(f"La cantidad que respondieron fueron: {len(encuesta_limpia)} personas")


suma_respuestas = 0
for value in encuesta_limpia.values():
    suma_respuestas += int(value)  # Si le cambias el tipo de dato se llama "casting"

print(f"Suma de las respuestas: {suma_respuestas}")

# Siempre que vayamos a usar variables generales hay que definirlas en el head, no arriba de la funcion en
# la que la voy a usar

nota_maxima = 10
print(f"Porcentaje de aceptación: {(suma_respuestas / (len(encuesta_limpia) * nota_maxima)) * 100} %")

# Ultima parte del ejercicio: usar set, que lo va a convertir en un conjunto, y por ende no va a haber repeticiones
# Tratar terminar los ejercicios

numeros_de_valoracion1 = set()

for value in encuesta_limpia.values():
    numeros_de_valoracion1.add(value)

print(numeros_de_valoracion1)
numeros_de_valoracion2 = sorted(numeros_de_valoracion1)
print(f"Los numeros de valoracion fueron {numeros_de_valoracion2}")


print("\n---------------------------")
# Ejercicio 5
paises_a_visitar = {"Estados Unidos": {"cities": ["New York", "Chicago"], "currency": "dólar estadounidense",
                                       "lenguage": "english"},
                    "Costa Rica": {"cities": ["San Jose", "Heredia"], "currency": "colón", "lenguage": "spanish"},
                    "México": {"cities": ["Tijuana", "Guadalajara", "DF"], "currency": "peso mex",
                               "lenguage": "spanish"},
                    "Canadá": {"cities": ["Toronto", "Vancouver"], "currency": "dolar canadiense",
                               "lenguage": "english"},
                    "Alemania": {"cities": ["Berlin", "Hamburgo", "Frankfurt"], "currency": "euro",
                                 "lenguage": "german"},
                    "Francia": {"cities": ["Paris", "Niza"], "currency": "euro", "lenguage": "french"},
                    "Suiza": {"cities": ["Zurich", "Ginebra"], "currency": "franco suizo", "lenguage": "french"},
                    "España": {"cities": ["Madrid", "Barcelona", "Murcia"], "currency": "euro", "lenguage": "spanish"},
                    "Italia": {"cities": ["Roma", "Venecia"], "currency": "euro", "lenguage": "italian"}}

# seria mejor armar una lista de diccionarios, poniendo como parte de las keys "country" y que su valor sea el
# nombre del pais

print("¿Queremos visitar Suecia?:", "Suecia" in paises_a_visitar.keys())
print("¿Queremos visitar Madrid?:", "Madrid" in paises_a_visitar["España"]["cities"])

ciudades = []
for key, value in paises_a_visitar.items():
    for city in value["cities"]:
        ciudades.append(city)

print(f"Ciudades a visitar: {ciudades}")


no_existe = True
pais_a_buscar = "Australia"
for key, value in paises_a_visitar.items():
    if key == pais_a_buscar:
        print(pais_a_buscar, value)
        no_existe = no_existe and False
    else:
        no_existe = no_existe and True

if no_existe:
    print(f"{pais_a_buscar} no está en el listado de paises a visitar")
# ¿Como hacerlo con el get()?

del(paises_a_visitar["Estados Unidos"])
print(f"Listado actualizado: {paises_a_visitar}")


print("\n---------------------------")
# Ejercicio 6
cards_trx = [{'user_id': '35465', 'total_amount': 30000, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 7},
            {'user_id': '23423', 'total_amount': 19099, 'payment_method': 'credit card', 'total_installments': 12,
             'current_installment': 3},
            {'user_id': '82312', 'total_amount': 15500, 'payment_method': 'credit card', 'total_installments': 12,
             'current_installment': 4},
            {'user_id': '29332', 'total_amount': 90200, 'payment_method': 'credit card', 'total_installments': 6,
             'current_installment': 4},
            {'user_id': '82231', 'total_amount': 29000, 'payment_method': 'credit card', 'total_installments': 12,
             'current_installment': 9},
            {'user_id': '76289', 'total_amount': 42300, 'payment_method': 'credit card', 'total_installments': 12,
             'current_installment': 11},
            {'user_id': '58092', 'total_amount': 18900, 'payment_method': 'credit card', 'total_installments': 6,
             'current_installment': 1},
            {'user_id': '30943', 'total_amount': 13520, 'payment_method': 'debit card'},
            {'user_id': '75230', 'total_amount': 67000, 'payment_method': 'credit card', 'total_installments': 6,
             'current_installment': 4},
            {'user_id': '20582', 'total_amount': 21500, 'payment_method': 'credit card', 'total_installments': 12,
             'current_installment': 6},
            {'user_id': '10943', 'total_amount': 5200, 'payment_method': 'debit card'},
            {'user_id': '29002', 'total_amount': 9000, 'payment_method': 'credit card', 'total_installments': 12,
             'current_installment': 11},
            {'user_id': '92389', 'total_amount': 39200, 'payment_method': 'debit card'},
            {'user_id': '12772', 'total_amount': 65700, 'payment_method': 'credit card', 'total_installments': 12,
             'current_installment': 10},
            {'user_id': '72879', 'total_amount': 7300, 'payment_method': 'credit card', 'total_installments': 6,
             'current_installment': 5},
            {'user_id': '83489', 'total_amount': 44000, 'payment_method': 'debit card'}]

customer_payments = ['23423', '58092', '75230', '72879', '82231', '35465', '30943', '12772']

print(f"El current installment del usuario {cards_trx[1].get('user_id')} es {cards_trx[1].get('current_installment')}")

for card in cards_trx:
    if card["payment_method"] == "debit card":
        continue
    else:
        if card["user_id"] in customer_payments:
            card["current_installment"] += 1

'''
Con for dentro de for (ciclo anidado):

for card in cards_trx:
    if card["payment_method"] != "debit card":
        if card["user_id"] in customer_payments:
            card["current_installment"] += 1
'''

print(f"Despues del pago, el current installment del usuario {cards_trx[1].get('user_id')} es "
      f"{cards_trx[1].get('current_installment')}")

print("\n")
remaining_installment = 0

for card in cards_trx:
    if card["payment_method"] == "debit card":
        continue
    else:
        print(f"User {card['user_id']}: {card['total_installments'] - card['current_installment']} cuotas")
        remaining_installment += card['total_installments'] - card['current_installment']

print(f"El total de cuotas que restan pagar entre todos los clientes son {remaining_installment}")

'''
Hacerlo poniendo cada deuda en una lista:

remaining_installment = []
for n in cards_trx:
    if n["payment_method"] != "debit card":
        cuotas_a_pagar = {}
        cuotas_a_pagar["user id " + n["user_id"]] = (n["total_installments"] - n["current_installment"])
        remaining_installment.append(cuotas_a_pagar)
print(remaining_installment)
'''

print("\n")
paid_user_ids = []
for card in cards_trx:
    if card["payment_method"] == "debit card":
        continue
    else:
        if card["total_installments"] == card["current_installment"]:
            paid_user_ids.append(card["user_id"])

print(f"Usuarios sin deuda: {paid_user_ids}")


print("\n---------------------------")
# Ejercicio 7
numeros = []

# con for
for numero in range(1, 100):
    if (numero % 2) == 0:
        numeros.append({"number": numero, "type": "par"})
    else:
        numeros.append({"number": numero, "type": "impar"})

print(numeros)
print(f"\n(for) Los primeros 3 elementos de mi lista de diccionarios de numeros son:\n{numeros[:3]}")

print("\n")
# con while
nums = []
num = 1
while num <= 100:
    if (num % 2) == 0:
        nums.append({"number": num, "type": "par"})
        num += 1
    else:
        nums.append({"number": num, "type": "impar"})
        num += 1

print(f"(while) Los primeros 3 elementos de mi lista de diccionarios de numeros son:\n{nums[:3]}")

# Investigación
# Import math: Python has a set of built-in math functions, including an extensive math module, that allows you to
# perform mathematical tasks on numbers.
# https://www.w3schools.com/python/python_math.asp

# random?
