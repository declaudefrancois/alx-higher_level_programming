#!/usr/bin/python3
"""
    Rectangle class test.
"""
from models.rectangle import Rectangle
from tests.test_models import basetestcase
from contextlib import redirect_stdout
import io


class TestRectangle(basetestcase.BaseTestCase):
    """Rectangle test Case.
    """

    def test_should_inherit_base(self):
        """Instance of Rectangle should be Base
        """
        b1 = Rectangle(10, 12)
        self.assertIsInstance(b1, Rectangle)

    def test_all_atttribute_set(self):
        """Attributes should be set correctly and accessible.
        """
        w = 4
        h = 8
        x = 12
        y = 24
        id = 12

        r1 = Rectangle(w, h, x, y, id)
        self.assertEqual(r1.width, w)
        self.assertEqual(r1.height, h)
        self.assertEqual(r1.x, x)
        self.assertEqual(r1.y, y)
        self.assertEqual(r1.id, id)

    def test_raise_typerErrors(self):
        """Should raise a TypeError if user is
        trying to set a non int value.
        """
        with self.assertRaises(TypeError) as ctx:
            Rectangle("10", 10, 1, 2)

        e = ctx.exception
        self.assertIsInstance(e, TypeError)
        self.assertEqual("{}".format(e), "width must be an integer")

        with self.assertRaises(TypeError) as ctx:
            Rectangle(12, [], 1, 2)

        e = ctx.exception
        self.assertIsInstance(e, TypeError)
        self.assertEqual("{}".format(e), "height must be an integer")

        self.assertRaisesRegex(TypeError,
                               "x must be an integer",
                               Rectangle, 12, 12, [], 2)
        self.assertRaises(TypeError,
                          "y must be an integer",
                          Rectangle, 12, 12, 14, "2")

    def test_raise_value_errors(self):
        """Should raise if width <= 0 or
        height <= 0 or x < 0 or y < 0.
        """
        gt_err = "{} must be > 0"
        gte_err = "{} must be >= 0."
        self.assertRaisesRegex(ValueError,
                               "must be >= 0",
                               Rectangle, 1, 1, -1, -4)
        self.assertRaisesRegex(ValueError,
                               "must be >= 0",
                               Rectangle, 1, 1, 1, -4)

        self.assertRaisesRegex(ValueError,
                               "must be > 0",
                               Rectangle, -1, 1, 1, -4)
        self.assertRaisesRegex(ValueError,
                               "must be > 0",
                               Rectangle, 1, 0, 1, 45)

    def test_required_positional_args(self):
        """Width and height are required.
        """
        err = ("TypeError: __init__() missing 2 "
               "required positional arguments: "
               "'width' and 'height'")
        self.assertRaises(TypeError,
                          err,
                          Rectangle)

    def test_rectangle_area(self):
        """Area calculation shoudl be correct.
        """
        r1 = Rectangle(4, 4)
        self.assertEqual(r1.area(), 16)

        r2 = Rectangle(23, 3)
        self.assertEqual(r2.area(), 69)

    def test_display(self):
        """Rectangle shoud be displayed with the character #.
        """
        r1 = Rectangle(4, 6)
        with redirect_stdout(io.StringIO()) as f:
            r1.display()

        self.assertEqual(f.getvalue(), "####\n" * 6)

        r1 = Rectangle(2, 2)
        with redirect_stdout(io.StringIO()) as f:
            r1.display()

        self.assertEqual(f.getvalue(), "##\n" * 2)

    def test_display1(self):
        """Rectangle shoud be displayed with the character #.
        """
        r1 = Rectangle(2, 3, 2, 2)
        with redirect_stdout(io.StringIO()) as f:
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n" + "  ##\n" * 3)

        r1 = Rectangle(3, 2, 1, 0)
        with redirect_stdout(io.StringIO()) as f:
            r1.display()
        self.assertEqual(f.getvalue(), " ###\n" * 2)

    def test_update(self):
        """Test update method positional args.
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(99, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.id, 99)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 5, 10)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 10)

    def test_update1(self):
        """Test update with keworded/non-keyworded args.
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)

    def test_to_dictionary(self):
        """Should return a dictionary with all keys set.
        """
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        self.assertIsInstance(r1_dict, dict)
        self.assertEqual(
            r1_dict,
            {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        )
