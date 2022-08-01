from flask import Flask, jsonify

# Ejercicio 2 y 3
employees = [
            {"ID": "456", "nombre": "Pepe", "apellido": "Gutierrez", "documento": "27845690", "fecha_ingreso":
            "12/06/22", "area": "tesoreria", "cargo": "secretario"},
            {"ID": "888", "nombre": "Alejandra", "apellido": "Perez", "documento": "34555021", "fecha_ingreso":
            "23/04/19", "area": "tesoreria", "cargo": "gerente"},
            {"ID": "640", "nombre": "Sol", "apellido": "Ruiz", "documento": "20015548", "fecha_ingreso":
            "02/10/10", "area": "impuestos", "cargo": "jefa"},
            {"ID": "954", "nombre": "Roberto", "apellido": "Sanchez", "documento": "22485000", "fecha_ingreso":
            "15/01/12", "area": "impuestos", "cargo": "gerente"},
            {"ID": "870", "nombre": "Oscar", "apellido": "Modolo", "documento": "30021145", "fecha_ingreso":
            "22/10/15", "area": "tesoreria", "cargo": "jefe"}
            ]

app = Flask(__name__)


@app.route("/api/employees", methods=["GET"])
def employees_tesoreria():
    return jsonify(employees)

