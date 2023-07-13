def mi_funcion(modelo):
  print("VW " + modelo)
mi_funcion("Jetta")
mi_funcion("Polo")
mi_funcion("Rabbit")
mi_funcion("Passat")

def mi_funcion(marca, modelo):
  print(marca + " " + modelo)
mi_funcion("Ford", "Mustang")
mi_funcion("Chevrolet", "Camaro")

def mi_funcion(marca, modelo):
  print(marca + " " + modelo)
mi_funcion("Ford")
mi_funcion("Chevrolet")

def mi_funcion(*marcas):
  print("Mi marca preferida es " + marcas[0])
 
mi_funcion("Ford", "Toyota", "VW")


def mi_funcion(marca1, marca2, marca3):
  print("La marca mas vendida es " + marca3)
 
mi_funcion(marca1 = "Ford", marca2 = "Toyota", marca3 = "VW")

def mi_funcion(**marca):
  print("Mi marca preferida es " + marca["marca"])
mi_funcion(marca= "Ford",modelo= "Mustang")