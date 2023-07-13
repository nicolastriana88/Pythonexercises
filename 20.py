from random import randint 
start = 1
end = 100

value =randint(start,end)

print("Escoge un numero entre", start, "y", end)

guess = None

while guess != value:
    text = input("Adivina el numero: ")
    guess =int(text)

    if guess < value:
        print("El numero es menor")
    elif guess > value:
        print("El numero es mayor")

print("Ganaste ese era el numero")     