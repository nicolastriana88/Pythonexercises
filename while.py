contador = 1
while contador <= 5:
 print(contador)
 contador += 1

numero = -1
while numero != 0:
    numero = int(input("Ingrese un numero (0 para salir): "))


n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("El factorial es:", fact)

dato = 2
while dato <= 10:
   print(dato)
   dato += 2

import random

secreto = random.randint(1, 100)
adivinanza = None

while adivinanza != secreto:
   adivinanza = int(input("Adivina el numero secreto (entre 1 y 100)"))
   if adivinanza < secreto:
      print("Demasiado bajo.")
   elif adivinanza > secreto:
      print("Demasiado alto.")
   else:
      print("!Correcto! !Has adivinado el numero secreto!")