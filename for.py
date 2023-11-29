for num in [1, 2, 3, 4, 5,]:
    print(num)

for letra in "Python":
    print(letra)

suma = 0
for i in range(1, 11):
    suma += 1
    print(suma)

nombres = ["Alice","Bob","Charlie","David"]
for nombre in nombres:
    print(nombre)


datos = {"nombre": "Juan", "edad":30, "ciudad": "Madrid"}
for clave, valor in datos.items():
    print(clave, ":", valor)    