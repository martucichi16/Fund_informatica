# Unidad 3: Estructura de Datos

# TUPLAS:
mis_frutas = ('manzana', 'mandarina', 'naranja')
print("La tupla contiene:", mis_frutas)

print("El indice de la futa mandarina es:", mis_frutas.index("mandarina"))

frutas = ("mandarina", "frutilla", "pera", "mandarina")
print("La tupla frutas contiene", frutas)

print("La fruta mandarina se repite", frutas.count("mandarina"), "veces")

print("\n----------------------------")
# Buscar github en YouTube (cómo subir archivo)


# Conjuntos
lista = [9, 12, 9, 36, 22, 12]
conjunto = set(lista)
lista_2 = list(conjunto)


# Lista de diccionarios
articulos = []

articulo_1 = {"nombre": "chicle", "precio": 10, "stock": 1500}
articulos.append(articulo_1)

articulo_2 = {"nombre": "alfajor", "precio": 40, "stock": 300}
articulos. append(articulo_2)

articulo_3 = {"nombre": "caramelo", "precio": 2, "stock": 10000}
articulos.append(articulo_3)

print(articulos)

# Dos maneras de recorrer las claves valor de un diccionario

# 1) for clave, valor in diccio.items():
# 2) for fruta in diccio:
#           print(fruta, "--", diccion[fruta])

print("\n----------------------------")
# --------------------------------------------------------------------------
# Unidad 4: Entradas y salidas
# dato = input()
dato = "hola"  # mock --- para agilizar asignas lo que pones en la consola directo en la variable
# mientras seguis programando y una vez que terminas se puede borrar esta linea y a la del input
# sacarle el #
print(dato)

# nombre = input("Por favor ingrese su nombre: ")
nombre = "Jose"
print("Bienvenido ", nombre)
print('Hola {n}!, bienvendo '.format(n=nombre))

# Todo lo que se ingresa en la consola se toma como un string


# Conversion de tipo de datos
numero_1 = input("Ingres un numero:")
numero_2 = input("Ingrese otro numero:")

print("Suma =", numero_1, "+", numero_2)
print("Resultado = ", int(numero_1) + int(numero_2))
