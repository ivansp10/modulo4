from class_vehiculo import Vehiculo
from class_automovil import Automovil
from class_auto_part import Particular
from class_auto_carga import Carga
from class_bici import Bicicleta
from class_moto import Motocicleta
import csv

#### Parte 1####


num_vehiculos = int(input("Cuantos Vehículos desea insertar: "))
vehiculos = []
for i in range(num_vehiculos):
    print(f"Datos del automóvil {i+1}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    num_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en Km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))
    vehiculo = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
    vehiculos.append(vehiculo)

print("Imprimiendo por pantalla los vehículos:")
contador = 0
for i in vehiculos:
    contador = contador+1
    print(f"Datos del automóvil {contador}:{i}")

### Parte 2##
# agregando e imprimiendo las instancias solicitadas#
print("*"*70)
particular = Particular("Ford", "Fiesta", "4", "180", "500", 5)
print(particular.imprimir())

carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
print(carga.imprimir())

bicicleta = Bicicleta("Shimano", "MT Ranger", "2", "Carrera")
print(bicicleta.imprimir())

motocicleta = Motocicleta("BMW", "F800s", 2, "CARRERA", 21, "DOBLE VIGA", "4T")
print(motocicleta.imprimir())

print("*"*70)

#### verificar la relacion que existe entre motocicleta y las demas clases###
print(f"Motocicleta es instancia con relación a Vehiculo:",
      isinstance(motocicleta, Vehiculo))

print(f"Motocicleta es instancia con relación a Automovil:",
      isinstance(motocicleta, Automovil))

print(f"Motocicleta es instancia con relación a Automóvil Particular:",
      isinstance(motocicleta, Particular))

print(f"Motocicleta es instancia con relación a Automóvil Carga:",
      isinstance(motocicleta, Carga))

print(f"Motocicleta es instancia con relación a Bicicleta:",
      isinstance(motocicleta, Bicicleta))

print(f"Motocicleta es instancia con relación a Motocicleta:",
      isinstance(motocicleta, Motocicleta))

### parte 3 ###
particular.guardar_datos_csv("vehiculos.csv")
carga.guardar_datos_csv("vehiculos.csv")
bicicleta.guardar_datos_csv("vehiculos.csv")
motocicleta.guardar_datos_csv("vehiculos.csv")

print("*"*70)
automoviles = particular.leer_datos_csv("vehiculos.csv")

for auto in automoviles:
    print(auto)
