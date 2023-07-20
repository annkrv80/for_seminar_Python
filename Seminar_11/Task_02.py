#Создайте класс Архив, который хранит пару свойств.
#Например, число и строку.
#При нового экземпляра класса, старые данные из ранее
#созданных экземпляров сохраняются в пару списков архивов
#list-архивы также являются свойствами экземпляра

class Archive:
    """The Archive class stores information about a number and a string."""
    my_list_number = []
    my_list_srt = []
    def __init__(self, number, string):
        """The created instances are saved in a pair of list archives"""
        self.number = number
        self.string = string
        self.my_list_number.append(number)
        self.my_list_srt.append(string)

    def __str__(self):
        return f'Экземпляр класса Archive с числом {self.number} и строкой {self.string}'
    
    def __repr__(self):
        return f'Archive ({self.number}, {self.string})'



if __name__ == '__main__':
    a = Archive(4, 'four')
    #print(f'{a.my_list_number}\n{a.my_list_srt}')
    print(a)
    print(repr(a))
    b = Archive(5, 'five')
    #print(f'{b.my_list_number}\n{b.my_list_srt}')
    print(b)
    print(repr(b))
    print(f'Документация метода {b.__init__.__doc__}')
    