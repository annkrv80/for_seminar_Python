#Функция принимает на вход три списка одинаковой длины:
#имена str,
#ставка int,
#премия str с указанием процентов вида «10.25%».
#Вернуть словарь с именем в качестве ключа и суммой
#премии в качестве значения.
#Сумма рассчитывается как ставка умноженная на процент премии.


def remineration(name, salery, bonus):
    sal = [(i[0] *float(i[1].strip('%'))) / 100 for i in zip(salery, bonus)]
    return dict(zip(name, sal))   


names = ['Ivan', 'Petr', 'Sergey']
salesies = [125_000, 96_000, 135_000]
bonuses = ['10.25%', '15.50%', '25.30%' ]

print(remineration(names, salesies, bonuses))


def remineration_2(name, salery, bonus):
    salary_dict = {}
    for name, salary, bonus in zip(name, salery, bonus):
        salary_dict[name] = salary * float(bonus[:-1]) / 100
    return salary_dict

print(remineration_2(names, salesies,bonuses))