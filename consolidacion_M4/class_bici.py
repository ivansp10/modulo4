from class_vehiculo import Vehiculo
from excepciones import Error_Tipo_Ingresado


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numRuedas, tipo):
        super().__init__(marca, modelo, numRuedas)

        self.tipo = self.validar_tipo(tipo)

    def validar_tipo(self, tipo):
        if tipo.lower() == "carrera" or tipo.lower() == "urbana":
            return tipo.lower()
        else:
            raise Error_Tipo_Ingresado(
                f"El tipo de {self.__class__.__name__} debe ser carrera o urbana ")

    def __str__(self):
        return super().__str__() + f",Tipo:{self.tipo}"

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def imprimir(self):
        return super().imprimir()+f",Tipo:{self.tipo}"
