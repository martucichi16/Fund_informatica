# Ejercicio 1
print("EJERCICIO SHOPPING CART")
shopping_cart = []


def agregar_producto(product, cant):
    diccio_producto = dict()
    diccio_producto["producto"] = product
    diccio_producto["cantidad"] = cant

    shopping_cart.append(diccio_producto)


def buy_shopping_cart(lista_carrito):
    print("\nProductos en el carrito:")
    for product in lista_carrito:
        print(f"\t> {product['producto']}; {product['cantidad']} unidad/es")


while True:
    print("\nMenu de opciones")
    print("1) Agregar producto al carrito")
    print("2) Comprar")
    print("(De querer cerrar el programa ingrese \"quit\")")

    opcion = input(">> ")

    if opcion == "1":
        print("\n")
        producto = input("Producto a agregar\n>> ")
        cantidad = input("Cantidad a agregar\n>> ")

        agregar_producto(producto, cantidad)

    elif opcion == "2":
        buy_shopping_cart(shopping_cart)

    elif opcion == "quit":
        break

    else:
        print("\nOpción no válida, vuelva a intentarlo")
