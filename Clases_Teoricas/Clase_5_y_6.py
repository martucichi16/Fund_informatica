# Funciones
# Las funciones son fragmentos de código que se pueden ejecutar múltiples
# veces gracias a un nombre único que las identifica. Además, pueden recibir y devolver información
# para comunicarse con el proceso principal
# Definir una funcion:
"""
def nombre_de_la_funcion():
    instrucciones_a_ejecutar
"""


def saludar():
    print("Hola, Estoy saludando desde la funcion")


saludar()


# El nombre de las funciones deberia de ser descriptivo

# Las variables que se definen dentro de una función existen sólo dentro de la misma. Estas se llaman
# VARIABLES LOCALES

def inicializar():
    print("Inicializando...")
    numero = 25
    print("Valor dentro de la funcion:", numero)


print("\nDefinimos una variable local (dentro de la funcion) llamada \"numero\"")
print("Si intento imprimir la variable \"numero\" por fuera de la funcion voy a tener un error porque es una variable"
      " local:")
try:
    print(numero)
except Exception as e:
    print(e)

# A pesar de que las variables locales y globales son distitnas, y si están llamadas iguales se pueden
# seguir utilizando, lo mejor es no repetir los nombres de la variables

# return: al ejecutarlo la función no sólo devuelve el valor sino que además finaliza su ejecución

print("\n------------------------------------------------")
# -------------------------------------------------------------------------------------------------------------
'''
Clase 6 (Continuacion de funciones)

-Las funciones reciben ARGUMENTOS // PARAMETROS
(Dif argumento y parametro ¿?)

CONTEXTOS
- Locales: solo dentro de la funcion
- Globales: es "accesible" en todo el programa

- Shadow: definis variables locales con mismo nombre que la global, pero en el contexto local la variable local hace
"sombra" a la global y el programa usa esa

-Lo mejor para las funciones es que el codigo de las mismas dependa de los argumentos que le pasamos y no tome
valores globales

Pseudocodigo: "borrador" de codigo

-ABSTRACCION
-ENCAPSULAMIENTO: mirada general y local, codigo global y local

-Programacion procedural: bloque de codigo enorme
-Programacion modular: dividir el codigo total en modulos, hacer pruebas unitarias, articular con otros bloques
de codigo
-Programacion Orienteda a Objetos --- encapsulamiento + pruebas unitarias e integrales


'''


# Usar las funciones dentro de "otras funciones"
def dias_semana():
    return ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]


print("La funcion devuelve:", dias_semana())

print("\nA traves del uso de [] puedo pedir solo algunos de los elementos que devuelve la funcion")
print("Habiles:", dias_semana()[0:5])
print("No habiles:", dias_semana()[-2:])

# Al usar la funcion en otras funciones, podemos ver que trabaja con lo que esa funcion retorna
print("\n------------------------------------------------")


# Una función podría devolver múltiples valores separados por coma
# + Se puede asignar mas de una variable en una misma linea

def fun_calc(a, b):
    return a + b, a - b, a * b, a / b


suma, resta, multiplicacion, division = fun_calc(2, 2)

print("Resultado suma:", suma)
print("Resultado resta:", resta)
print("Resultado multiplicacion:", multiplicacion)
print("Resultado division:", division)

print("\n------------------------------------------------")


# Existe la posibilidad de ponerle NOMBRE a cada parámetro y luego utilizar estos nombres,
# permitiendo esto ingresar parametros sin la necesidad de respetar el orden de los parametros como
# nosotros lo definimos
def calcular_impuesto(importe, tasa):
    return tasa * importe / 100


print("Resultado usando parametros respetando el orden:", calcular_impuesto(importe=100000, tasa=100))
print("Resultado usando parametros sin respetar el orden:", calcular_impuesto(tasa=100, importe=100000))

print("\n------------------------------------------------")


# En el caso de usar la funcion pero no pasarle algun parametro, la funcion da un error porque no puede ejecutar
# las instrucciones que se le han dado

# Para solucionar eso podemos definir un argumento default o un "valor por defecto" que sera utilizado si al usar la
# funcion no se ingresan datos para ese parametro
def calcular_tax(importe, tasa=10):
    return tasa * importe / 100


print("Le pasamos ambos parametros:", calcular_tax(importe=100000, tasa=21))

print("Si no se le ingresa la tasa, usa el valor por defecto:", calcular_tax(importe=100000))

# Como podemos ver, si recibe un valor para "tasa" utiliza ese valor (en el primer caso el 21), pero si no se le
# ingresa un valor para ese parametro, va a calcular un impuesto del 10%

print("\n------------------------------------------------")


# Los casos vistos hasta ahora trataban ARGUMENTOS RECIBIDOS POR VALOR, los cuales al modificar el
# valor en la función, no modifica el de la variable enviada. Era el caso de definir una variable global y
# pasarla como argumento: la funcion retornaria la variable "modificada", pero la variable original global
# no se modificaba

# Tambien se pueden recibir los ARGUMENTOS POR REFERENCIA, que implica trabajar sobre el dato original y modificarlo

def cuadrado_de_elementos(lista):
    for elemento in range(len(lista)):
        lista[elemento] = lista[elemento] ** 2
    return


# Las funciones pueden tener return o no, y devolver algo o no
# Por ejemplo, podemos hacer una funcion que solo modifique a una variable

# El return solo corta con la funcion pero no devuelve nada, va a modificar la lista que le pasamos como argumento
# y despues de la funcion cada elemento va a quedar elevado al cuadrado

primeros = [1, 2, 3, 4, 5]
print("Lista antes de la funcion:", primeros)

cuadrado_de_elementos(primeros)
print("Lista despues de la funcion:", primeros)

print("\n------------------------------------------------")


# ~PARAMETROS ITERABLES~
# Si ponemos un * delante del nombre del argumento, eso significa que podes pasarle la cantidad que quieras de
# argumentos
def indeterminados(*args):
    for arg in args:
        print(f"Argumento: {arg} // type: {type(arg)}")
    return


print("~Funcion con parametros iterables y sin nombre~")
indeterminados("Hola", 4625, True, [1, 2, 3])


# Con ** podemos, despues de definir la funcion, usarla pasandoles argumentos con nombre. Esto de debe a que, al usar
# los ** el tipo de dato a devolver va a ser un diccionario
def diccio(**args):
    print("Argumento:", args)
    print(type(args))
    return


print("\n~Funcion con parametros iterables y con nombre~")
diccio(producto="caramelo", precio=10, stock=2000)

'''
Idea para hacer ejercicio 5

def fun_login(user, password):

def fun_salir():
    cuenta = {
    user = ""
    password = ""

while True:
    user = input("Ingresar ID")
    password = input("Ingrese contraseña")

    cuenta = fun_login(user, password)
    if cuenta != {}:
        opcion = input("Ingrese una opcion...")
        while opcion >= 1 and opcion <= 6:
            if opcion == 1:
                fun_acreeditar_ca(cuenta)
            elif opcion == 2:
                
            elif opcion == 3:
                fun_saldo_ca(cuenta)
            ...
            else: (opcion 6):
                fun_salir()
                break
'''
