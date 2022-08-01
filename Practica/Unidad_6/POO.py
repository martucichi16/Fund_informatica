# Programación Orientada a Objetos (POO): modelo de cómo podemos representar la realidad

# Todo puede expresarse como un objeto: definiendo propiedades y acciones -- ABSTRACCION

# El self es necesario siempre que definamos algo relacionado al objeto o clase, y debe ir al principio

# El método “__init__()”, le dice a Python como generar un objeto cuando instanciamos la clase, y se lo denomina el
# "constructor" de la clase

# Los nombres de las clases de escriben en CamelCase o PascalCase, por convención, comenzando la primera letra de cada
# palabra siempre en mayúscula

# Warm up
class Ballena:

    def __init__(self, nombre, edad, sexo, peso, mamifero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero

    def nadar(self):
        return f"{self.nombre} está nadando..."

    def saltar(self):
        return f"{self.nombre} está saltando..."

    def alimentarse(self):
        return f"{self.nombre} se está alimentando..."

    def descansar(self):
        return f"{self.nombre} está descansando ... zZz"

    def estado(self):
        return f"Estado de la ballena:" \
               f"\n\tNombre: {self.nombre}" \
               f"\n\tEdad: {self.edad}" \
               f"\n\tSexo: {self.sexo}" \
               f"\n\tPeso: {self.peso}" \
               f"\n\tEs mamifero: {'SI' if self.mamifero else 'NO'}"


# Los métodos son funciones pero se las llaman métodos por pertener a una clase y ser "especificos" de esa clase

# crear un objeto de una clase es denominado INSTANCIACIÓN
willy = Ballena("Willy", 9, "M", 2000, True)
willy_clone = Ballena("Willy", 9, "M", 2000, True)

print(willy)  # Devuelve la "direccion" donde está guardada la variable en la memoria
print(f"La ballena llamada {willy.nombre} tiene {willy.edad} años y pesa {willy.peso} kgs")
# Al crear un objeto estamos "instanciando" una clase

print(willy.nadar())
print(willy.saltar())
print(willy.alimentarse())
print(willy.descansar())

print("\n", willy.estado())

print("\n")
print(willy.nombre == willy_clone.nombre)
print(willy == willy_clone)
# A pesar de tener los mismos datos (atributos) no son lo mismo, porque cada objeto es "unico" y se guarda en un
# lugar especifico, distintos entre los distintos objetos

# -------------------------------------------------------------------------------------------------------------------
# Clase 2 POO
# Ejemplo de plomorfismo

# La "firma" del metodo (la linea en la que se define) es la misma, pero el desrrollo/funcionalidad es distinto

# Herencia y polimorfismo


class Animal:

    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        print("Guau")


class Gato(Animal):
    def hablar(self):
        print("Miau")


class Leon(Animal):
    def hablar(self):
        print("Roar")

# La clase "hija" hereda el metodo de la clase padre "Animal" pero al definir cada subclase se reescribe (
# override) el metodo = polimorfismo


dog = Perro()
cat = Gato()
lion = Leon()

animals = [dog, cat, lion]

for animal in animals:
    animal.hablar()

print("\n")
# ------------------------------------------------------------------------------------------------------------------
# Clase 03 POO - 24/05/22

# Encapsulamiento
# Publico: lo puede acceder cualquiera y por fuera de la clase

# Privado: sive para que una persona (usuario) que manipula el objeto no puede cambiar al metodo o atributo
# privado
# Si es privado no se puede acceder al mismo POR FUERA de la clase, pero si DENTRO, es decir, podemos definir
# metodos que accedan a él

# Protegido: es privado en la super clase y cuando se hereda es publico


class Auto:

    def __init__(self, marca, modelo) -> None:  # la flecha muestra qué retorna el metodo
        self.marca = marca
        self.modelo = modelo
        self.__velocimetro = 10
        self.__codigo_motor = "JASBD4587345"
        # self._combustible = 0

    def __str__(self):
        return f"{self.marca}, {self.modelo}"

    def get_velocidad(self):
        return self.__velocimetro

    def get_codigo_motor(self):
        return self.__codigo_motor


auto = Auto("Ford", "Focus")
print(auto.marca)
print(auto)  # al haber definido el string, cuando hacemos el print hace lo definido en el __str__
# Esto porque la funcion print busca el metodo str, porque está definido asi. Cuando nosotros definimos
# el __str__ en la funcion, en realiad  estamos rescribiendo el metodo str definido por el lenguaje para las clases
