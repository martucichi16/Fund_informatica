# Unidad_4
# Cuando usamos el input y ejecutamos el programa, el programa se pausa porque se queda esperando
# un "comando" para seguir el flujo
# Esa entrada de datos se da, por ahora, a traves de la "linea de comandos" o consola

print("Inicio del programa\n")

nombre = input("Ingrese su nombre: ")

print(f"Su nombre es {nombre}")

print("\nFin del programa")

# -----------------------------------------------------------------
print("\n")
# Todo dato ingresado por la consola tiene "formato" de string
numero = input("Ingrese un numero: ")

print(type(numero))
print(f"El numero ingresado fue {numero}")

# Si quiero cambiarle el formato podria hacerlo a tarves de una funcion cuando defino la variable ("casting")
print("\n")
numero2 = int(input("Ingrese otro numero: "))

print(type(numero2))
print(f"El segundo numero ingresado fue {numero2}")

# -----------------------------------------------------------------
print("\n-------------------------------------------------------------")
# 3 diseños para el ciclo while
# When to quit --> condicion

message = ""
while message != "quit":
    message = input("Enter your name: ")
print(message)

# En este ejemplo, siempre que se ingrese un texto distinto a "quit", el programa me va a pedir de vuelta
# que ingrese datos. Cuando lo ingresado sea "quit", imprimira el texto y rompe con  el programa


print("\n-------------------------------------------------------------")
# Flag
# Hacemos uso de una variable boolanea

active = True
while active:
    message = input("Enter your name: ")
    if message == "quit":
        active = False
    else:
        print(message)


# En este caso siempre que ingrese un dato que no sea "quit" lo va a imprimir por consola, y al ingresar
# el quit, la variable booleana active va a cambiar a False y por ende rompe el while


print("\n-------------------------------------------------------------")
# Break
while True:
    name = input("Enter your name: ")
    if name == "quit":
        break
print(name)


# Al decirle while True, le indicamos que itere infinitamente, pero le indicamos que cuando se ingrese el quit
# rompa con el ciclo

# -----------------------------------------------------------------------------------------

print("\n-------------------------------------------------------------")
# ERRORES
try:
    print(10/0)
except ZeroDivisionError:
    print("No es posible dividir por 0")

# El try y except sirve para "salvar" los errores, obtener un flujo alternativo que sea mas amigable
# a la hora de devolver el error
