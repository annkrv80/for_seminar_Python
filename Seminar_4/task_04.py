#Функция получает на вход список чисел.
#Отсортируйте список по убыванию суммы цифр

def get_sum(num):
    return sum(map(int, str(num)))


list_number = [22, 2, 44, 111, 125]
print(sorted(list_number, key=get_sum, reverse=True))

def get_dict(lst:list):
    result_dict = dict(zip(map(get_sum, lst), lst))
    return sorted(result_dict.items(),key=lambda x: x[0], reverse=True)


print(get_dict(list_number))