#Пользователь вводит данные. Сделайте проверку данных
#и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть
#хотя бы одна заглавная буква
# Строку в нижнем регистре в остальных случаях

arg = input('Введите символ: ')
if arg.isdecimal():
    print(f' {arg} целое положительное число')
elif arg.replace('.','').replace('-','').isdecimal() and arg.count('.') == 1 and \
arg.count('-') <= 1 and arg[1:].count('-') == 0:
    print(f' {arg} вещественное число')
else:
    print(arg.lower())