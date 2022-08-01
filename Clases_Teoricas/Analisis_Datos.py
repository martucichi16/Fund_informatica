import pandas as pd
import matplotlib.pyplot as plt

# Creamos una serie (objeto
# Cuando no indicamos los indices, se crean como default indices numericos
s = pd.Series([12,-4,-7,-9])
print(s)
print('values: ', s.values)
print('index: ', s.index)

print("\n------------------------------------------------------------------------")
# Con el index podemos crear el indice que querramos
s = pd.Series([12,-4,-7,-9], index=['a','b','c','d'])
print(s)
print('values: ', s.values)
print('index: ', s.index)


print("\n------------------------------------------------------------------------")
# Seleccion de elementos idividuales, a traves del indice/posicion y "clave" (indice generado)
print(s)
print('Por indices: ', s[2])
print('Por clave: ', s['b'])

print("\n")
# Selección de multiples elementos
print('Por indices: ', s[0:2])
print('Por clave: ', s[['b','c']])


print("\n------------------------------------------------------------------------")
# Asignando/cambiando valores
print("Serie previo a cambios:")
print(s)


s[0] = 10
s['b'] = -19
print("\nSerie con valores cambiados:")
print(s)

print("\n")
s[0:2] = 18
s[['c','d']] = -4
print(s)


print("\n------------------------------------------------------------------------")
# Filtrar valores en serie con condiciones
# Guardamos la condicion en una variable y pedimos que devuelva aquellos elementos de la serie que cumplan con la
# condicion de la siguiente manera:
s = pd.Series([12, -4, -7, -9], index=['a', 'b', 'c', 'd'])

sMayore = s[s > 8]
print('sMayore: ', sMayore)


print("\n------------------------------------------------------------------------")
# Es posible aplicar operaciones matemáticas sobre las series
print('Aplicando operaciones matemáticas a las series:')
suma = s + 3
print('suma: \n ', suma)

suma = s /  2
print('sMayore: \n ', suma)


print("\n------------------------------------------------------------------------")
# Medidas
s = pd.Series([12,-4,-7,-9], index=['a','b','c','d'])

# Hay como funciones o metodos que devuelven ciertas medidas, por ejemplo:
promedio_serie = s.mean()
desvio_serie = s.std()
print('Promedio: ', promedio_serie)
print('Desvio estanadr', desvio_serie)


# Sino, a traves del .describe(), podemos obtener un resumen de todas las medidas importantes
print('\nDescribe la serie: ')
print(s.describe())


print("\n------------------------------------------------------------------------")
# Eliminar elementos repetidos de la serie: unique()
s2 = pd.Series([1, 1, 0, 2, 0, 5])

unicos = s2.unique()
print(unicos)


print("\n------------------------------------------------------------------------")
# Se puede crear series a partir de diccionarios haciendo pd.Series(dicc)
# Esto va acrear una serie donde los indices van a ser las keys del diccionario y los valores de la serie van a ser los
# valores del diccionario

my_dicc = {"blue": 10, "green": 24, "red": 8}
s_form_dicc = pd.Series(my_dicc)
print(s_form_dicc)


# Otro caso: le pasamos un indice que no está en el diccionario, por lo que el valor es NaN
colors = ["blue", "green", "yellow", "red"]
s_from_dicc = pd.Series(my_dicc, index=colors)
print(s_from_dicc)


print("\n------------------------------------------------------------------------")
# Suma de series
# Definimos 2 diccionarios con sus respectivos indices/etiquetas

# Serie 1:
my_dicc = { 'red':100, 'blue':200, 'yellow':500, 'orange':700, 'green':600 }
colors = ['red', 'yellow', 'green', 'orange', 'blue']

my_serie1 = pd.Series(my_dicc, index=colors)

# Serie 2:
my_dicc2 = {'red': 400, 'yellow': 100, 'black': 500}
my_serie2 = pd.Series(my_dicc2)


# Suma: la suma va a resultar en una nueva serie que contendra los indices de ambas series sumadas, pero los unicos
# indices que tendran valores seran aquellos que se encuentran en ambas series sumadas y que contienen valores en sus
# respectivas series "natas". Si el indice se encuentra en una sola de las series o se encuentra en las 2 pero en alguna
# tiene como valor NaN, entonces su valor en la serie sumada será NaN
suma_series = my_serie1 + my_serie2
print("Suma de series: ", suma_series)


print("\n------------------------------------------------------------------------")
print("\n------------------------------------------------------------------------")
print("DATAFRAMES")
# DataFrame: extiende una serie a múltiples dimensiones. Consiste en una colección de columnas donde cada una puede
# contener valores de un tipo de dato diferente

# Los DataFrames reciben 2 listas de etiquetas: uno para las etiquetas de las filas y otra para las etiquetas de la
# columnas

# Para crear un DataFrame lo podemos hacer a traves de un diccionario

