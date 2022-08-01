# Ejercicio 2
class Vehiculo:

    def __init__(self, nombre, anio, motor=None, combustible=None, ruedas=None, ruedas_sanas=True):
        self.nombre = nombre
        self.anio = anio
        self.motor = motor
        self.combustible = combustible
        self.ruedas = ruedas
        self.ruedas_sanas = ruedas_sanas

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}" \
               f"Año: {self.anio}"

    def avanzar(self):
        self.combustible -= 3
        if self.combustible <= 0 and self.ruedas_sanas:
            print("No es posible avanzar, debe cargar combustible para continuar y/o reparar las ruedas")
            self.combustible += 3
        else:
            print(f"La/El {self.__class__.__name__} está avanzando...")

    def cargar_combustible(self, carga):
        self.combustible += carga
        print(f"Se han cargado {str(carga)} al combustible1"
              f"")

    def rueda_pinchada(self):
        self.ruedas -= 1
        self.ruedas_sanas = False
        print("Se actualizó la informacion del vehiculo")

    def reparar_ruedas(self):
        if not self.ruedas_sanas:
            self.ruedas += 1
            self.ruedas_sanas = True
            print("La rueda ha sido reparada exitosamente")
        else:
            print("Las ruedas del vehiculo están en buen estado, no necesitan reparación")


class Auto(Vehiculo):

    def __init__(self, nombre, anio, modelo, motor, ruedas, puertas, combustible, ruedas_sanas):
        super().__init__(nombre, anio, motor, combustible, ruedas, ruedas_sanas)
        self.modelo = modelo
        self.puertas = puertas

    def __str__(self):
        return f"Nombre: {self.nombre}" \
               f"\nAño: {self.anio}" \
               f"\nModelo: {self.modelo}" \
               f"\nMotor: {self.motor}" \
               f"\nRuedas: {str(self.ruedas)}" \
               f"\nPuertas: {str(self.puertas)}" \
               f"\nCombustible: {str(self.combustible)}\n" \
               f"Estado de las ruedas: {'No necesitan reparacion' if self.ruedas_sanas else 'Necesitan reparacion'}"


class Moto(Vehiculo):

    def __init__(self, nombre, anio, modelo, motor, ruedas, combustible, ruedas_sanas):
        super().__init__(nombre, anio, motor, combustible, ruedas, ruedas_sanas)
        self.modelo = modelo

    def __str__(self):
        return f"Nombre: {self.nombre}" \
               f"\nAño: {self.anio}" \
               f"\nModelo: {self.modelo}" \
               f"\nMotor: {self.motor}" \
               f"\nRuedas: {str(self.ruedas)}" \
               f"\nCombustible: {str(self.combustible)}\n" \
               f"Estado de las ruedas: {'No necesitan reparacion' if self.ruedas_sanas else 'Necesitan reparacion'}"


class Velero(Vehiculo):

    def __init__(self, nombre, anio, pies, palo_mayor, motor, combustible):
        super().__init__(nombre, anio, motor, combustible)
        self.pies = pies
        self.palo_mayor = palo_mayor

    def __str__(self):
        return f"Nombre: {self.nombre}" \
               f"\nAño: {self.anio}" \
               f"\nPies: {str(self.pies)}" \
               f"\nMotor: {self.motor}" \
               f"\nPalo mayor: {self.palo_mayor}" \
               f"\nCombustible: {str(self.combustible)}"

    def rueda_pinchada(self):
        print("El velero no tiene ruedas, por lo que no es posible haber pinchado un neumatico")

    def reparar_ruedas(self):
        print("Al no tener ruedas, el velero no necesita ninguna reparacion")


class Bicicleta(Vehiculo):

    def __init__(self, nombre, anio, tipo, cambios, ruedas, ruedas_sanas):
        super().__init__(nombre, anio, ruedas, ruedas_sanas)
        self.tipo = tipo
        self.cambios = cambios

    def __str__(self):
        return f"Nombre: {self.nombre}" \
               f"\nAño: {self.anio}" \
               f"\nTipo: {self.tipo}" \
               f"\nCambios: {'Si' if self.cambios else 'No'}" \
               f"\nRuedas: {str(self.ruedas)}\n" \
               f"Estado de las ruedas: {'No necesitan reparacion' if self.ruedas_sanas else 'Necesitan reparacion'}"

    def avanzar(self):
        print(f"La/El {self.__class__.__name__} está avanzando...")

    def cargar_combustible(self, carga=None):
        print("La bici no necesita combustible")


mi_auto = Auto("Etios", "2018", "Etios", "L1,5", 4, 4, 0, True)

mi_bicicleta = Bicicleta("Bici", "2010", "Playera", True, 2, True)

mi_moto = Moto("motito", "2015", "Lucky Lion", "220", 2, 5, True)

mi_velero = Velero("hola", "2022", 20, "xd", "jnr", 10)

mis_vehiculos = [mi_auto, mi_bicicleta, mi_moto, mi_velero]

# -----------------------------------------------------------------------------------------------------------------
# Menu


def main_menu():

    while True:
        print("Seleccione el vehiculo a utilizar")
        print("0) Salir")
        print("1) Auto")
        print("2) Bicicleta")
        print("3) Moto")
        print("4) Velero")

        try:
            opcion_vehiculo = int(input(">>> "))

        except ValueError:
            print("Valor no valido, por favor ingrse alguno de los numeros en las opciones")

        else:
            if opcion_vehiculo == 0:
                break

            else:
                while True:
                    print("\n¿Qué quiere probar del vehiculo seleccionado?")
                    print("1) Caracteristicas del vehiculo")
                    print("2) Avanzar")
                    print("3) Cargar combustible")
                    print("4) Reportar rueda pinchada")
                    print("5) Arreglar rueda")
                    print("De querer elegir otro vehiculo ingrese \"quit\"")

                    opcion_metodo = input(">>> ")

                    if opcion_metodo == "1":
                        print("\n")
                        print(mis_vehiculos[opcion_vehiculo - 1])  # Definir un __str__ para cada clase

                    elif opcion_metodo == "2":
                        print("\n")
                        mis_vehiculos[opcion_vehiculo - 1].avanzar()

                    elif opcion_metodo == "3":

                        if opcion_vehiculo == 2:
                            mis_vehiculos[opcion_vehiculo - 1].cargar_combustible()

                        else:
                            print("\nIngrese cuanto combustible quiere cargar al Vehiculo:")
                            carga_combustible = int(input(">>> "))
                            mis_vehiculos[opcion_vehiculo - 1].cargar_combustible(carga_combustible)

                    elif opcion_metodo == "4":
                        print("\n")
                        mis_vehiculos[opcion_vehiculo - 1].rueda_pinchada()

                    elif opcion_metodo == "5":
                        print("\n")
                        mis_vehiculos[opcion_vehiculo - 1].reparar_ruedas()

                    elif opcion_metodo == "quit":
                        print("\n")
                        break

                    else:
                        print("Opcion no valida")


main_menu()
