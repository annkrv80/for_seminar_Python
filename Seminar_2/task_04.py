import decimal
import math

while True:

    diam = int(input('Введи диаметр: '))
    if diam <= 1000 : break

decimal.getcontext().prec = 42
sqauer = decimal.Decimal(math.pi * diam * diam / 4)
lenght = decimal.Decimal(math.pi * diam)
print(f'Площадь круга {sqauer}')
print(f'Длина оуружности {lenght}')