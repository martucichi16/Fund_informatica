# Ejercicio 6
import random

manufactoring_cars = [{'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Raptor', 'engine': '3.5'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Raptor', 'engine': '3.5'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Raptor', 'engine': '3.5'},
                      {'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Mondeo', 'engine': '2.0'}]

car_colors = ['white', 'dark gray', 'red', 'black']

car_options = {"basic": ['synthetic seats', 'led dashboard'], "premium": ['leather seats', 'GPS', 'led dashboard']}


# random.choice(list): elige un valor aleatorio de la lista


def paint_car(car):
    # No le paso color como parametro porque no tiene sentido si va a estar automatizado
    # + si pongo el random.choice como parametro default me pinta todos del mismo color
    color = random.choice(car_colors)
    car["color"] = color
    print(f"Se pintó el modelo {car['model'].upper()} con el color {car['color'].upper()}")


def car_interior(car):
    if car["model"] == "Focus":
        car["interior"] = car_options["basic"]
    else:
        car["interior"] = car_options["premium"]


def manufactoring():
    for manufactoring_car in manufactoring_cars:
        paint_car(manufactoring_car)
        car_interior(manufactoring_car)

        print(manufactoring_car)
        print("\n--------------------------------------------------------")


manufactoring()
