"""pares = 0
while pares < 50:
   pares += 2
   print(pares)"""

"""impares = 1
while impares < 99:
   print(impares)
   impares += 2"""

"""num = 0
while num < 200:
 num += 5
 print(num)"""

"""a = -100
while a <= -10:
 print(a)
 a += 1"""

"""num = 3
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1"""

"""num = float(input("Ingresa un número: "))

while num == 0:
    num = float(input("El número debe ser diferente de cero. Ingresa otro número: "))

if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")"""


"""sumatoria = 0
i = 0

while i <= 100:
    if i % 3 == 0:
        sumatoria += i
    i += 1

print("La sumatoria de los múltiplos de 3 entre 0 y 100 es:", sumatoria)"""

suma = 0
cantidad_numeros = 0

while True:
    numero = input("Ingrese un número (o 'fin' para salir): ")
    if numero.lower() == "fin":
        break
    suma += float(numero)
    cantidad_numeros += 1

if cantidad_numeros > 0:
    promedio = suma / cantidad_numeros
    print("La suma de los números ingresados es:", suma)
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se ingresaron números")
   