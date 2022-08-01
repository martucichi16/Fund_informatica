from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/json")
def saludo_json():
    return jsonify({"message": "Hola"})


@app.route("/texto")
def saludo_text():
    return "Hola"


# --------------------------------------------------------------------------------------------------------------------
productos = [{'Nombre': 'tensiometro', 'stock': 5},
             {'Nombre': 'termometro', 'stock': 20},
             {'Nombre': 'ibupofreno', 'stock': 500},
             {'Nombre': 'paracetamol', 'stock': 450}]


@app.route("/productos", methods=['GET'])
def productos_get():
    return jsonify({'productos': productos, 'status': 'ok'})


# Consultar un producto en especifico
'''
@app.route('/productos/<producto>', methods=['GET'])
def productoGet(producto):
    for indice, p in enumerate(productos):
        if p['Nombre'] == producto:
            return jsonify({'producto':productos[indice], 'busqueda':producto, 'status':'ok'})
        else:
            return jsonify({'productos':productos, 'status':'nof found' })
'''


# POST: subir nueva data, en este caso, subir un nuevo producto
# Hay que agregar la libreria request
# En Postman hay que poner lo que indica la ruta "http://localhost:6000/productos" con el metodo POST, y desde la
# parte de BODY seleccionar raw y formato json --- ahi se escribe el body que queremos incorporar
@app.route('/productos', methods=['POST'])
def producto_post():
    body = request.json
    nombre = body['Nombre']
    stock = body['stock']
    producto_alta = {'Nombre': nombre, 'stock': stock}
    productos.append(producto_alta)
    return jsonify({'productos': productos, 'status': 'ok'})


# PUT: actualiza la info --- en este caso buscamos un producto y actualizamos el stock
# La actualizacion de la data es igual que como el POST
@app.route('/productos', methods=['PUT'])
def producto_put():
    body = request.json
    nombre = body['Nombre']
    stock = body['stock']
    for indice, p in enumerate(productos):
        if p['Nombre'] == nombre:
            p['stock'] = stock
            return jsonify({'producto': p,
                           'busqueda': nombre,
                           'status': 'ok'})

    return jsonify({'busqueda': productos,
                    'status': 'not found'})


# DELETE: borrar algun producto
# En postman pones el metodo delete y como url "http://localhost:6000/producto_a_borrar"
@app.route('/productos/<producto>', methods=['DELETE'])
def producto_delete(producto):
    for indice, p in enumerate(productos):
        if p['Nombre'] == producto:
            productos[indice:indice+1] = []
            return jsonify({'producto': p, 'busqueda': producto, 'status': 'ok'})
    return jsonify({'productos': productos, 'status': 'nof found'})


if __name__ == '__main__':  # cambias el puerto
    app.run(debug=True, port=6000)

# En postman hay que escribir la url "http://localhost:6000" y dependiendo si le agregamos "/texto" o "/json" devuelve
# lo que definimos en esas rutas
# Lo podemos llamar con localhost o con la url que aparece en la consola

# Nª: si lo corremos con el interpete de PyCharm hay que poner el 5000, que es el default, pero si corremos el archivo
# desde la funcion donde cambiamos el puertovamos a poder llamar a la api con el nuevo puerto

# ¿Para que cambiar el numero del puerto? Porque si ponemos dos servicios en el mismo puerto van a "chocar" y no van
# a funcionar

# El cambio de puerto tiene que hacerse al final del archivo, sino no va a correr lo que quede por debajo de este
# codigo
