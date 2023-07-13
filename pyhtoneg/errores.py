try:
  print(x)
except:
  print("Ocurrio una execion")

try:
  print("Hola")
except:
  print("Algo salio mal")
else:
  print("Nada salio mal")

try:
  print(x)
except:
  print("Algo salio mal")
finally:
  print("El 'try except' termino aca") 

  x = -1
if x < 0:
  raise Exception("Disculpe, no hay numeros abajo de cero")

x = "hola"
 
if not type(x) is int:
  raise TypeError("Solo se permiten enteros (integer)") 