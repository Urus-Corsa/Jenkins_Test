import unittest
from app import Square

class TestClass(unittest.TestCase):
    
    def test_area(self):
        sq = Square(2)
        self.assertEqual(sq.area(), 4, f'Area of a square with side {sq.side} should be equal to {sq.area()}')

    def test_perimeter(self):
        sq = Square(2)
        self.assertEqual(sq.perimeter(), 16, f'Perimeter of a square with side {sq.side} should be equal to {sq.perimeter()}')    

if __name__ == '__main__':
    unittest.main()
