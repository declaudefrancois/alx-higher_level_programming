#!/usr/bin/python3
"""Defined the Test class for Rectangle.
"""
from models.square import Square
from tests.test_models import basetestcase
from models.rectangle import Rectangle
from contextlib import redirect_stdout
import io


class TestSquare(basetestcase.BaseTestCase):
    """Square Test class.
    """
    def test_should_be_a_rectangle(self):
        """A Square must be a Rectangle instance.
        """
        s1 = Square(5)
        self.assertIsInstance(s1, Rectangle)

    def test_should_have_attr_set(self):
        """The Square contructor must properly set Attributes.
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsInstance(s1.id, int)

        s1 = Square(2, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)
        self.assertIsInstance(s1.id, int)

        s1 = Square(3, 1, 3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 3)
        self.assertIsInstance(s1.id, int)

    def test_area(self):
        """The area should be correct.
        """
        self.assertEqual(Square(4).area(), 16)
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(9).area(), 81)

    def test_str_rpr_human(self):
        """The string representation of a square
        must be [Square] (<id>) <x>/<y> - <size>.
        """
        s1 = Square(5)
        with redirect_stdout(io.StringIO()) as f:
            print(s1)
        self.assertRegex(f.getvalue(), r"\[Square\] \(\d+\) 0\/0 - 5")

        s1 = Square(3, 1, 3, 10)
        with redirect_stdout(io.StringIO()) as f:
            print(s1)
        self.assertRegex(f.getvalue(), r"\[Square\] \(10\) 1\/3 - 3")

    def test_getter_setter(self):
        """Size should be accessible for reading and writting.
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 45
        self.assertEqual(s1.size, 45)

    def test_udpate(self):
        """Update method should properly assign attributes.
        """
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def test_to_dictioanry(self):
        """Should return a dicionary with all keys.
        """
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        self.assertIsInstance(s1_dict, dict)
        self.assertEqual(s1_dict, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