data = {
    'color': ['blue','green','yellow','red','white'],
    'object': ['red', 'yellow', 'green', 'orange', 'blue'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}

# Cada Key representará una columna y sus valores seran los valores de las filas (en sus columnas correspondientes)

print("Cresmos un DataFrame con sus columnas:")
frame = pd.DataFrame(data)
print(frame)


# Si solo quisieramos incluir alguna de las keys del diccionario como columnas, podriamos haerlo de la siguiente manera

print("\nCreamos un DataFrame, pero solo con las columnas de object y price:")
frame_2 = pd.DataFrame(data, columns=['object', 'price'])
print(frame_2)

# Hasta el momento creamos DataFrames con columnas, pero los indices de las filas son los default (numerado)
# Si queremos, podemos ponerle nombre a las filas tambien. Esto se puede hacer a traves del index

print("\nCreamos de nuevo el DataFrame completo, pero ahora le agregamos el indice/etiqueta de fila")
frame = pd.DataFrame(data, index=["one", "two", "three", "four", "five"])
print(frame)


print("\n------------------------------------------------------------------------")
# Tambien podemos pedir unicamente las columnas, los indices/filas y los valores respectivamente
print("Columnas: ", frame.columns)
print("Filas: ", frame.index)
print("Valores: ", frame.values)


print("\n------------------------------------------------------------------------")
# Seleccionar una columna en particular: DataFrame[column]
print("Seleccionar columna")
columna_precio = frame["price"]
print(columna_precio)


print("\n------------------------------------------------------------------------")
# Seleccionar una fila en particular: DataFrame.loc[indice_nº]
print("Seleccionar una fila:")
# fila = frame.loc[2]
# print(fila)

# Seleccionar multiples filas
print("\nSeleccionamos varias filas:")
# filas = frame.loc[[2, 4]]
# print(filas)


print("\n------------------------------------------------------------------------")
# Podemos asociar un nombre a TODAS las filas y a TODAS las columnas, como para describir en general lo que enlista
# cada una. Por ejemplo, indicar que en las filas se enlistas codigos o dnis
frame.index.name = "id"
frame.columns.name = "item"
print(frame)


print("\n------------------------------------------------------------------------")
# Agrgando una nueva columna al DataFrame: esto se realiza simplemente asignando un valor a una columna no existente
frame["new"] = 12
frame["new_2"] = [2, 5, 1.5, 8, 6]
print(frame)


print("\n------------------------------------------------------------------------")
# Filtros: se puede filtrzr a traves del uso de condiciones
menores = frame[frame['price'] < 1]
print(menores)


print("\n------------------------------------------------------------------------")
# Crear un DataFrame a partir de un diccionario anidado
# Se toman las keys "principales" como columnas y las keys del diccionario "anidado" como filas. Si falta alguno de los
# valores en algun diccionario se completa con NaN, por ejemplo Red/2011
mesDict = {
    'red': {2012: 800, 2013: 600},
    'white': {2011: 1500, 2012: 800, 2013: 400},
    'Blue': {2011: 300, 2012: 800, 2013: 600}
}
frame_mes = pd.DataFrame(mesDict)
print(frame_mes)


print("\n------------------------------------------------------------------------")
# Trasponer filas: cambiar filas por columnas y viceversa
frame_transpuesto = frame.transpose()
print("Frame original:")
print(frame)

print("\nFrame transpuesto:")
print(frame_transpuesto)


print("\n------------------------------------------------------------------------")
# Operaciones aritmeticas entre DataFrames: Es importante que el índice exista en ambas estructuras, ya que de no ser
# así el valor resultante de la operación será NaN
mesDict = {
    'red': {2012: 800, 2013: 600},
    'white': {2011: 1500, 2012: 800, 2013: 400},
    'Blue': {2011: 300, 2012: 800, 2013: 600}
}

mesDict2 = {
    'red': {2012: 800, 2013: 600},
    'white': {2011: 1500, 2012: 800, 2013: 400},
    'Blue': {2011: 300, 2012: 800, 2013: 600}
}

frame1 = pd.DataFrame(mesDict)
frame2 = pd.DataFrame(mesDict2)

frameSuma = frame1.add(frame2)

print(frameSuma)


print("\n------------------------------------------------------------------------")
# Medidas estadisticas de un DataFrame:
suma = frame1.sum()
promedio = frame1.mean()

print('Suma: \n', suma)
print("\n")

print('Promedio:\n ', promedio)
print("\n")

print('Describe: \n', frame1.describe())


print("\n------------------------------------------------------------------------")
# Tambien existen funciones que permiten analizar la relacion entre series o DataFrames. Por ejemplo la correlacion
# o la covarianza
sec1 = pd.Series([3, 4, 3, 4, 5, 4, 3, 2], [2006, 20007, 2008, 2009, 2010, 2011, 2012, 2013])
sec2 = pd.Series([1, 2, 3, 4, 4, 1, 3, 1], [2006, 20007, 2008, 2009, 2010, 2011, 2012, 2013])

correlacion = sec1.corr(sec2)
covarianza = sec1.cov(sec2)

print('Correlación: ', correlacion, ' / Covarianza: ', covarianza)


# print("\n------------------------------------------------------------------------")
# Exportar a csv
# frame.to_csv('MiDataFrame.csv')

# Exportar a json
# frame.to_json("DataFrameJson.json")

# Importar a csv
# frame = pd.read_csv("MiDataFrame.csv")
# print(frame)

# Leer json
# frame = pd.read_json("DataFrameJson.json"

# SQL

print("\n------------------------------------------------------------------------")
# Visualizacion
# import matpilot.pylot as plt

serie = pd.Series([10, 25, 30, 40], index=["2010", "2011", "2012", "2013"])
serie.plot()
plt.show()

# Grafico de barras
df = pd.DataFrame()
df.plot.bar(x='lab', y='val', rot=0)


# Barras con colores
speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 79, 1.5, 25, 12, 28]

index = ['snail', 'pig', 'elephant',
         'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'speed': speed,
                   'lifespan': lifespan}, index=index)

df.plot.bar(rot=0)


# Ploting pie
df_pie = pd.DataFrame({'mass': [0.330, 4.87, 5.97],
                       'radius': [2439.7, 6051.8, 6378.1]},
                      index=['Mercury', 'Venus', 'Earth'])

plot = df.pie.plot.pie(y='mass', figsize=(5, 5))  # sun solo pie

# plot = df.pie.plot.pie(subplots=True, figsize=(11, 6))  # si se quiere un subplot (dos pie)

plt.show()
