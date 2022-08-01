# Ejercicio 5

class Video:

    def __init__(self, categoria, nombre, descripcion, fecha_publicacion, director, calif_edad):
        self.categoria = categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_publicacion = fecha_publicacion
        self.director = director
        self.calif_edad = calif_edad

    def __str__(self) -> str:
        return f"Categoria: {self.categoria}" \
               f"\nNombre: {self.nombre}" \
               f"\nDescripción: {self.descripcion}" \
               f"\nFecha de publicación: {self.fecha_publicacion}" \
               f"\nDirector: {self.director}" \
               f"\nCalificación de edad: {self.calif_edad}"



class Serie(Video):

    def __init__(self, num_temporadas, categoria, nombre, descripcion, fecha_publicacion, director, calif_edad):
        super().__init__(categoria, nombre, descripcion, fecha_publicacion, director, calif_edad)
        self.numero_temporadas = num_temporadas

    def __str__(self) -> str:
        print("~~~ SERIE ~~~")
        print(f"Numero de temporadas: {self.numero_temporadas}")
        return super().__str__()

    def agregar_temporada(self):
        self.numero_temporadas += 1
        return self.numero_temporadas

class Pelicula(Video):

    def __init__(self, duracion, categoria, nombre, descripcion, fecha_publicacion, director, calif_edad):
        super().__init__(categoria, nombre, descripcion, fecha_publicacion, director, calif_edad)
        self.duracion = duracion

    def __str__(self) -> str:
        print("~~~ PELICULA ~~~")
        print(f"Tiempo de reproducción: {self.duracion}")
        return super().__str__()


# ------------------------------------------------------------------------------------------------------------------
# Main
# From Ejercicio_5.py import Video
# From Ejercicio_5.py import Serie
# From Ejercicio_5.py import Pelicula

friends = Serie(11, "comedia", "Friends", "La vida de 6 mejores amigos en Nueva York", 1990, "Gary Halvorson", "14+")

back_to_the_future = Pelicula("117 minutos", "ciencia ficción", "Back to the Future", "En un viaje al pasado, Martin "
     "McFly debe juntar a sus padres para evitar su desaparición de la existencia", "1985", "Robert Zemeckis", "ATP")


print(friends.__str__())
print("\n")
print(back_to_the_future.__str__())

print("\n")
friends.agregar_temporada()
print(friends.__str__())
