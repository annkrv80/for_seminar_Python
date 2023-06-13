#Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
#ключ — тип элемента,
#значение — список элементов данного типа.

data = ('Hello', 12, 5.14, 'world', 33, True, False )
my_dict = {}
my_dict_2 = {}
my_dict_3 = {}


for item in data:
    if  type(item) in my_dict:
        my_dict[type(item)].append(item)
    else:
        my_dict[type(item)] = [item]
print(my_dict)


for item in data:
    my_dict_2.setdefault(type(item), []).append(item)
print(my_dict_2)

for item in data:
    my_dict_3[type(item)] = my_dict_3.get(type(item)), [] + [item]

print(my_dict_3)