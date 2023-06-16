import csv


class Vehiculo:
    def __init__(self, marca, modelo, numRuedas):
        self.marca = marca
        self.modelo = modelo
        self.numRuedas = numRuedas

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.numRuedas} Ruedas"

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_numRuedas(self):
        return self.numRuedas

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_numRuedas(self, numRuedas):
        self.numRuedas = numRuedas

    def imprimir(self):
        return f" Marca: {self.marca},Modelo: {self.modelo},{self.numRuedas} Ruedas"

    def guardar_datos_csv(self, nombre_archivo):
        if not nombre_archivo.endswith('.csv'):
            raise ValueError(
                "El nombre del archivo debe tener la extensión .csv")
        archivo = open(nombre_archivo, "a")
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()

    def leer_datos_csv(self, nombre_archivo):
        try:
            vehiculos = []
            archivo = open(nombre_archivo, "r")
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
            archivo.close()
            return vehiculos
        except FileNotFoundError:
            print("No se pudo encontrar o abrir el archivo:", nombre_archivo)
