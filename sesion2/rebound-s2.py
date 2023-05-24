class Animal:
    def __init__(self, Nombre, Raza, Edad, Peso):
        self.Nombre = Nombre
        self.Raza = Raza
        self.Edad = Edad
        self.Peso = Peso


## Crear dos objetos de la clase Animal##


caballo = Animal("Zeus", "Pura sangre", "5 años", "450 kg")
print(caballo.Raza)
print(caballo.Edad)
print(caballo.Peso)
print(caballo.Nombre)


leon = Animal("Boulder", "10 años", "Atlas", "130 kg")
print(leon.Edad)
print(leon.Raza)
print(leon.Nombre)
print(leon.Peso)
