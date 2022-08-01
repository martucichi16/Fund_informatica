"""
PERSISTENCIA
Como vimos en los programas hechos hasta ahora, una vez que se terminan de ejecutar, se borra lo que hicimos ---
esto es porque son VOLATILES porque se ejecutan en la memoria RAM de la computadora

Para guardar los datos y que no se pierdan vamos a ver el tema de PERSISTENCIA, que nos va a permitir guardar los
datos en en algún lugar que no sea volátil, como los archivos (pueden tener distintos formatos"

El formato de archivo más simple es el de texto (ej.: bloc de notas)

1) APERTURA DEL ARCHIVO:
"""

from io import open
archivo = open("Texto.txt", "w")


"""
Mediante la funcion open() indicamos que tiene que abrir el archivo. El primer argumento debe ser el nombre del
archivo a abrir, y despues el "modo de apertura"


Funciones para editar el archivo:
{"w", "a"}
• write: sobreescribe todo lo que ya está en el archivo indicado

{"r"}
• read: lee separando las lineas
• readlines: lee pero pone las lineas separadas por coma
• readline: lee la primera line ¿?

• close: cierra el archivo y no permite que se siga editando
• del: ??
"""

linea = "Ejecuto un write\ny sobrescribo lo que ya\nestaba en el archivo\n"
archivo.write(linea)

# archivo.close()
# del(archivo)  # ¿Que hace el del?

# Otra manera de escribir el archivo es con las lineas en una lista y usando el writelines()
lineas = ["Agrego más texto\n", "al archivo de texto"]
archivo.writelines(lineas)

archivo.close()

# Ahora, podriamos leer el contenido del archivo desde la consola a traves del metodo read

archivo_r = open("Texto.txt", "r")

contenido = archivo_r.read()
contenido_lista = archivo_r.readlines()

linea1 = archivo_r.readline()
linea2 = archivo_r.readline()


print(contenido)
print(contenido_lista)  # Me trae una lista vacia y no se por que

print(linea1)
print(linea2)

archivo_r.close()

# WITH
with open("Texto.txt", "r") as archive:
    for linea in archive:
        print(linea)

# Al ejecutar el WRITE no hace falta cerrar el archivo porque se hace automaticamente. Si intento escribir despues del
# write, voy a tener un error


# Hasta ahora vimo el write con el modo de apertura "r", que si se ejecuta por primera vez, sobreescribe lo que ya está
# en el archivo indicado
# ¿Y si quisieramos abrir un archivo con texto y agregar texto pero sin borrar el ya existente?
# En este caso usamos APPEND (a) cuando abrimos el archivo e indicamos a traves del write el texto que queremos añadir
archivo = open("Texto.txt", "a")
archivo.write("\nAgrego una nueva linea con append\n")

archivo.close()

# ---------------------------------------------------------------------------------------------------------------------
# PUNTERO
# Seek: indicamos desde qué posicion arranca a leer el archivo

archivo = open("Texto.txt", "r")

archivo.seek(10)
content = archivo.read()
print(content)

short_content = archivo.read(6)  # Le indico con el parametro que a partir de donde esta el puntero lea 6 caracteres
print(short_content)  # No me lo imprime

archivo.close()


archivo = open("Texto.txt", "r+")

archivo.seek(10)
nuevo = "HOLA"
archivo.write(nuevo)
# Ver que se agrega el HOLA en el archivo

archivo.close()

