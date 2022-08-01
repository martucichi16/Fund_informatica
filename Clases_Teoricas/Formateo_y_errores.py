# SALIDAS
# Formateo de salida de datos

nombre = "Martina"
apellido = "Cichi"

# Formateo por oden
print("Mi nombre es {} y mi apellido es {}".format(nombre, apellido))

# Formateo con indices
print("Mi apellido es {1} y mi nombre es {0}".format(nombre, apellido))

# Formateo con nombre de variables
print("Mi nombre es {n} y mi apellido es {a}".format(n=nombre, a=apellido))

print("\n")

print("-Alineacion del texto a la derecha:")
d = "{:>30}".format("Hola a todos")
print(d)
print("La suma de los espacios y el texto es igual a", len("                  ") + len("Hola a todos"))

print("\n-Alineacion del texto a la izquierda:")
i = "{:30}".format("Hola a todos") + "fin"
print(i)

print("\n-Centrar el texto:")
c = "{:^30}".format("Hola a todos") + "fin"
print(c)


# Alineacion con numeros
# Truncar texto
a = "{:.3}".format("Hola a todos!") + "fin"
print(a)


# El formateo resulta muy util para los numeros:
# Numeros alineados a la derecha
print("{:>4}".format(10))
print("{:>4}".format(100))
print("{:>4}".format(1000))


print("\n")
# Numeros alineados a la derecha y rellenado con 0 a la izquierda
print("{:04}".format(10))
print("{:04}".format(100))
print("{:04}".format(1000))

print("\n")
# Truncamiento de numeros con decimales a un float con 2 decimales
print("{:.2f}".format(3.141526))

print("\n")
# Truncamiento de numeros con decimales a un float con 2 decimales, con espacios a la izquierda
print("{:7.2f}".format(3.141526))
print("{:7.2f}".format(153.21))

print("\n")
# Truncamiento de numeros con decimales a un float con 2 decimales, con 0 a la izquierda
print("{:07.2f}".format(3.141526))
print("{:07.2f}".format(153.21))

# En los ultimos 2 casos colocamos un 7, queriendo decir esto que los espacios + numeros = 7,
# y los 0 + los numeros = 7


print("\n-----------------------------------")
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
'''
Excepciones
# Tipos de errores:
# 1) Sintactico: error de sintaxis, relacionado a la escritura de las instrucciones
# El interprete lo reconoce antes de ejecutar, por lo que ya salta el error, sin ejecutar nada
# "SyntaxError: ..."

# 2) Semantico: durante la ejecución salta un error, como por ejemplo con la division de 0
# Ejecuta el programa hasta que encuentra el error semántico
'''

# Tratamiento de los errores semánticos a traves de EXCEPCIONES, que dé errores más "amigables"
# Ejemplo 1: error controlado con if
'''
print("Caso control del error con if:")
numero = int(input("Ingrese un numero:"))
if numero == 0:
    print("Error: No se puede ingresar un 0!!")
else:
    print(10/numero)

# Este tipo de errores controlados implica conocer todas las casuísticas por las cuales un programa puede
# dejar de funcionar y eso no siempre sucede
# Por ejemplo, si en lugar de ingresar un Nª cualquiera o un 0, ingresamos un string, el control realizado
# con el if no aplicaría y tendriamos un error arrojado por Python

print("\n")
# try + except: nos permite controlar todos los escenarios posibles de un error
# TRY: recibe todo el bloque de programa propenso a tener un error
# EXCEPT: escribimos la instruccion a ejecutar en caso de error
print("Caso excepcion con try y except:")
try:
    numero2 = int(input("Ingrese un numero:"))
    division = 10 / numero2
    print("Resultado:", division)
except:
    print("Error: No se puede ingresar un 0!!")


print("\n")
# A traves de un while se puede pedir reiteradas veces el ingreso del dato hasta que este sea correcto
# Mantenemos el except por si existe algun error como ingresar un string o cualquier tipo de dato distinto a un Nª
print("Caso con while, gracias al cual podemos repetir el ingreso del dato hasta que este ultimo sea valido:")
while True:
    try:
        numero3 = int(input("Ingrese un numero:"))
        division = 10 / numero3
        print("Resultado:", division)
        break
    except:
        print("Error: No se puede ingresar un 0!!")


print("\n")
# try, except, else, finally
# Intenta, si da error hace el except y si no da error hace el else
print("Caso while + else:")
while True:
    try:
        numero4 = int(input("Ingrese un numero:"))
        division = 10 / numero4
    except:
        print("Error: No se puede ingresar un 0!!")
    else:
        print("Resultado:", division)
        break
# En el TRY escribimos las instrucciones que debe hacer el programa, pero no es hasta el ELSE que le diremos
# al programa qué retornar por dichas instrucciones
# En el medio de eso escribimos la excepcion por si acaso hay algun error en el ingreso de los datos


print("\n")
# El finally es otro grupo de instrucciones, el cual se ejecutara tanto si el programa falla o no
print("Caso while + else + finally: el finally siempre se ejecuta, independientemente de la validez del valor" 
        "ingresado")
while True:
    try:
        numero5 = int(input("Ingrese un numero:"))
        division = 10 / numero5
    except:
        print("Error: No se puede ingresar un 0!!")
    else:
        print("Resultado:", division)
        break
    finally:
        print("FINALLY: Esto se ejecuta siempre")  # Independientemente de que haya un error o no va a ejecutar finally
'''

# MULTIPLES EXCEPCIONES
# En todos los casos anteriores de excepciones, sea cual sea el error, imprimia un mismo mensaje de excepcion. Por
# ejemplo daba lo mismo si lo que se ingresaba por consola era un 0 o un string, el programa siempre imprimia
# "Error: No se puede ingresar un 0!!")
# ¿No seria mejor que el programa reconozca el tipo de error y devuelva un "mensaje" especifico para cada error?

# Para hacer eso necesitamos incorporar al bloque de except el siguiente codigo:
while True:
    try:
        numero6 = int(input("Ingrese un numero:"))
        division = 10 / numero6
        print("Resultado:", division)
        break
    except Exception as e:
        print("Error de tipo:", type(e).__name__)


while True:
    try:
        numero6 = int(input("Ingrese un numero:"))
        division = 10 / numero6
        print("Resultado:", division)
        break
    except ValueError:
        print("Ingrese un valor válido (Nª)")
    except ZeroDivisionError:
        print("Ingrese un valor distinto a 0")
    except Exception as e:
        print("Error de tipo:", type(e).__name__)

# SIEMPRE ES MEJOR PONER LAS EXCEPCIONES ESPECIFICOS MAS ARRIBA Y DEJAR LAS GENERALES PARA EL FINAL

# En los bloques de except donde pusimos "ValueError" y "ZeroDivisionError" lo que estamos haciendo es decirle al
# programa que en el caso de que se reproduzcan esos tipos especificos de errores imprima un mensaje "personalizado"
# para ese error

# En el ultimo bloque de except escribimos una excepcion que reciba todos aquellos errores que no son por division
# de 0 o de valor (errores que no definimos). Definimos la excepcion con un nombre (en este caso la e) y con el
# codigo type(nombre_variable_excepcion).__name__ nos devuelve el tipo de error que ocurrio


# ¿Cuales son todos los tipos de errores? Estaria bueno conocerlos para poder usarlos en las excepciones

'''
Estructura recomendada (por Pablo) cuando hay varias excepciones:
try
except
except
except
else
finaly - optativa
'''
