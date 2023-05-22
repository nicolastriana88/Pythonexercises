number = 10
number += 5 # Suma 5, number = 15
number -= 5 # Resta 5, number = 10 otra vez
number *= 5 # Multiplica por 5, number = 50
number /= 5 # Dividido sobre 5, number = 10 otra vez

number=int(input(f'Cual es valor de {number} en la linea 1: '))
number+=int(input(f'Cual es valor de {number} en la linea 2: '))
number-=int(input(f'Cual es valor de {number} en la linea 3: '))
number*=int(input(f'Cual es valor de {number} en la linea 4: '))
number/=int(input(f'Cual es valor de {number} en la linea 5: '))

print(f'linea 6: {int(number)}')