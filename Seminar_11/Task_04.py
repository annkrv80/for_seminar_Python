from random import randint

#Создайте класс Матрица. Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

START = 0
END = 100

class Matrix:
    
    matrix = []
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[randint(START, END) for _ in range(self.columns)] for _ in range(self.rows)]

    
    
    def __add__(self, other): 
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]         
            return result
        else:
            print("Количество рядов и/или столбцов не совпадают")
      
    
    def __sub__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result
        else:
            print("Количество рядов и/или столбцов не совпадают")
    
    def __mul__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, other.columns)   
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result
        else:
            print("Количество рядов и/или столбцов не совпадают")

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join([str(el) for el in row]) + '\n'
        return matrix_str
    

if __name__ == '__main__':
    m_1 = Matrix(2,2)
    m_2 = Matrix(2,2)
    print(m_1)
    print(m_2)
    m_3 = m_1 + m_2
    print(m_3)
    m_4 = m_1 - m_2
    print(m_4)
    m_5 = m_1 * m_2
    print(m_5)
    print(m_1 == m_2)
    