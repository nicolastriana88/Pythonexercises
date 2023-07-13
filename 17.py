import random

def generate_username(first_name, last_name):
    # Obtiene una lista de posibles combinaciones de nombres de usuario
    username_options = [
        first_name + last_name,
        first_name + "_" + last_name,
        first_name + "." + last_name,
        first_name[0] + last_name,
        first_name + str(random.randint(1, 100))
    ]
    
    # Elige una combinación de forma aleatoria
    username = random.choice(username_options)
    
    return username

# Ejemplo de uso
first_name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")

username = generate_username(first_name, last_name)
print("Tu nombre de usuario es:", username)