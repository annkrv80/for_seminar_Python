#Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
#символ из Unicode, а значением — целое число.
#Диапазон пар ключ-значение от наименьшего из введённых
#пользователем чисел до наибольшего включительно.

def create_dict(string_number):
    a, b = map(int, string_number.split(" "))
    dict_numbers = {}
    for i in range(min(a, b), max(a, b) + 1):
        dict_numbers[chr(i)] = 1
    return dict_numbers


num = input('Введите два число через пробел: ')
print(create_dict(num))
