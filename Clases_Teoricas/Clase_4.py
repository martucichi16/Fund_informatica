# La clase pasada vimos como ingresar datos a traves de la consola, lo cual demanda la interacción constante
# del programa con el usuario, dado que cada vez que se ejecuta necesitamos ingresar los datos


# EJECUTAR DESDE LA TERMINAL ---> python nombre_de_file.py

# -clear: limpia la terminal
# -sys: un módulo del sistema Python (como una extension)
# -argv: genera una lista de los argumentos que le pasamos por la terminal, es decir, los valores que queremos usar en
# las variables (despues del nombre del archivo): python Clase_4.py 10 5 /

# Esto lo hacemos para automatizar y que no haya una interaccion constante entre el usuario y el programa

# Si quisieramos tener 2 numeros y una operacion, ingresados por consola, seria de la siguiente manera:
# numero_1 = int(input("Ingrese el primer numero:"))
# numero_2 = int(input("Ingrese el segundo numero:"))
# operacion = input("Que operacion (+, -, *, /)?")

# Lo vamos a hacer por terminal:
import sys
lista = sys.argv
print(f"El .argv creo una lista con los argumentos que le pase: {lista}")

numero_1 = int(lista[1])
numero_2 = int(lista[2])
operacion = lista[3]

print("Numero 1:", numero_1)
print("Numero 2:", numero_2)

if operacion == "+":
    print("Resultado operacion:", numero_1 + numero_2)
elif operacion == "-":
    print("Resultado operacion:", numero_1 - numero_2)
elif operacion == "*":
    print("Resultado operacion:", numero_1 * numero_2)
else:
    print("Resultado operacion:", numero_1 / numero_2)


# Para entender un poco mejor la terminal:

# Directorio = carpeta
# Arbol de directorios (carpeta adentro de carpeta)
# Raiz del "arbol" = cd C:\
# Saber donde estoy: pwd
# cd ..: te lleva a carpetas atras

# RESUMEN
# Entrada interactiva: input()
# Entrada no interactiva: argumentos por terminal


# ------------------------------------------------------------------------------------------
# Video de youtube

# Para ejecutar en la terminal del PowerShell (no en PyCharm) necesito si o si posisionarme donde está el archivo
# o codigo de python que quiero ejecutar. Los siguientes "comandos" me permiten moverme dentro del explorador de
# archivos y buscar el directorio (carpeta) que estoy buscando:

# dir: enlista los archivos y carpetas que estan dentro de la posicion/direccion en la que estoy

# pwd: muestra donde estoy

# cd nombre_de_carpeta/archivo: me permite moverme, cambiar de posicion/direccion

# python: una vez que estoy en el directorio que guarda el archivo que quiero ejecutar, para ejecutarlo necesito
# escribir python nombre_de_archivo.py

# + dato: si quiero abrir una carpeta o archivo que tiene espacios, tengo que escribir el nombre entre "", como si
# fuera un string
