from io import open


# Nosotros trabajamos con bases de datos de tipo RELACIONAL: datos relacionados, conocemos sus relaciones, se guardan
# en tablas

# Fila = REGISTRO
# Columna = CAMPO

# Sistema gestor de base de datos/Motor de base de datos: son programas que nos permiten trabajar con bases de datos.
# Lenguaje por excelencia de datos es SQL

archivo = open("Texto.txt", "w")

linea = "Hola"
archivo.write(linea)