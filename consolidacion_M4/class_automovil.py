from class_vehiculo import Vehiculo


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numRuedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numRuedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f",{self.velocidad} Km/h, {self.cilindrada} cc"

    def get_velocidad(self):
        return self.velocidad

    def get_cilindrada(self):
        return self.cilindrada

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada

    def imprimir(self):
        return super().imprimir() + f",{self.velocidad} Km/h, {self.cilindrada} cc"
