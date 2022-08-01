# Ejercicio 1
# Cotizaciones al 22/03/22 de Criptomonedas
bitcoin = "4.483.127"
ethereum = "308.416"
litecoin = "12.080"

print("Cotizacion Bitcoin (22/03/22): ", bitcoin)
print("Cotizacion Ethereum (22/03/22): ", ethereum)
print("Cotizacion Litecoin (22/03/22): ", litecoin)


# Ejercicio 2
# Poniendo la f antes de las "" del string dentro del print, esto nos permite usar la variable
# dentro del string sin necesidad de abrir y cerrar las comillas
print("\n-------------------------------")
print(f"Cotizacion Bitcoin (22/03/22): {bitcoin}")


# Ejercicio 3
print("\n------------------------------")

nombre = "ERNESTO"
apellido = "caldini"
mail = "Ecaldini@gmail.com"

print(f"Datos cargados por el usuario: \nnombre = {nombre}\napellido = {apellido}\nmail = {mail}")

print("\nInfo. en la base de datos: \nnombre = ", nombre.lower(), "\napellido = ", apellido.lower(),
      "\nmail = ", mail.lower())
# The .lower() METHOD converts all uppercase characters in a string into lowercase characters and
# returns it.

print("\nInfo. en perfil: \nnombre = ", nombre.title(), "\napellido = ", apellido.title(), "\nmail = ",
      mail.title())
# The .title() METHOD makes the first letter in each word upper case:

print("\n")
nombre = "ERNESTO   "
print("Mi nombre tiene ", len(nombre), "caracteres")

nombre = nombre.rstrip()
print("Despuès de usar el .rstrip() mi nombre tiene ", len(nombre), " caracteres")
# Que hace el rstrip()? Remueve los espacios al final de un string


# Ejercicio 4
print("\n------------------------------")

importacion_en_dolares = 300 * 1500
cotizacion_dolar = 110.69
monto_a_importar = importacion_en_dolares * cotizacion_dolar
interes = 0.03
comision = interes * monto_a_importar
sellado = 15000

total_a_cobrar = monto_a_importar + comision + sellado

print("El monto total a cobrar al cliente es de $", total_a_cobrar)

cant_socios = 5
comision_por_socio = comision / cant_socios
print(f"\nCada socio cobrara ${comision_por_socio} de comision")


print("\n------------------------------")
# Investigación:
# ¿Cómo obtener la cantidad de caracteres de un string?
string = "hola"
print("Mi variable string guarda el valor: ", string)
print("El largo del string es: ", len(string))


print("\n------------------------------")
# ¿Qué sucede cuando intentamos realizar una división por cero? Salta un error "ZeroDivisionError"
# ------------------------------------------------------

# Partiendo de un string con valor “python” ¿cómo podemos obtener el primer carácter y el último?
# Con los indices []
lenguaje = "python"
print("La primera letra del lenguaje es ", lenguaje[0])
print("La ultima letra del lenguaje es ", lenguaje[-1])
