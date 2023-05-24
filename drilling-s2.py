#### Drilling sesion 2#####

## clase persona##
class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

### getters###
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellidos

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad

    def get_estatura(self):
        return self.estatura

    def get_peso(self):
        return self.peso

    ### setters###
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def set_estatura(self, estatura):
        self.estatura = estatura

    def set_peso(self, peso):
        self.peso = peso

## creacion de dos objetos##


Persona_1 = Persona('Pedro', 'Vivas', 'Masculino',
                    '20 años', '1.78 mts', '68 kg')
Persona_2 = Persona('Juan', 'Camargo', 'Masculino',
                    '18 años', '1.8 mts', '75 kg')

### modificacion de edad Persona_1###
Persona_1.set_edad('21 años')
print(Persona_1.get_edad())

### modificacion de apellido Persona_2###
Persona_2.set_apellidos('Santiago')
print(Persona_2.get_apellido())
