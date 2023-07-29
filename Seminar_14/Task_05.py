#На семинарах по ООП был создан класс прямоугольник
#хранящий длину и ширину, а также вычисляющую периметр,
#площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
#Напишите 3-7 тестов unittest для данного класса.
from Task_02_08 import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.p1 = Rectangle(5,6)
        self.p2 = Rectangle(4, 6)
       

    def test_create(self):
        self.assertEqual(self.p1, Rectangle(5, 6))

    def test_perimetr(self):
        self.assertEqual(self.p1.perimeter_rectagle(), 22)

    def test_area(self):
        self.assertEqual(self.p1.area_rectagle(), 30)

    def test_add(self):
        self.assertEqual(self.p1.__add__(self.p2), (Rectangle(15, 6)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
    