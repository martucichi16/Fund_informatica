# Ejercicio 1
class Esfera:

    def __init__(self, radio):
        self.nombre = "Esfera"
        self.radio = radio

    def get_name(self):
        return self.nombre

    def get_radio(self):
        return self.radio

    def print_properties(self):
        return f"{self.nombre} con propiedad radio {self.radio} cm"


class Cubo:

    def __init__(self, lado):
        self.nombre = "Cubo"
        self.lado = lado

    def get_name(self):
        return self.nombre

    def get_lado(self):
        return self.lado

    def print_properties(self):
        return f"{self.nombre} con propiedad lado {self.lado} cm"


class PrismaRectangular:

    def __init__(self, base, altura, profundidad):
        self.nombre = "Prisma Rectangular"
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def get_name(self):
        return self.nombre

    def get_dimensiones(self):
        return(self.base, self.altura, self.profundidad)


'''
esfera = Esfera(4)

espera.nombre = cubo

print(esfera.nombre)
   >>> cubo
   
-Para que esto no sea posible podemos hacer privado al atributo nombre
'''

# print(PrismaRectangular(4, 2, 2).get_dimensiones())
