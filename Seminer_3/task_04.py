#Создайте вручную список с повторяющимися элементами.
#Удалите из него все элементы, которые встречаются дважды

my_list = [2, 3, 2, 4, 4, 5, 7, 6, 7, 7]

for item in my_list:
    if my_list.count(item) == 2:
       res = item
    while res in my_list:
        my_list.remove(res)
print(my_list)
