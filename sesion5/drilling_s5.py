# drilling sesion 5

## clase Persona##
class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno
## clase Departamento##


class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto


## clase trabajador que hereda de Persona y Departamento Respectivamente##
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario


trabajador = Trabajador("Juan", "Pérez", "2005",
                        "Ingeniería de software", "IS", 20000)
## imprimir los atributos##
print(trabajador.__dict__)

## verificar la instancia del trabajador con respecto a Persona,Departamento y Trabajador##
print(f"Es trabajador una instancia de Persona:",
      isinstance(trabajador, Persona))
print(f"Es trabajador una instancia de Deparatamento:",
      isinstance(trabajador, Departamento))
print(f"Es trabajador una instancia de Trabajador:",
      isinstance(trabajador, Trabajador))
