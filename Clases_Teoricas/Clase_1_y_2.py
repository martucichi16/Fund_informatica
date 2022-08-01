# LISTAS
lista = [0, 1, 2, 3]
print("La lista original es:", lista)

# Para agregar elementos a la lista:
lista.append(4)
print("Con .append() se le puede agregar elementos al final de la lista:", lista)

# o tambien se puede hacer de la siguiente manera:
lista += [5, 6]
print("O con +=:", lista)

# para eliminar el ultimo elemento de la lista:
lista.pop()
print("A traves del .pop() se elimina el ultimo elemento:", lista)

# Se pueden hacer listas de listas
elem1 = [1, 0, 0]
elem2 = [0, 1, 0]
elem3 = [0, 0, 1]
matriz_identidad = [elem1, elem2, elem3]
print(matriz_identidad)

elem2[1] = 7
print(matriz_identidad)

# si quiero saber un elemento de la lista dentro de la lista:
e = matriz_identidad[2][2]
print(e)


print("\n----------------------------")
# BOOLEANOS
# "funcionan" con operadores logicos
a = True
b = False
print(a and b)

c = not a
print(c)

# el and tiene mas precedencia que el or
# a or b and c = a or (b and c)

# el not tiene mas precedencia que los otros operadores
# a and not b = a and (not b)


print("\n----------------------------")
# While / contador
contador = 0
while contador < 5:
    print("Ejecuto el ciclo iterativo")
    contador += 1
print("El contador vale ", contador)
print("Fin del ciclo")

print("\n----------------------------")
# continue
c = 0
while c < 5:
    c += 1
    if c == 2:
        continue
print(c)
print("Fin del ciclo")
# uso el continue porque no quiero que imprima el 2
