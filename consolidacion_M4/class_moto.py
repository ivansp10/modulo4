from class_bici import Bicicleta
from excepciones import Error_Cuadro_Ingresado, Error_Motor_Ingresado


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numRuedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numRuedas, tipo)
        self.nro_radios = nro_radios

        if cuadro.lower() in ["doble cuna", "multitubular", "doble viga"]:
            self.cuadro = cuadro.lower()
        else:
            raise Error_Cuadro_Ingresado(
                "El cuadro de la Motocicleta solo puede ser doble cuna, multitubular o doble viga")

        if str(motor).upper() in ["2T", "4T"]:
            self.motor = str(motor).upper()
        else:
            raise Error_Motor_Ingresado(
                "El Motor de la Motocicleta solo puede ser 2T o 4T")

    def __str__(self):
        return super().__str__()+f", Número de radios: {self.nro_radios}, cuadro: {self.cuadro}, motor: {self.motor}"

    def get_nro_radios(self):
        return self.nro_radios

    def get_cuadro(self):
        return self.cuadro

    def get_motor(self):
        return self.motor

    def set_nro_radios(self, nro_radios):
        self.nro_radios = nro_radios

    def set_cuadro(self, cuadro):
        self.cuadro = cuadro

    def set_motor(self, motor):
        self.motor = motor

    def imprimir(self):
        return super().imprimir()+f", Número de radios: {self.nro_radios}, cuadro: {self.cuadro}, motor: {self.motor}"
