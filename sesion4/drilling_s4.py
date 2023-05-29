## Desarrollo drilling_s4##

# creando clase Persona#
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        print("Estado:Caminando")

# creando subclases Maratonista y Ciclista  #


class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self):
        print("Estado:Trotando")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self):
        print("Estado:Rodando")


persona_1 = Persona("Juan")
maratonista_1 = Maratonista("Pedro")
ciclista_1 = Ciclista("Carlos")

print(persona_1.__dict__)
print(maratonista_1.__dict__)
print(ciclista_1.__dict__)
persona_1.movimiento()
maratonista_1.movimiento()
ciclista_1.movimiento()
