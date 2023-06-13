#Вручную создайте список с целыми числами, которые
#повторяются. Получите новый список, который содержит
#уникальные (без повтора) элементы исходного списка. 

my_list = [2, 3, 5, 2, 6, 7, 10, 7]

my_list_2 = [*set(my_list)] # * оператор распаковки
print(my_list_2)

result = set(my_list)

print(result)

result_2 = []
for item in my_list:
    if my_list.count(item) == 1:
        result_2.append(item)

print(result_2)

result_3 = []

for item in my_list:
    if item not in result_3:
        result_3.append(item)
print(result_3)