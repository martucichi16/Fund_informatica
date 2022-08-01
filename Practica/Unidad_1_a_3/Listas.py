# LISTAS: Son una colección de items/elementos en un orden particular.
bitcoin = "4.483.127"
ethereum = "308.416"
litecoin = "12.080"
crypto = [bitcoin, ethereum, litecoin]
print("Lista crypto: ", crypto)

print("\n")
# Para agregar elementos al final de la lista se puede hacer con el lista.append(elemento)
crypto.append("200")
print("Agregué un nuevo valor a las crypto: ", crypto)

# Tambien se le puede insertar un valor y no necesariamente al final: lista.insert(indice, elemento)
crypto.insert(0, "500")
print("Con .insert pude agregar un elemento al principio de la lista: ", crypto)
crypto.insert(3, "887")
print("Y otro elemento a la mitad de la lista: ", crypto)

print("\n")
# Se puede dar vuelta la lista con lista.reverse()
crypto.reverse()  # No hace falta redefinir la variable, la afecta directo
print("Lista al reves: ", crypto)

print("\n")
# Para solicitar elementos de la lista hay que usar los indices []
print("El primer elemento de la lista es: ", crypto[0])
print("El 3 elemento de la lista es: ", crypto[2])
print("El ultimo elemento de la lista es: ", crypto[-1])

print("\n-------------------------------------")

# ITERACIONES
# Para "recorrer" una lista, con una longitud definida, podemos usar el for
friends_favs = ["Monica", "Chandler", "Joey"]

print("Mis personajes favoritos de Friends son:")
for personaje in friends_favs:
    print(personaje)

# Dentro del for se usa una "mini variable", en el ejemplo anterior "personaje", a la cual se le va a ir
# asignando, automaticamente,  el valor de cada elemento de la lista, y de esa manera funciona el for.
# Basicamente con esa mini variable nos referimos a los elementos de la lista


print("\n-------------------------------------")
# Ejercicio 5
# Por convcención, las listas suelen definirse con nombres en plural
guests = ["ernest", "martin andrés", "sofia", "lucia", "jose maría", "abril"]

print("Los huespedes son:")
for guest in guests:
    print(guest.title())

print("\n")
print("Podemos verlos mejor en la siguiente linea:")
guests_formated = []
for guest in guests:
    guests_formated.append(guest.title())
print(guests_formated)

print("\n-------------------------------------")
# Ejercicio 6
new_guests = ["martina", "josefina isabel", "tomás"]

# Concatenamos (+)
merge_guests = guests + new_guests
print("La nueva lista de huespedes es :", merge_guests)

template_guests = []
for guest in merge_guests:
    template_guests.append(guest.title())
print("Y aqui podemos verla bien formateada: ", template_guests)

print("\n-------------------------------------")
# Ejercicio 7: hay que remover un huesped
# Para eliminar algun elemento se puede usar el pop o el remove
# El pop elimina el elemento pero ademas lo podes "guardar":

guest_removed = template_guests.pop(-1)
print(f"Huesped eliminado: {guest_removed}")
print("Huespedes actualizado: ", template_guests)

# Como podemos ver se eliminó el último elemento de la lista pero al usar la variable donde usamos el
# pop nos muestra el elemento eliminado


# CONCATENACION
# 1) Con el +
# 2) Con el for y una lista vacia a la que agregamos cosas
print("\n-------------------------------------")


# Ejercicio 7
pares_hasta_100 = []
for numero in range(0, 100, 2):
    pares_hasta_100.append(numero)
print("Los numeros pares hasta 100 son: ", pares_hasta_100)


print("\n-------------------------------------")
# Ejercicio 8
lista_de_precios = [117.12, 121.19, 128.37, 135.70, 139.47, 151.80, 157.95, 161.80,
                    166.20, 174.51, 179.68, 188.96, 200.89, 211.89, 225.99, 232.50,
                    249.12, 262.69, 177.67, 187.19, 193.81, 209.57, 216.73, 227.52,
                    239.24, 250.22, 256.04, 269.91, 282.93, 12.37, 92.17, 65.37,
                    73.26, 43.26, 78.26]

print("Nuestra lista de precios es la siguiente: ", lista_de_precios)

nuevos_precios = []
for precio in lista_de_precios:
    nuevos_precios.append(precio * 1.07)

print("Hubo un aumento de los precios del 7%")
print("Vamos a necesitar redondear porque el aumento del 7% da muchos decimales, como por ejemplo el "
      "primer precio actualizado: ", nuevos_precios[0])

# Como podemos ver quedan numeros con muchisimos decimales, asi que estaria mejor si redondeamos los
# precios con solo 2 decimales
# Para eso podemos usar el round(): round(elemento_a_redondear, cant. de decimales)

new_product_price = []
for precio in lista_de_precios:
    new_price = round(precio * 1.07)
    new_product_price.append(new_price)
print("La lista de precios actualizada es la siguiente: ", new_product_price)

print("\n-------------------------------------")
# Ejercicio 9
resultados_encuesta = [True, False, True, True, True, False, True, False, True, True,
                       True, False, False, True, True, True, True, False, True, True,
                       True, False, True, True, False, True, True, False, True, False,
                       True, True, True, False, True, True, True, False, True, False,
                       True, True, True, False, False, True, True, True, True, False,
                       True, True, True, False, True, True, False, True, True, False,
                       True, False, True, True]

aprobada = 0
desaprobada = 0
for resultado in resultados_encuesta:
    if resultado:  # Al "resultado" ser un booleano, no hace falta igualarlo a True
        aprobada += 1
    else:
        desaprobada += 1

print("Gustó: ", aprobada)
print("No gustó: ", desaprobada)

porcentaje_aprobada = aprobada / len(resultados_encuesta) * 100
porcentaje_desaprobada = desaprobada / len(resultados_encuesta) * 100

print(f"\nAl {porcentaje_aprobada}% de los encuestados le gustó la gaseosa, mientras que al "
      f"{porcentaje_desaprobada}% restante no le gustó")


print("\n")
# Con el int(float) trunca el int, lo que quiere decir que le saca los decimales
if porcentaje_aprobada > 65:
    print("Conclusion: PRODUCTO EXITOSO")
else:
    print("Conclusion: Aun hay que mejorar el producto")

print("\n-------------------------------------")
# -------------------------------------------------------------------------------------------------
# Para copiar una lista se puede hacer de la siguiente manera:
colores = ["Rojo", "Verde", "Amarillo", "Rosa"]
print("La lista contiene:", colores)

copia_colores = colores[:]
print("La copia contiene:", copia_colores)

# Completar con ejemplos de las funciones para lista, que estan en el link del pdf
