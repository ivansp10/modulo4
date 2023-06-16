while True:
    try:
        edad = int(input("Ingresa tu edad: "))

        if edad >= 18:
            print("Eres adulto")
        else:
            print("No eres un adulto")
        break
    except ValueError:
        print("Debes ingresar un numero entero")
