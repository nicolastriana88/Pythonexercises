## TUPLAS

# Definición de una tupla
mi_tupla = ("manzana", "banana", "cereza")

# Accediendo a los elementos de la tupla
print(mi_tupla[0])  # Output: manzana
print(mi_tupla[1])  # Output: banana
print(mi_tupla[2])  # Output: cereza

# Intentando modificar un elemento de la tupla (esto generará un error)
mi_tupla[0] = "pera"  # Genera un TypeError

# Iterando sobre una tupla
for elemento in mi_tupla:
    print(elemento)

# Longitud de una tupla
print(len(mi_tupla))  # Output: 3

# Concatenación de tuplas
otra_tupla = ("dátil", "uva")
tupla_concatenada = mi_tupla + otra_tupla
print(tupla_concatenada)  # Output: ("manzana", "banana", "cereza", "dátil", "uva")
