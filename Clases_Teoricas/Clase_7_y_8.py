# Funciones recursivas / Recursividad:
# Funciones que se llaman a si mismas

# Ejemplo: 5! = 5*4*3*2*1
# n! = n * (n-1)!

# En el factorial podemos ver que el factorial de n está definido por otro factorial, el factorial del munero
# anterior (n-1)
# Esto podemos verlo en la programacion como "recursividad"

# ¿Para que hariamos una funcion recursiva?
# Porque hay problemas que se resulven de manera mucho mas sencilla con esta estructura

# Ejemplo 1
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


print("El factorial de 5 es", factorial(5))

# Lo que hace la funcion factorial es lo siguiente:
# 1) factorial(5) = 5 * factorial(4)
# 2) factorial(4) = 4 * factorial(3)
# 3) factorial(3) = 3 * factorial(2)
# 4) factorial(2) = 2 * factorial(1)
# 5) factorial(1) = 1
# Entonces queda: 5 * (4 * (3 * (2 * (1))))

print("\n-------------------------------")


# Ejemplo 2

def bomba(n):
    if n > 0:
        print(n)
        bomba(n - 1)
    else:
        print("BOMBAAAAAAAAAAAAAA!!!")


bomba(5)

# Podriamos cometer un error al definir una funcion recursiva y hacerla "infinita". Necesito una condicion de salida


print("\n-----------------------------------")


def buscar(n, lista):
    if len(lista) == 1:
        if lista[0] == n:
            return True
        else:
            return False

    return buscar(n, lista[0:1]) or buscar(n, lista[1:])


mi_lista = [7, 1, 3, 8, 4]
encontro = buscar(8, mi_lista)

print(encontro)

print("\n-----------------------------------")
# ---------------------------------------------------------------------------------------------------------------------
'''
Clase 8: PROGRAMACION ORIENTADA A OBJETOS
Cambio de paradigma: cambio en la forma de pensar

-Objetos que comparten funcionalidades o caracteristicas, pueden "clasificarse" en clases

--------------------------------------------------------------------------------------------------------------------
1) ABSTRACCION: informacion basica para representar un modelo, se lo abstrae para definirlo de manera simplificada
Ej.: si queremos definir un perro podriamos definir como caracteristicas suyas su color, tamaño, raza y pelaje.
Podria tener más caracteristicas que lo hagan más especifico, pero elegimos lo más representativo
Acciones: ladrad, caminar, correr, dormir ---> Metodos

"Perro" es la clasificacion más amplia, y despues podria definir razas
Perro = clase, razas = instancias (objetos "pertenecientes" a la clase)

Un objeto puede ser una instancia de una clase, y quiere decir que ese objeto pertenece a la clase instanciada

--------------------------------------------------------------------------------------------------------------------
2) ENCAPSULAMIENTO: implica esconder algunos de sus atributos y métodos
Lo que nos interesa --- publico
Lo que no nos interesa --- privado

Para esconder se tiene que escribir __ : __metodo o __atributo

--------------------------------------------------------------------------------------------------------------------
3) POLIMORFISMO: la accion se adapta a cada forma de objeto particular que pertenece a una clase
Ej.: clase -- transporte / objetos --- caballo, auto, avion / acciones --- avanzar y frenar
-Cada vehiculo tendra una manera "personalizada" de avanzar y frenar

"Nos permite realizar distintas acciones en función al tipo de objeto, aún cuando dicha acción 
conceptualmente sea la misma (y por lo tanto posee el mismo nombre)"

--------------------------------------------------------------------------------------------------------------------
4) HERENCIA: "La herencia nos brinda la capacidad de extender parte de la funcionalidad de una clase madre hacia una 
clase hija (o heredada), así como también sus atributos"

Existen clases padre/super clase y subclasses/clases heredadas
-Las subclases de la clase padre heredan los atributos y metodos de su clase padre

Por ejemplo, si la clase padre es transporte y sus metodos son avanzar y frenar, al definir a la subclase bicileta,
esta ya hereda los metodos / acciones avanzar y frenar sin necesidad de volverlos a definir

--------------------------------------------------------------------------------------------------------------------
La POO nos permite modelizar cada uno de estos elementos en clases, definiendo sus atributos y métodos (abstracción). 
Al programar generaremos instancias de cada uno de ellos y estableceremos cómo se comunican y relacionan

'''


# Como definir una clase?
class Galletita:
    sabor = "Dulce"
    color = "Negro"
    chispas_chocolate = False


# Definir un objeto:
mi_galletita = Galletita()
print("Mi galletita es de sabor", mi_galletita.sabor)

mi_galletita.sabor = "Salado"  # Le estas cambiando el valor al atributo "sabor"
print("Mi galletita es de sabor", mi_galletita.sabor)

# También se le puede agregar nuevos atributos al OBJETO, no a la clase
mi_galletita.tamanio = "Mediano"
print("Mi galletita es de tamaño", mi_galletita.tamanio)

print("\n")


# Acciones en la clase = metodo
class Galletita2:
    sabor = "Dulce"
    color = "Negro"
    chispas_chocolate = False

    def cambiar_sabor(self):  # El self representa al objeto al que le aplicaremos el metodo
        if self.sabor == "Dulce":
            self.sabor = "Salado"
        else:
            self.sabor = "Dulce"


cookie = Galletita2()
print("En principio el sabor de la galletita es", cookie.sabor)
print("Le podemos cambiar el valor del atributo sabor")

cookie.cambiar_sabor()
print("El nuevo sabor de la galletita es", cookie.sabor)

print("\n")
galleta = Galletita2()
galleta.sabor = "Salado"
print("En principio el sabor de la galletita es", galleta.sabor)

galleta.cambiar_sabor()
print("El nuevo sabor de la galletita es", galleta.sabor)

print("\n")


# Metodo CONSTRUCTOR: se definira siempre con __init__. A pesar de no invocarlo se ejecuta siempre que se insatncie
# una clase
class Galletita3:
    sabor = "Dulce"
    color = "Negro"
    chispas_chocolate = False

    def __init__(self):
        print("Se acaba de crear una galletita")


una_galletita = Galletita3()

print("\n")


# Por lo general el constructor se usa para pedir los valores que van a tomar los atributos del objeto

# Destructor: saca un objeto de la "memoria" (definido en la clase)
# print(del(galle))

# Método especial = __string__: permite re definir la funcion default de str, para poder llamar al objeto y que en
# consola se imprima algo entendible y legible (si uno hace print(objeto) en consola se muestra la ubicacion de memoria
# donde está guardado el mismo)


class GalletitaVariable:
    chispas_chocolates = False

    def __init__(self, sabor, color):  # constructor
        self.sabor = sabor
        self.color = color

        print(f"Nueva galletita: Sabor {self.sabor}, color {self.color}")

    def __del__(self):
        print(f"Se ha borrado la galletita de sabor {self.sabor}")

    def __str__(self):
        print(f"Galletita sabor {self.sabor}")


galle = GalletitaVariable("Salado", "Negra")
galle2 = GalletitaVariable("Dulce", "Marron")


print("\n")
str(galle)

print("\n")
del galle
