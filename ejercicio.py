import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv")
print(titanic.head())

print(titanic.columns)

# seleccionar la edad de los pasageros del titanic

ages = titanic["Age"]
print(ages)

# Cada columna de a DataFramees un Series. Cuando se selecciona una sola columna,
# el objeto devuelto es un pandas Series. Podemos verificar esto comprobando el tipo de salida:

print(type(titanic["Age"]))

# DataFrame.shapees un atributo (recuerde tutorial sobre lectura y escritura ,
# no use paréntesis para atributos) de un pandas Seriesy que DataFramecontiene el número de
# filas y columnas: (nrows, ncolumns). Una serie de pandas es unidimensional y solo se devuelve
# el número de filas.

print(titanic["Age"].shape)

# Me interesa la edad y el sexo de los pasajeros del Titanic.

ages_sex = titanic[["Age", "Sex"]]
print(ages_sex)

#Para seleccionar varias columnas, use una lista de nombres de columna dentro de los
# corchetes de selección [].

# El tipo de datos devuelto es un DataFrame de pandas:

print(type(titanic[["Age", "Sex"]]))

print(titanic[["Age", "Sex"]].shape)

# Me interesan los pasajeros mayores de 35 años.

above_35 = titanic[titanic["Age"] > 35]
above_35_2 = ages_sex[ages_sex["Age"] > 35]
print(above_35)
print(above_35_2)

# La condición dentro de los corchetes de selección verifica qué filas tiene la columna un valor mayor que
print(titanic["Age"] > 35)

# Estoy interesado en los pasajeros del Titanic de las clases de cabina 2 y 3.

class_23 = titanic[titanic["Pclass"].isin([2,3])]
print(class_23)

# otra forma pero en ves de .isin es con el operador or "|"

class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23)

# Quiero trabajar con datos de pasajeros para los que se conoce la edad.
# La notna()función condicional devuelve un Truepara cada fila, los valores no son un Nullvalor. Como tal,
# esto se puede combinar con los corchetes de selección []para filtrar la tabla de datos.

age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na.head())
print(age_no_na.shape)



# ¿Cómo selecciono filas y columnas específicas de un DataFrame?

# Me interesan los nombres de los pasajeros mayores de 35 años.

#En este caso, se crea un subconjunto de filas y columnas de una vez y ya no basta con usar corchetes de
# selección []. Los operadores loc/ ilocson obligatorios delante de los corchetes de selección [].
# Al usar loc/ iloc, la parte antes de la coma son las filas que desea y la parte después de la coma son
# las columnas que desea seleccionar.

#Cuando utilice nombres de columnas, etiquetas de filas o una expresión de condición, utilice el
# loc operador delante de los corchetes de selección []. Tanto para la parte anterior como posterior a la coma,
# puede utilizar una sola etiqueta, una lista de etiquetas, un segmento de etiquetas, una expresión condicional o
# dos puntos. El uso de dos puntos especifica que desea seleccionar todas las filas o columnas.

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names.head(50))

# Me interesan las filas 10 a 25 y las columnas 3 a 5.
a = titanic.iloc[9:25, 2:5]
print(a)


# Una vez más, se crea un subconjunto de filas y columnas de una sola vez y ya no basta con usar corchetes
# de selección []. Cuando esté específicamente interesado en ciertas filas y / o columnas en función de su
# posición en la tabla, utilice el ilocoperador delante de los corchetes de selección [].


# Al seleccionar filas y / o columnas específicas con loc o iloc, se pueden asignar nuevos valores a los
# datos seleccionados. Por ejemplo, para asignar el nombre anonymousa los primeros 3 elementos de la tercera
# columna:

titanic.iloc[0:3, 3] = "anonymous"
print(titanic["Name"])