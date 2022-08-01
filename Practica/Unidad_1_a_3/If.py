# Arrancamos a ver el if en la parte de listas, con el ejercicio 9

"""
weather = "raining"
if (weather == "raining"):
print("Take umbrella")

La linea de la condición del if, se llama "conditional test" o "prueba condicional", y su
resultado puede ser True or False
"""


# Ejercicio 10
productos = ["té", "café", "arroz", "harina 000", "lata de tomate", "jabón", "queso pategras", "leche",
             "levadura", "desodorante", "detergente", "agua con gas", "trapo de piso", "lavandina",
             "aceite de oliva", "vinagre", "mayonesa", "ketchup", "galletas de arroz"]

producto_a_buscar = "leche"
for producto in productos:
    if producto == producto_a_buscar:
        print("Producto en existencia: ", producto)
        break
    elif producto != productos[-1]:
        continue
    else:
        print("El proveedor no cuenta con el producto:", producto_a_buscar)


producto_a_buscar2 = "mostaza"
for producto in productos:
    if producto == producto_a_buscar2:
        print("Producto en existencia: ", producto)
        break
    elif producto != productos[-1]:
        continue
    else:
        print("El proveedor no cuenta con el producto:", producto_a_buscar2)

# Preguntar por la última parte de la consigna


print("\n----------------------------------------------")
# Ejercicio 11
usuarios = ["marmeant", "gruntmar", "tokcie", "ciebank", "mueslicie", "sanero", "robedrock", "admin",
            "derivero", "posloth", "claypo", "locustpo", "mostter"]

for user in usuarios:
    if user != "admin":
        print("Bienvenido estimado", user.title(), ", le deseamos un buen día")
    else:
        print("Bienvenido Administrador, en qué lo puedo ayudar")

print("\n")
# Programa modificado
user_acces_denied = "claypo"

for user in usuarios:
    if user == user_acces_denied:
        print(f"User: {user} acces denied")
    elif user != "admin":
        print("Bienvenido estimado", user.title(), ", le deseamos un buen día")
    else:
        print("Bienvenido Administrador, en qué lo puedo ayudar")

print("\n----------------------------------------------")
# Ejercicio 12
students = [37128693, 38346828, 48577851, 23923908, 23747794, 46033685, 28372488, 33143443,
            38122921, 38915457, 24807285, 35759559, 21061055, 33613272, 24082600, 26477319,
            46655903, 46988530, 25145603, 35368988, 25393784, 21295674, 48348316, 31247247,
            28498292, 37538741, 21332845, 27557703, 24435687, 38794110, 44518399, 34178717,
            45788239, 36998322, 32098132, 22185788, 25030083, 21256524, 34592517, 41755997,
            37570846, 30401721, 34832996, 47330519, 34380715, 42724546, 26615771, 23171192,
            42223891, 40210778, 33530381, 20478110, 20753240, 28187999, 27785500, 37236996,
            22981717, 27744330, 44855039, 36552090, 36824210, 39684157, 26469844, 45037525,
            25916934, 41595563, 23571241, 30552911, 40100736, 36047292, 46818813, 36680587,
            36107300, 41367347]

student_marks = [15, 19, 19, 9, 6, 12, 20, 3, 1, 15, 10, 16, 3, 25, 18, 13, 24, 30, 7, 28, 20, 25,
                 28, 10, 2, 1, 18, 20, 3, 3, 19, 12, 11, 8, 24, 27, 15, 15, 19, 0, 27, 8, 29, 5,
                 1, 12, 8, 17, 19, 0, 0, 18, 15, 23, 22, 2, 24, 6, 10, 28, 18, 3, 15, 6, 26, 0,
                 21, 14, 24, 13, 10, 17, 16, 2]

my_dni = 22185788
index_dni = -1
for dni in students:
    if dni != my_dni:
        index_dni += 1
    else:
        index_dni += 1
        break
print("El índice en la lista de mi dni es: ", index_dni)

# Sería mucho mejor definir una función que reciba un dni y busque la nota, en lugar de definir en una
# variable un dni fijo, pero lo resolví de esta manera porque todavia no vimos funciones en la materia

# Verificación de que mi programa salió bien:
if students[index_dni] == my_dni:
    print("El programa funcionó")
else:
    print("Revisar programa")


print("Mi nota es: ", student_marks[index_dni])


print("\n")
# Clasificación de notas
avanzado = []
intermedio_alto = []
intermedio_bajo = []
basico = []
debajo_basico = []

for mark in student_marks:
    if mark >= 25:
        avanzado.append(mark)
    elif mark >= 20:
        intermedio_alto.append(mark)
    elif mark >= 16:
        intermedio_bajo.append(mark)
    elif mark >= 10:
        basico.append(mark)
    else:
        debajo_basico.append(mark)

print(len(avanzado), " exámenes tuvieron una nota que aplica al nivel de avanzado")
print(len(intermedio_alto), " exámenes tuvieron una nota que aplica al nivel de intermedio alto")
print(len(intermedio_bajo), " exámenes tuvieron una nota que aplica al nivel de intermedio bajo")
print(len(basico), " exámenes tuvieron una nota que aplica al nivel de basico")
print(len(debajo_basico), " examenes tuvieron una nota por debajo del básico")


print("\n")
# Total de estudiantes
cant_students = len(students)
print(f"Al exámen se presentaron {cant_students} estudiantes")


print("\n----------------------------------------------")
# Ejercicio 13
deudas_de_clientes = [1323.23, 5755.20, 1928, 3876, 4539, 4648, 4000, 3713, 3148, 1240, 3232, 4948,
                      2491, 2092, 3471, 1704.92, 4630, 4697, 1495.30, 2174, 2897, 2505, 3502, 2573]

# No se me ocurre cómo hacerlo con un while, por eso lo hago con un for
deudas_actualizadas = []
for deuda in deudas_de_clientes:
    deudas_actualizadas.append(round(deuda * 1.035, 2))

print("Las deudas después del aumento son:", deudas_actualizadas)


'''
Investigación

DATOS MUTABLES: permiten ser modificados una vez creados
DATOS INMUTABLES: no permiten ser modificados una vez creados

Son conceptos importantes a entender y conocer porque sino podriamos llegar a tener 
comportamientos inesperados en nuestros programas.

--------------------------------------------------------------------------------------
Si no se usa una condición de corte en un while se genera un bucle infinito (creo)

--------------------------------------------------------------------------------------


'''
