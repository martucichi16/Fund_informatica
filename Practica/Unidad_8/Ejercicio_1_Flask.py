from flask import Flask, jsonify

# Ejercicio 1

admin = {"ID": "4566541", "nombre": "Pepe", "apellido": "Gutierrez", "Role": "admin", "telefono": "1164859778",
         "ultimo_ingreso": "12/06/22"}

app = Flask(__name__)

@app.route("/api/admin", methods=["GET"])
def info_admin():
    return jsonify(admin)
