#Создайте класс Моя Строка, где:
#будут доступны все возможности str
#дополнительно хранятся имя автора строки и время создания (time.time)
import time

class MyString(str):
    """The created class has access to all the features of the string."""

    def __new__(cls, value, author):
        """Additionally, the class stores the author and time."""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance
    
    def __str__(self) :
        return f"Автов строки {self.author} , время {self.time}"
    
    def __repr__(self):
        return f'MyString({self.author}, {self.time})'
        


if __name__ == '__main__':
    str_1 = MyString('Идет на меня похожий', 'Цветаева')
    print(str_1)
    print(repr(str_1))
    print(str_1.upper())
    print(str_1.title())
    print(str_1.author)
    print(str_1.time)
    help(MyString)
