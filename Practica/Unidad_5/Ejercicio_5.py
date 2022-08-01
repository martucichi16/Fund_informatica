# Ejercicio 5
db_movies = [{"movie": "Back to the Future", "abailability": 2},
             {"movie": "The Devil Wears Prada", "abailability": 0},
             {"movie": "My best friend´s wedding", "abailability": 8},
             {"movie": "Ghost", "abailability": 7},
             {"movie": "Scream", "abailability": 4},
             {"movie": "Top Gun", "abailability": 0},
             {"movie": "Rocky", "abailability": 5},
             {"movie": "Home Alone", "abailability": 10}]

rented_movies = []

def update_db_movies(rented_movie):
    for movie in db_movies:
        if rented_movie == movie["movie"]:
            movie["abailability"] -= 1

def rent_movie(id, movie):
    has_rented = False
    for client in rented_movies:
        if id == client["client_id"]:
            client["rented_movies"].append(movie)
            has_rented = has_rented or True

    if not has_rented:
        client = dict()
        client["client_id"] = id
        client["rented_movies"] = []
        client["rented_movies"].append(movie)
        rented_movies.append(client)

    update_db_movies(movie)
    print(f"\nLa pelicula {movie} fue rentada por el cliente ID: {id}")


def search_movie():
    while True:
        print("Ingrese la pelicula a buscar")
        print("(De querer cerrar el programa ingrese \"quit\")")
        lookup_movie = input(">> ")
        existance = False
        for movie in db_movies:

            if movie["movie"] == lookup_movie:
                existance = existance or True
                if movie["abailability"] == 0:
                    print(f"\nLa pelicula {movie['movie']} no está disponible\n")

                else:
                    print("\nLa pelicula está disponible")
                    print("\nLOGIN")
                    print("Ingrese ID")
                    id = input(">> ")
                    print("Ingrese la pelicula a rentar")
                    pelicula = input(">> ")

                    rent_movie(id, pelicula)
                    print(f"La nueva disponibilidad de la pelicula es de {movie['abailability']} unidad/es\n")

        if lookup_movie == "quit":
            break

        if not existance:
            print(f"\nLa pelicula {lookup_movie} no existe\n")

search_movie()


print("\n~ Resumen de clientes ~")
for cliente in rented_movies:
    print(cliente)


