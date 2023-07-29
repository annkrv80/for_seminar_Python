#Создайте функцию, которая удаляет из текста все символы
#кроме букв латинского алфавита и пробелов.
#Возвращается строка в нижнем регистре.
import string

def del_symbol(my_text):  
    str_chars = string.ascii_letters + ' '
    return ''.join(char for char in my_text.lower() if char in str_chars)


if __name__ =='__main__':
    text = 'Hello world Привет Anna '
    print(del_symbol(text))