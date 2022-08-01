# Clase 9
# Encapsulamiento
"""
class GalletitaVariable:
    chispas_chocolates = False
    metodo_productivo = "Lotes"

    def __init__(self, sabor, color):  # constructor
        self.sabor = sabor
        self.color = color

        print(f"Nueva galletita: Sabor {self.sabor}, color {self.color}")

    def __obtenerMetodoProductivo(self):
        return metodo_productivo

Si llamamos "galletita.__obtenerMetodoProductivo()" no va a retornar nada porque es un metodo privado, por lo que no
podemos acceder al mismo
"""

# ---------------------------------------------------------------------------------------------------------------------
# Herencia -- GitHub (Magui)


# overriding = sobre escritura
# override = sobreescribir: heredas un metodo pero lo "volves" a definir, es decir, defino un metodo con el mismo nombre
# Si lo reescribo, por orden de ..., primero se tiene en cuenta lo definido en la subclase y despues a la clase padre

# Ej.: vehiculo
class Vehiculo:
    def __init__(self, velMaxima, nroRuedas, marca, modelo):
        self.velMaxima = velMaxima
        self.nroRuedas = nroRuedas
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return '''
            vehiculo {:10} {:10}, de {:1} ruedas y que llega a una
            velocidad máxima de {:>3} km/h 
        '''.format(self.marca, self.modelo, self.nroRuedas, self.velMaxima)


miVehiculo1 = Vehiculo(100, 4, "Chevolet", "Tracker")

miVehiculo2 = Vehiculo(50, 2, "Olmo", "Wish")

print(str(miVehiculo1))
print(str(miVehiculo2))


# La clase vehiculo será la clase padre y ahora definimos dos clases que heredarán sus atributos y metodos

# 1) Para esto al definir la clase hija, pasamos por parentesis el nombre de la clase padre

# 2) Al momento de definir el CONSTRUCTOR de auto vamos a heredar algunos de los atributos de la clase padre, a traves
# del "super().metodo_a_heredar" e indicandole el metodo y los atributos quue heredaria
# Notese que dentro del __init__ de la subclase agregamos "cilindrada" y "motor", atributos especificos de la clase
# hijo, por lo que las definimos por fuera del metodo super


class Auto(Vehiculo):
    def __init__(self, velMaxima, nroRuedas, marca, modelo, cilinrada, motor):
        super().__init__(velMaxima, nroRuedas, marca, modelo)
        self.cilindrada = cilinrada
        self.motor = motor

    def __str__(self):
        agergo = '''
            con una cilindrada de {} y motor de {}.
        '''.format(self.cilindrada, self.motor)
        return super().__str__() + agergo

    def avanzar(self):
        print("[Vehiculo      ]: Estoy Avanzando el Vehículo")


miAuto = Auto(100, 4, "Chevolet", "Tracker", 1.2, "Naftero")
print(str(miAuto))

# Como podemos ver los objetos que son instancias de la clase Auto heredaron lo definido en __str__ del vehiculo, con
# el agregado de imprimir los datos de motor y cilindrada (atributos de la subclase Auto)

# ---------------------------------------------------------------------------------------------------------------------
# Polimorfismo
# EJ.: __self__ porque varia con cada objeto
# Ej.: funcion definida por nosotros -- avanzar, la incorporamos a la clase auto


class Auto(Vehiculo):
    def __init__(self, velMaxima, nroRuedas, marca, modelo, cilinrada, motor):
        super().__init__(velMaxima, nroRuedas, marca, modelo)
        self.cilindrada = cilinrada
        self.motor = motor

    def __str__(self):
        agergo = '''
            con una cilindrada de {} y motor de {}.
        '''.format(self.cilindrada, self.motor)
        return super().__str__() + agergo

    def avanzar(self):
        print("[Vehiculo Auto ]: Se debe apretar el acelerador")


# Estamos overriding (reescribiendo) una funcion definida anteriormente en la superclase
# En este caso podriamos ver cómo todas las subclases de Vehiculo tendrán la funcion avazar pero será "personalizada",
# , lo que a su vez puede verse como que la funcion avanzar toma diversas formas

class Bicicleta(Vehiculo):

    def __init__(self, velMaxima, nroRuedas, marca, modelo,
                 rodado, tipo):
        super().__init__(velMaxima, nroRuedas, marca, modelo)
        self.rodado = rodado
        self.tipo = tipo

    def __str__(self):
        agergo = '''
            es una bici rodado {} y de tipo {}.
        '''.format(self.rodado, self.tipo)
        return super().__str__() + agergo

    def avanzar(self):
        print("[Vehiculo Bici ]: Se debe pedalear")


etios = Auto("260 km", 4, "Toyota", "El Etios", 1496, "1,5 L")

bici = Bicicleta("40 km", 2, "isjfi", "nefn", "inef", "ion")

print(str(etios))
etios.avanzar()
bici.avanzar()


print("\n")
# ---------------------------------------------------------------------------------------------------------------------
# Hay una funcion que nos permite verificar si un objeto es instancia de una clase: isinstance(objeto, clase)

print("¿Es el Etios un auto?", "Si" if isinstance(etios, Auto) else "No")
print("¿Es el Etios una bicicleta?", "Si" if isinstance(etios, Bicicleta) else "No")


print("\n")
# Esto puede llegar a ser util para algunas funcones. Por ejemplo:

vehiculos = [etios, bici]

for vehiculo in vehiculos:
    if isinstance(vehiculo, Auto):
        print("El motor es:", vehiculo.motor)
    else:
        print("El rodado es:", vehiculo.rodado)


print("\n")
# Cuando se pasan objetos como parametros de funciones ajenas al objeto, de todas maneras se afecta sus valores
# Ejemplo:


class Articulo:
    precio = 10


def aumentar(art):
    art.precio = art.precio * 2


articulo = Articulo()
print("Precio Original:", articulo.precio)

aumentar(articulo)
print("Precio Nuevo:", articulo.precio)
