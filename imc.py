import math as m
import sys
import os

os.system('clear')

try:
    weight = float(sys.argv[1])
    height = (float(sys.argv[2])) / 100
    if weight == 0 or height == 0:
        print('Solo valores distintos de 0 por favor')
        exit()
    elif len(sys.argv) > 3:
        print('Argumento inválido: ingresa solo dos valores, peso en kg y altura en cm respectivamente.')

except ValueError:
    print('Por favor ingresa un número válido')
    exit()

imc = round((weight / m.pow(height, 2)), 2)

if imc < 18.5:
    print(f'Su IMC es {imc}\nLa clasificación OMS es Bajo Peso\n')
elif 18.5 <= imc < 25:
    print(f'Su IMC es de {imc}\nLa clasificación OMS es Peso Adecuado\n')
elif 25 <= imc < 30:
    print(f'Su IMC es de {imc}\nLa clasificación OMS es Sobrepeso\n')
elif 30 <= imc < 35:
    print(f'Su IMC es de {imc}\nLa clasificación OMS es Obesidad Grado I\n')
elif 35 <= imc < 40:
    print(f'Su IMC es de {imc}\nLa clasificación OMS es Obesidad Grado II\n')
elif imc >= 40:
    print(f'Su IMC es de {imc}\nLa clasificación OMS es Obesidad Grado III\n')