#!/usr/bin/python3

import unittest
import pep8

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unittest for rectangle class."""
    
    def setUp(self):
        """setup test"""
        self.rectangle = Rectangle(6, 9, 3, 4, 1)

    def test_to_dict(self):
        """Test for dict repr"""
        exDict = {"id": 1, "width": 6, "height": 9, "x": 3, "y": 4}
        self.assertEqual(self.rectangle.to_dictionary(), exDict)

    

    def tearDown(self):
        """test teardown"""
        del self.rectangle
    
    def test_attr(self):
        """Test creation of Rectangle instance"""
        rengo = Rectangle(5, 10, 2, 3, 1)

        self.assertEqual(rengo.width, 5)
        self.assertEqual(rengo.height, 10)
        self.assertEqual(rengo.x, 2)
        self.assertEqual(rengo.y, 3)
        self.assertEqual(rengo.id, 1)

    def test_create_r(self):
        """Test creation of Rectangle instance"""
        rengod = {"id": 1, "width": 1, "height": 1, "x": 3, "y": 1}
        rengo = Rectangle.create(**rengod)
        self.assertIsInstance(rengo, Rectangle)
        self.assertEqual(rengo.width, 1)
        self.assertEqual(rengo.height, 1)
        self.assertEqual(rengo.x, 3)
        self.assertEqual(rengo.y, 1)
        self.assertEqual(rengo.id, 1)

    def test_et(self):
        """setter"""
        rengo = Rectangle(5, 10)

        rengo.width = 7
        self.assertEqual(rengo.width, 7)

        rengo.height = 15
        self.assertEqual(rengo.height, 15)

        rengo.x = 3
        self.assertEqual(rengo.x, 3)

        rengo.y = 4
        self.assertEqual(rengo.y, 4)

    def test_width_v(self):
        """validation of width value"""
        with self.assertRaises(TypeError):
            rengo = Rectangle(5, "not_an_integer")
        with self.assertRaises(ValueError):
            rengo = Rectangle(5, 0)

    def test_height_v(self):
        """validation of height value"""
        with self.assertRaises(TypeError):
            rengo = Rectangle(5, "not_an_integer")
        with self.assertRaises(ValueError):
            rengo = Rectangle(5, 0) 

    def test_x_v(self):
        """validation of x value"""
        with self.assertRaises(TypeError):
            rengo = Rectangle(5, 5, "not_an_integer")
        with self.assertRaises(ValueError):
            rengo = Rectangle(5, 5, -1)

    def test_y_v(self):
        """validation of y value"""
        with self.assertRaises(TypeError):
            rengo = Rectangle(5, 5, "not_an_integer")
        with self.assertRaises(ValueError):
            rengo = Rectangle(5, 0, -1)

    def test_A(self):
        """Test area method"""
        rengo = Rectangle(5, 10)
        self.assertEqual(rengo.area(), 50)

    def test_A_zero_w(self):
        """Test area method with rectangle zero width"""
        rengo = Rectangle(0, 20)
        self.assertEqual(rengo.area(), 0)

    def test_A_zero_h(self):
        """Test area method with rectangle zero height"""
        rengo = Rectangle(0, 20)
        self.assertEqual(rengo.area(), 0)
    
    def test_A_w_invalid_value(self):
        """Test that width raises ValueError for invalid value"""
        with self.assertRaises(ValueError):
            self.rectangle.width = -10

    def test_A_w_invalid_type(self):
        """Test that width raises TypeError for invalid type"""
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"

    def test_A_h_invalid_value(self):
        """Test that height raises ValueError for invalid value"""
        with self.assertRaises(ValueError):
            self.rectangle.height = -21

    def test_A_h_invalid_type(self):
        """Test that height raises TypeError for invalid type"""
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"

    def test_A_x_invalid_value(self):
        """Test that x raises ValueError for invalid value"""
        with self.assertRaises(ValueError):
            self.rectangle.x = -5

    def test_A_x_invalid_type(self):
        """Test that x raises TypeError for invalid type"""
        with self.assertRaises(TypeError):
            self.rectangle.x = "invalid"

    def test_A_y_invalid_value(self):
        """Test that y raises ValueError for invalid value"""
        with self.assertRaises(ValueError):
            self.rectangle.y = -1

    def test_A_y_invalid_type(self):
        """Test that y raises TypeError for invalid type"""
        with self.assertRaises(TypeError):
            self.rectangle.y = "invalid"

    def test_D(self):
        """Test for display method."""
        exQ = "###\n###\n###\n"
        with self.assertLogs(level='INFO') as cem:
            self.rectangle.display()
        self.assertEqual(cem.output, [exQ])

    def test_Str(self):
        """Test for str method."""
        ex_str = "[Rectangle] (1) 3/4 - 6/9"
        self.assertEqual(str(self.rectangle), ex_str)

    def test_upd_args(self):
        """Test for args method."""
        self.rectangle.update(2, 4, 6, 8, 1)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 6)
        self.assertEqual(self.rectangle.x, 8)
        self.assertEqual(self.rectangle.y, 1)

    def test_upd_with_kwargs(self):
        """Test for updated kwargs method."""
        self.rectangle.update( id=2, width=4, height=6, x=4, y=1)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 6)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 1)

    def test_upd_with_args_n_kwargs(self):
        """Test for updated args and kwargs method."""
        self.rectangle.update( id=2, width=6, height=9, x=4, y=1)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 6)
        self.assertEqual(self.rectangle.height, 9)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 1)

    def runT():
        """Test for running unittest."""
        lod = unittest.TestLoader()
        sut = lod. loadTestsFromTestCase(TestRectangle)
        runn = unittest.TextTestRunner(verbosity=2)
        outcam = runn.run(sut)
        return len(outcam.errors) + len(outcam.failures)
        
    def test_pep8_con(self):
        """Test for pep8 guidelines"""
        pep8sty = pep8.StyleGuide(quiet=True)
        outcome = pep8sty.check_files(['models/rectangle.py'])
        self.assertEqual(outcome.total_errors, 0)

    if __name__ == '__main__':
        unittest.main()
