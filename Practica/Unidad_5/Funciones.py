# Funciones
# Bloque de codigo que se puede usar muchas veces, sin la necesidad de tener que volver a escribir
# el codigo

"""
Las funciones se definen de la siguiente manera:

def nombre_de_funcion(argumento1, argumento2, ...):
    instrucciones
    ...
    return lo_que_quiero_que_devuelva
"""


# Ejemplo:
def sum_numbers(num_1, num_2):
    print("La suma es: ", num_1 + num_2)
    return num_1 + num_2


sum_numbers(16, 14)

# Cuando creamos una funcion, definimos "parametros".
# Cuando "llamas" a la funcion para usarla, los datos que le pasas son "argumentos"

# Positional Arguments: al usar una funcion, Python mapea el primer argumento que le pasamos con el
# primer parametro de la funcion y asi...

# Keyword Arguments: escribir los argumentos en el orden que quiero, pero mapeando al usar
# el nombre del parametro para indicar qué dato es cuál

suma = sum_numbers(16, 14)  # La variable guarda el valor del return de la funcion

# Si lo imprimo podemos ver qué valor tiene asignado
print(suma)


print("\n---------------------------------------")
# "Warmup"
print("EJERCICIO DEPORTISTAS")
sportsmen = []


def save_sportsmen(sportsman, sport):
    sportsmen_dict = dict()
    sportsmen_dict["sportsman"] = sportsman
    sportsmen_dict["sport"] = sport

    sportsmen.append(sportsmen_dict)


def print_sportsman(sportsmen_list):
    for sportsman in sportsmen_list:
        print(f"El/La deportista {sportsman['sportsman']} juega {sportsman['sport']} ")


while True:
    print("\nMenu de opciones")
    print("1) Agregar deportista")
    print("2) Ver listado de deportistas")
    print("(De querer cerrar el programa ingrese \"quit\")")

    option = input(">> ")

    if option == "1":

        print("\nNombre del deportista")
        sportsman = input(">> ")
        print("Deporte")
        sport = input(">> ")

        save_sportsmen(sportsman, sport)

    elif option == "2":
        print_sportsman(sportsmen)

    elif option == "quit":
        break

    else:
        print("Valor invalido, vuelva a intentarlo")


'''
-En el caso de que una funcion reciba como argumento una lista global, los cambios que se le apiquen a esta lista a
lo largo del body, se verán reflejados en la lisa global original


MODULOS
-Un módulo es un archivo con extensión ".py" que contiene código que luego importamos en nuestro programa, como 
hicimos con los módulo "math" y "random"

-Los módulos nos sirven para agrupar funcionalidad relacionada y luego poder importarla en diferentes programas, 
brindando reutilización de código. Imagine un módulo como un conjunto de funciones.

-Siempre que importemos un modulo debemos importarlo al principio del programa

-Una vez importado el modulo, para utilizar sus funciones se hace de la siguiente manera:
modulo.funcion()

 ~ LO PRUEBO EN LOS ARCHIVOS MODULO Y APP ~
'''
