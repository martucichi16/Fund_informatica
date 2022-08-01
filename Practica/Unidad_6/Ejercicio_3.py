# Ejercicio 3
class Lampara():

    def __init__(self, fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio):
        self.fabricante = fabricante
        self.codigo_fabr = codigo_fabricante
        self.amperaje = amperaje
        self.potencia = potencia
        self.diametro = diametro
        self.eficiencia_energetica = eficiencia_energ
        self.precio = precio

    def info_general(self):
        print(f"La lámpara de modelo {self.modelo}, fabricada por {self.fabricante}, tiene un diametro de"
              f" {self.diametro}cm")

    def info_precio(self):
        print(f"El precio del modelo es ${self.precio}")

    def caracteristicas_consumo(self):
        print(f"Amperaje: {self.amperaje}"
              f"\nPotencia: {self.potencia}"
              f"\nEficiencia energética: {self.eficiencia_energetica}")

    def ajuste_inflacion(self, tasa_inflacion):
        self.precio = self.precio * (1 + tasa_inflacion)
        print(f"El nuevo precio de la lámpara es {self.precio}")
        return self.precio


class NPN923(Lampara):

    def __init__(self, fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio):
        super().__init__(fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio)
        self.modelo = "NPN-923"


class NPN328(Lampara):

    def __init__(self, fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio):
        super().__init__(fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio)
        self.modelo = "NPN-328"


class NPN731(Lampara):

    def __init__(self, fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio):
        super().__init__(fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio)
        self.modelo = "NPN-731"
        self.certificado_iso = "ISO 9023"

    def certificado(self):
        print("Certificado de codigo: ", self.certificado_iso)


class NPN021(Lampara):

    def __init__(self, fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio):
        super().__init__(fabricante, codigo_fabricante, amperaje, potencia, diametro, eficiencia_energ, precio)
        self.modelo = "NPN-021"


# -------------------------------------------------------------------------------------------------------------------
# INSTANCIACION
lamp_1 = NPN923("Lyghtning SRL", "88451", 220, 220, 30, "kbsdfb", 1500)
lamp_2 = NPN328("Lyghtning SRL", "88451", 220, 220, 30, "kbsdfb", 1500)
lamp_3 = NPN731("Lyghtning SRL", "88451", 220, 220, 30, "kbsdfb", 1500)
lamp_4 = NPN021("Lyghtning SRL", "88451", 220, 220, 30, "kbsdfb", 1500)

lamp_1.caracteristicas_consumo()

lamp_2.info_general()

lamp_4.info_precio()

lamp_3.certificado()
