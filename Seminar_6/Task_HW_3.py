#Добавьте в пакет, созданный на семинаре шахматный модуль.
#Внутри него напишите код, решающий задачу о 8 ферзях. 
#Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
#Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
#Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
from random import randint as rnd



def queen(positions_list):
    for i in range(len(positions_list)-1):
        for j in range(i+1, len(positions_list)):
            x1, y1 = positions_list[i]
            x2, y2 = positions_list[j]
            if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
                return False
    return True
  

def positions():
    posit_list= []
    for i in range(8):
        x = rnd(1, 8)
        y = rnd(1, 8)
        posit_list.append((x, y))  
    return posit_list


def posit_result(p_list):
    posit_result_list.extend(p_list)
    return posit_result_list

def print_result(p_list):
  for i in range(0, len(p_list), 8):
    for j in range(i, min(i + 8, len(p_list))):
        print(p_list[j], end=" ")
    print() 



count = 0
posit_result_list = []
while count < 2:
    positions_list = positions()
    print(positions_list)
    if queen(positions_list):
        posit_result(positions_list)
        print('True')
        count += 1
    else:
        print('False')
print_result(posit_result_list)





