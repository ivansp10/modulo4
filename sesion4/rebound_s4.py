### Desarrollo rebound_s4###

# crear clase libro#
class Libro:
    pass


# creación instancia libro_1
libro_1 = Libro()
libro_1.autor = "Dan Brown"
libro_1.titulo = "Infierno"

# creación instancia libro_2
libro_2 = Libro()
libro_2.autor = "Dan Brown"
libro_2.titulo = "El Código Da Vinci"
libro_2.ann_de_publicacion = "2003"

# resultado
print(libro_1.__dict__)
print(libro_2.__dict__)
