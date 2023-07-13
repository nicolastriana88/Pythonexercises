def fibonacci(data):
    n1 = 0
    n2 = 1
    suma = 0 + 1
    for item in range(data):
        print(suma)
        suma = n1 + n2
        n1 = n2
        n2 = suma

fibonacci(10)