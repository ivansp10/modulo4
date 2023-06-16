class Error_Tipo_Ingresado(Exception):
    def __init__(self, message):
        super().__init__(message)


class Error_Cuadro_Ingresado(Exception):
    def __init__(self, message):
        super().__init__(message)


class Error_Motor_Ingresado(Exception):
    def __init__(self, message):
        super().__init__(message)
