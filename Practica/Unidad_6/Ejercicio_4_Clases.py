# Ejercicio 4
import random

class Cliente:

    def __init__(self, nombre, apellido, documento, telefono, direcc, categoria, tarjeta_debito = None,
                 tarjeta_credito = None):
        self.id = random.randrange(10000000)
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.telefono = telefono
        self.direcc = direcc
        self.categoria = categoria
        self.tarjeta_debito = tarjeta_debito
        self.tarjeta_credito = tarjeta_credito

    def __str__(self) -> str:
        mensaje = f"Nombre completo: {self.nombre} {self.apellido}" \
              f"\nTelefono: {self.telefono}" \
              f"\nDocumento: {self.documento}" \
              f"\nDireccion completa: {self.direcc}" \
              f"\nCategoria: {self.categoria}" \
              f"\n\n--------------------TARJETAS--------------------" \
              f"\nTarjeta de Debito: {self.tarjeta_debito}" \
              f"\n"

        if self.tarjeta_credito:
            print("\n")
            mensaje = mensaje + f"Tarjeta de Crédito: {self.tarjeta_credito}"

        return mensaje

    def agregar_tarjeta_debito(self, tarjeta_debito):
        self.tarjeta_debito = tarjeta_debito

    def agregar_tarjeta_credito(self, tarjeta_credito):
        self.tarjeta_credito = tarjeta_credito

    def info_tc(self):
        print(self.tarjeta_credito)

    def info_td(self):
        print(self.tarjeta_debito)

    def modificar_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria

    def aumentar_limite_credito(self):
        if self.tarjeta_credito == None:
            print("No se ha dado de alta a ninguna tarjeta de credito")
        else:
            aumento = int(input("Ingrese el aumento del limite: "))
            self.tarjeta_credito.aumentar_limite(aumento)

    def cancelar_tc(self):
        print("Se ha eliminado la tarjeta de credito")
        self.tarjeta_credito = None

    def baja(self):  # Lo copio de Rodri
        self.tarjeta_credito = None
        self.tarjeta_debito = None


"""
Para dar de baja al cliente Rodri hizo lo siguiente:

    def suspend_client(self):
        self.is_client_active = False
        self.debit_card = None
        self.credit_card = None

    def client_state(self):
        if self.is_client_active:
            return f"Cliente activo"
        else:
            return f"Cliente numero: {self.id} esta suspendido"
"""


class Tarjeta:

    def __init__(self, numero, categoria, emision, vencimiento, codigo_seguridad):
        self.numero = numero
        self.categoria = categoria
        self.emision = emision
        self.vencimiento = vencimiento
        self.codigo_seguridad = codigo_seguridad

    def __str__(self) -> str:
        return f"Numero: {self.numero}" \
               f"\nCategoria: {self.categoria}" \
               f"\nFecha de Emision: {self.emision}" \
               f"\nFecha de Vencimeinto: {self.vencimiento}" \
               f"\nCodigo de Seguridad: {self.codigo_seguridad}"


# La palabra "super" viene de superclass y necesaria para heredar los atributos y métodos del padre

class TarjetaDebito(Tarjeta):

    def __init__(self, numero, categoria, emision, vencimiento, codigo_seguridad):
        super().__init__(numero, categoria, emision, vencimiento, codigo_seguridad)


class TarjetaCredito(Tarjeta):
    def __init__(self, numero, categoria, emision, vencimiento, codigo_seguridad, limite_compra):
        super().__init__(numero, categoria, emision, vencimiento, codigo_seguridad)
        self.limite_compra = limite_compra

    def __str__(self):
        limite = f"Limite compra: {self.limite_compra}"
        return super().__str__() + limite

    def aumentar_limite(self, aumento):
        self.limite_compra += aumento

# limite_compra lo defino en el primer renglon porque el renglon del super está heredando los
# atributos de la clase padre
