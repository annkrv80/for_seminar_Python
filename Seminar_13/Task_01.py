#Создайте функцию, которая запрашивает числовые данные от
#пользователя до тех пор, пока он не введёт целое или вещественное число.
#Обрабатывайте не числовые данные как исключения.

def input_number():
    while True:
        num = input('Введите целое или ыещественное число: ')
        try:
            num = int(num)
            break
        except ValueError as e:
            print(e)
        try:
            num = float(num)
            break
        except ValueError as e:
            print(e)
    return num

if __name__ == '__main__':
    print(input_number())