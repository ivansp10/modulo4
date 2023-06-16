from class_automovil import Automovil


class Particular(Automovil):
    def __init__(self, marca, modelo, numRuedas, velocidad, cilindrada, numPuesto):
        super().__init__(marca, modelo, numRuedas, velocidad, cilindrada)
        self.numPuesto = numPuesto

    def __str__(self):
        return super().__str__() + f"Número de puestos: {self.numPuesto}"

    def get_numPuesto(self):
        return self.numPuesto

    def set_numPuesto(self, numPuesto):
        self.numPuesto = numPuesto

    def imprimir(self):
        return super().imprimir()+f",Número de puestos: {self.numPuesto}"
