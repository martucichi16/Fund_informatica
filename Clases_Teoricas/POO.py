# Cómo crear clases y objetos en Python (video YouTube)
# https://www.youtube.com/watch?v=wfcWRAxRVBA

class Robot:
    def introduce_self(self):
        print("My name is " + self.name)

# Es necesario agregar el self como parametro en cada funcion que se crea dentro de la clase)

r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()

# ---------------------------------------------------------------------------------------------------------------
# Vamos a crear una clase Robot_pro con un constructor que nos permita definir los objetos de mandera más fácil

class Robot_pro:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

# Ahora podemos crear un objeto en una simple linea
r3 = Robot_pro("Steven", "white", 80)
r4 = Robot_pro("Hulk", "green", 200)

r3.introduce_self()