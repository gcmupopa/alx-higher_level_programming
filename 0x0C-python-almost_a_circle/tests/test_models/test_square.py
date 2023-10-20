#!/usr/bin/python3

import unittest
import pep8

from models.square import Square

class TestSquare(unittest.TestCase):
    """Unittest for square class."""
    
    def setUp(self):
        """setup test"""
        self.square = Square(6, 3, 4, 1)

    def test_to_dict(self):
        """Test for dict repr"""
        exDict = {"id": 1, "size": 6, "x": 3, "y": 4}
        self.assertEqual(self.square.to_dictionary(), exDict)

    def tearDown(self):
        """test teardown"""
        del self.square

    def test_A(self):
        """Test area method"""
        sqe = Square(10, 10)
        self.assertEqual(self.square.area(), 100)

    def test_create_sq(self):
        """Test creation of square instance"""
        sqod = {"id": 1, "size": 10, "x": 3, "y": 1}
        sqe = Square.create(**sqod)
        self.assertIsInstance(sqe, Square)
        self.assertEqual(sqe.size, 10)
        self.assertEqual(sqe.x, 3)
        self.assertEqual(sqe.y, 1)
        self.assertEqual(sqe.id, 1)
    

    def test_A_x_invalid_value(self):
        """Test that x raises ValueError for invalid value"""
        with self.assertRaises(ValueError):
            self.square.x = -5

    def test_A_x_invalid_type(self):
        """Test that x raises TypeError for invalid type"""
        with self.assertRaises(TypeError):
            self.square.x = "invalid"

    def test_A_y_invalid_value(self):
        """Test that y raises ValueError for invalid value"""
        with self.assertRaises(ValueError):
            self.square.y = -1

    def test_A_y_invalid_type(self):
        """Test that y raises TypeError for invalid type"""
        with self.assertRaises(TypeError):
            self.square.y = "invalid"

    def test_D(self):
        """Test for display method."""
        exQ = ("###\n###\n###\n")
        with unittest.mock.patch("built.print") as mopr:
            self.square.display()
            mopr.assert_called_once_with(exQ)

    def test_Str(self):
        """Test for str method."""
        ex_str = "[Square] (10) 1/2 - 5"
        self.assertEqual(str(self.square), ex_str)

    def test_upd_args(self):
        """Test for args method."""
        self.square.update(2, 4, 6, 8)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.width, 4)
        self.assertEqual(self.square.height, 4)
        self.assertEqual(self.square.x, 6)
        self.assertEqual(self.square.y, 8)

    def test_upd_with_kwargs(self):
        """Test for updated kwargs method."""
        self.square.update(id=2, width=6, height=6, x=4, y=1)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.width, 6)
        self.assertEqual(self.square.height, 6)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square, 1)

    def test_upd_with_args_n_kwargs(self):
        """Test for updated args and kwargs method."""
        self.square.update(id=2, width=6, height=6, x=4, y=1)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.width, 6)
        self.assertEqual(self.square.height, 6)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 1)

    def test_sqe_cr(self):
        """Test for square creation"""
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNone(square.id)

    def test_sqe_repr(self):
        """Test for square str repr"""
        square = Square(10, id=1, x=1, y=3)
        self.assertEqual(str(square), "[Square] (1) 1/3 - 10")

    def test_sqe_ss(self):
        """Test for square setter"""
        square = Square(5)

        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

        with self.assertRaises(TypeError):
            square.size = "invalid"

        with self.assertRaises(ValueError):
            square.size = -9

    def test_upd_args(self):
        """Test square with args"""
        square = Square(5)

        square.update(1, 7, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

        with self.assertRaises(ValueError):
            square.update(1, 7, 3)

    def test_upd_kwargs(self):
        """Test square with kwargs"""
        square = Square(5)

        square.update(id=1, size=7, x=3, y=4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_upd_args_n_kwargs(self):
        """Test square with args and kwargs"""
        square = Square(5)

        square.update(1, 7, x=3, y=4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_upd_wout_args_n_kw(self):
        """Test for sq without args and kwargs"""
        square = Square(5)

        with self.assertRaises(ValueError):
            square.update()

    def test_upd_w_invalid_args(self):
        """Test for sq with invalid args"""
        square = Square(5)

        with self.assertRaises(ValueError):
            square.update(1, 7, 3, 4, 9)


    def test_upd_w_invalid_args_n_kw(self):
        """Test for sq with inalid args and kwargs"""
        square = Square(5)

        with self.assertRaises(TypeError):
            square.update(id=1, size=7, x=3, y=4, invalid=6)

    def runT():
        """Test for running unittest."""
        lod = unittest.TestLoader()
        sut = lod. loadTestsFromTestCase(TestSquare)
        runn = unittest.TextTestRunner(verbosity=2)
        outcam = runn.run(sut)
        return len(outcam.errors) + len(outcam.failures)
        
    def test_pep8_con(self):
        """Test for pep8 guidelines"""
        pep8sty = pep8.StyleGuide(quiet=True)
        outcome = pep8sty.check_files(['models/square.py'])
        self.assertEqual(outcome.total_errors, 0)

    if __name__ == '__main__':
        unittest.main()
