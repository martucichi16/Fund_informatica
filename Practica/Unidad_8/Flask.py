# Flask - framework, modulo de python --> lo vamos a usar para crear apis (hay muchos pero vamos a usar flask)
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello", methods=['GET'])  # anotations, definimos una ruta
# El valor de la ruta es lo que esta en comillas "/", y despues vienen los metodos de http
# Cada vez que alguien ejecute un get con nuestro "endpoint", muestra la funcion de abajo
def hello_world():
    return "<p>Hello, World!</p>"


# Cuando le damos al run devuelve un servidor, creamos un servidor local, que va a estar esperando solicitudes
# Devuelve: Running on http://127.0.0.1:5000 --- LOCAL HOST = mi maquina
# Puerto: cada servidor tiene definidos diferentes puertos. Dentro de mi local host, el "puerto" al que quiero llegar,
# el que quiero solicitar

# Como acceder a la data?


# Si probamos http://localhost:5000 en Postman, nos devuelve la funcion
# Si intentamos llamarlo con otro metodo que no sea el get no va a funcionar
# En la consola nos va a mostrar todos los llamados que se hicieron al servidor

rsp = [{
        "id": 123,
        "name": "Mike",
        "is_alive": True,
        "favourite_sports": ["cycling", "tennis", "swiming"],
        "graduated": None
    }]


# Para devolver la estructura de rsp como un json tengo que convertirlo (porque por ejemplo el True en json es true o
# el None es null). Eso lo hacemos a traves de jsonify
@app.route("/person", methods=["GET"])
def person():
    return jsonify(rsp)


@app.route("/create", methods=["POST"])
def create_person():
    # "request" es lo que le pasamos por el body en Postman
    body = request.json
    rsp.append(body)

    return f"{body['name']} ha sido agregado al registro de personas"
