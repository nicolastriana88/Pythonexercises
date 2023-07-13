def puntuacion(clase):
    return sum(clase) / len(clase)

clase_input = input("Ingresa las calificaciones de la clase separadas por espacios: ")
clase = [float(x) for x in clase_input.split()]

media = puntuacion(clase)
print("La puntuacion de la clase es", media)


