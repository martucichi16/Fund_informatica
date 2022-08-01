# Operaciones

def suma_lista(lista_numeros):
    resultado = 0
    for numero in lista_numeros:
        resultado += numero
    return resultado


def resta(*numeros):
    resultado = 0
    for numero in numeros:
        if numero == numeros[0]:
            resultado += numero
        else:
            resultado -= numero
    return resultado


def multiplicacion(*numeros):
    resultado = 1
    for numero in numeros:
        resultado = resultado * numero
    return resultado
