data = input('Ведите целые числа через знак /: ')
value_1, key_1, key_2, *value_2 = data.split('/')
my_dict = {key_1: value_1, key_2:tuple(value_2)}
print(my_dict)