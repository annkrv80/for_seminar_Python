#Напишите для задачи 1 тесты unittest. Проверьтеследующие варианты:
#возврат строки без изменений
#возврат строки с преобразованием регистра без потери символов
#возврат строки с удалением знаков пунктуации
#возврат строки с удалением букв других алфавитов
#возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from Task_01 import del_symbol
import unittest

class TestDelSymbol(unittest.TestCase):
    def test_1(self):
        self.assertEqual(del_symbol('python'),'python', msg= 'Something went wrong')
    
    def test_2(self):
        self.assertEqual(del_symbol('Python'),'python', msg= 'Something went wrong') 
    
    def test_3(self):
        self.assertEqual(del_symbol(': python - is it , not java!!!'),\
                            ' python  is it  not java', msg= 'Something went wrong') 

    def test_4(self):
        self.assertEqual(del_symbol('python это не питон'),'python   ', msg= 'Something went wrong')

    def test_5(self):
        self.assertEqual(del_symbol('Python - это не Питон!!!'), 'python    ', msg= 'Something went wrong') 


if __name__ == '__main__':
    unittest.main(verbosity=2)