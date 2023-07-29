#Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
#возврат строки без изменений
#возврат строки с преобразованием регистра без потери символов
#возврат строки с удалением знаков пунктуации
#возврат строки с удалением букв других алфавитов
#возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import string

def del_symbol(my_text):
    """
    Function removes all characters from the text except Latin letters and spaces
    >>> del_symbol('python')
    'python'
    >>> del_symbol('Python')
    'python'
    >>> del_symbol(': python - is it , not java!!!')
    ' python  is it  not java'
    >>> del_symbol('python это не питон')
    'python   '
    >>> del_symbol('Python - это не Питон!!!')
    'python    '
    """
    str_chars = string.ascii_letters + ' '
    return ''.join(char for char in my_text.lower() if char in str_chars)


if __name__ =='__main__':
    import doctest
    doctest.testmod(verbose=True)