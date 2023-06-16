from class_automovil import Automovil


class Carga(Automovil):
    def __init__(self, marca, modelo, numRuedas, velocidad, cilindrada, pesoCarga):
        super().__init__(marca, modelo, numRuedas, velocidad, cilindrada)
        self.pesoCarga = pesoCarga

    def __str__(self):
        return super().__str__()+f",Peso carga: {self.pesoCarga} kg"

    def get_pesoCarga(self):
        return self.pesoCarga

    def set_pesoCarga(self, pesoCarga):
        self.pesoCarga = pesoCarga

    def imprimir(self):
        return super().imprimir()+f",Peso carga: {self.pesoCarga} kg"
