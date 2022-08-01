# Continuacion Ejercicio 1 post clases

# import shapes ---> tiene que estar en la misma carpeta, sino hay que pasarle una ruta / path
# cubo = shapes.Cubo(4)

from Ejercicio_1_Shapes import Cubo, Esfera, PrismaRectangular

# cubo = Cubo(4)


def user_menu():

    print("¿Qué figuras imprimir?")
    print("\t1) Esfera")
    print("\t2) Cubo")
    print("\t3) Prisma Rectangular")

    option = input(">> ")

    if option == "1":
        radio = input(">> ")
        esfera = Esfera(radio)
        print(f"Imprimiendo {esfera.nombre}, por favor espere...")
        print(esfera.print_properties())

    elif option == "2":
        lado = input(">> ")
        cubo = Cubo(lado)
        print(f"Imprimiendo {cubo.nombre}, por favor espere...")
        print(cubo.print_properties())

    elif option == "3":
        pass

    else:
        print("Opción inválida")


user_menu()
