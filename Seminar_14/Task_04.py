#Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
#возврат строки без изменений
#возврат строки с преобразованием регистра без потери символов
#возврат строки с удалением знаков пунктуации
#возврат строки с удалением букв других алфавитов
#возврат строки с учётом всех вышеперечисленных пунктов
#import pytest
from Task_01 import del_symbol

def test_1():
    assert del_symbol('python') == 'python', 'Something went wrong'
    
def test_2():
    assert del_symbol('Python') == 'python','Something went wrong'
    
def test_3():
    assert del_symbol(': python - is it , not java!!!') == ' python  is it  not java', 'Something went wrong'

def test_4():
    assert del_symbol('python это не питон') == 'python   ','Something went wrong'

def test_5():
    assert del_symbol('Python - это не Питон!!!') ==  'python    ', 'Something went wrong'



#if __name__ == '__main__':
   # pytest.main(['-v'])


