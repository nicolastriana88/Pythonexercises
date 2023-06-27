def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 1, 2, 5, 6, 3, 4]
resultado = eliminar_duplicados(mi_lista)
print(resultado)