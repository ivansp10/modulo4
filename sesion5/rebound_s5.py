## rebound_s5##
class A:
    def __init__(self):
        print("Pertenezco a la clase A")

    def metodo_a(self):
        print("Método heredado de A")


class B:
    def __init__(self):
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")

# Construya una nueva clase C que tenga herencia múltiple de B y A respectivamente#


class C(B, A):
    def __init__(self):
        super().__init__()

    def metodo_c(self):
        print("Método es de C")


# Cree un nuevo objeto C#
objeto_c = C()
objeto_c.metodo_a()
objeto_c.metodo_b()
objeto_c.metodo_c()
