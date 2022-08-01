import pickle
import csv

# Nos permite guardar info que solo puede leer la computadora
archivo = open("Colecciones.txt", "wb")

lista = [0, 1, 2, 3, 4]
pickle.dump(lista, archivo)  # Para agregar usamos el dump y "wb"

archivo.close()
del archivo


# Creamos un archivo colecciones.txt donde guardamos la lista. Si abrimos el archivo nos van a aparecer simbolos que no
# vamos a entender, dado que el pickle lo guarda como para que la computadora pueda leer lo guardado

archivo = open("Colecciones.txt", "rb")

lista = pickle.load(archivo)  # Para leer usamos el load y "rb"
print(lista)

archivo.close()
del archivo


# ---------------------------------------------------------------------------------------------------------------------
print("\nINTENTANDO CON DICCIONARIOS")

archivo = open("Colecciones.txt", "wb")

persona1 = {"nombre": "GUSTAVO", "apellido": "RODRIGUEZ", "edad": 30, "telefono": "1560254580"}
pickle.dump(persona1, archivo)

persona2 = {"nombre": "GLORIA", "apellido": "BORIA", "edad": 70, "telefono": "1544782003"}
pickle.dump(persona2, archivo)

persona3 = {"nombre": "MARCOS", "apellido": "PEREZ", "edad": 23, "telefono": "1502335561"}
pickle.dump(persona3, archivo)

archivo.close()
del archivo


# Para obtener todos los diccionarios usamos un ciclo while:
archivo = open("Colecciones.txt", "rb")

while True:
    try:
        cliente = pickle.load(archivo)
        print(cliente)
    except EOFError:
        break

archivo.close()
del archivo


# ---------------------------------------------------------------------------------------------------------------------
print("\nUSANDO CSVs CON PYTHON")

clientes = [
    ("Jorge", "Perez", 43, "Jorge.perez@gmail.com"),
    ("Maria", "Martinez", 65, "Maria.martinez@gmail.com"),
    ("Jay", "Pritchet", 63, "Jay.pritchet@gmail.com"),
    ("Monica", "Geller", 24, "Monica.geller@gmail.com")
]

with open("csv_ej.csv", "w", newline="\n") as archivo:
    writer = csv.writer(archivo, delimiter=";")
    for cliente in clientes:
        writer.writerow(cliente)


with open("csv_ej.csv", "r", newline="\n") as archivo:
    reader = csv.reader(archivo, delimiter=";")
    for cliente in reader:
        print(cliente, type(cliente))


# ---------------------------------------------------------------------------------------------------------------------
print("\n")
# Otra manera de leerlo
with open("csv_ej.csv", "r", newline="\n") as archivo:
    reader = csv.reader(archivo, delimiter=";")
    for nombre, apellido, edad, email in reader:
        print(nombre, apellido, edad, email)


# ---------------------------------------------------------------------------------------------------------------------
print("\n")
# Armar el csv con la primera fila que tiene los "encabezados"
clientes = [
    ( 'Jose', 'Peralta', 24, 'jose.peralta@email.com' ),
    ( 'Marta', 'Lopez', 33, 'marta.lopez@email.com' ),
    ( 'Ernesto', 'Garcia', 36, 'ernesto.garcia@email.com' ),
    ( 'Norma', 'Gonzalez', 28, 'norma.gonzalez@email.com' )
]

with open('csv_ej.csv','w', newline='\n') as archivo:
    campos = ['nombre', 'apellido', 'edad', 'email']
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for nombre, apellido, edad, email in clientes:
        writer.writerow({
            'nombre':nombre,
            'apellido': apellido,
            'edad': edad,
            'email': email
        })

archivo.close()
del (archivo)


# ---------------------------------------------------------------------------------------------------------------------
print("\n")
with open('csv_ej.csv','r', newline='\n') as archivo:
    reader = csv.DictReader(archivo)
    for cliente in reader:
        print(cliente['nombre'],
              cliente['apellido'],
              cliente['edad'],
              cliente['email'])
