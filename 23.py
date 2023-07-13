mi_tupla = ("Juan", 25, "Inglaterra")
nombre, edad, pais = mi_tupla
print(nombre)  # Output: Juan
print(edad)    # Output: 25
print(pais)    # Output: Inglaterra
#Desempaquetado de tuplas: Puedes asignar los elementos de 
# una tupla a variables individuales en una sola línea.


tupla1 = (1, 2, 3)
tupla2 = (1, 2, 4)
print(tupla1 < tupla2)  # Output: True

#Comparación de tuplas: Puedes comparar tuplas utilizando operadores de comparación, 
# como <, >, <= y >=. Python compara los elementos en orden secuencial y devuelve el resultado
#  basado en la primera diferencia encontrada.

mi_tupla2 = (1, 2, 2, 3, 4, 2)
print(mi_tupla2.count(2))     # Output: 3
print(mi_tupla2.index(3))     # Output: 3


#Métodos de tuplas: Las tuplas en Python tienen algunos métodos 
# útiles, como count() y index(). El método count()
#  devuelve el número de veces que aparece un elemento en la tupla,
#  mientras que el método index() devuelve el índice de la primera aparición de un elemento.

mi_lista = [1, 2, 3]
mi_tupla3 = tuple(mi_lista)
print(mi_tupla3)  # Output: (1, 2, 3)

otra_tupla = (4, 5, 6)
otra_lista = list(otra_tupla)
print(otra_lista)  # Output: [4, 5, 6]

#Conversión entre listas y tuplas: Puedes convertir 
# una lista en una tupla utilizando la función tuple() y viceversa utilizando la función list().