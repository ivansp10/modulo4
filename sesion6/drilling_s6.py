## Drilling sesion 6##

usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}
id_usuario = '004'

try:  # imprimir clave#
    print(usuarios[id_usuario])

except KeyError:  # en caso de KeyError agregar nueva clave##
    print("La clave no esta en el diccionario.Añadiendo clave...")
    usuarios[id_usuario] = "Ninguno"
    print(usuarios)
