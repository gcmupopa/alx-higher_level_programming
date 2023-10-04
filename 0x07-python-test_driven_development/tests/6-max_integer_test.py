import unittest
import importlib.util

"""
This is a module that defines max integer
"""

max = importlib.import_module("6-max_integer")

max_integer = max.max_integer

class MaxInt_Test(unittest.TestCase):
    """
    Test case for max int function
    """

    def testEMPTY(self):
        """
        Test for an empty list
        Outcome should be none
        
        """
        outcome = max_integer([])
        self.assertIsNone(outcome, "Expected None for an empty list")

    def test_mixed(self):
        """
        Test for mixed positive and negative integers
        Outcome should be max value in list
        
        """
        nums = [1, -2, 3, -4, 5]
        outcome = max_integer(nums)
        self.assertEqual(outcome, 5, "Expected the max value 5")

    def test_duplicate(self):
        """
        Test for duplicate numbers
        Outcome should be max value in list
        
        """
        nums = [1, 2, 3, 3, 2, 1]
        outcome = max_integer(nums)
        self.assertEqual(outcome, 3, "Expected the max value 3")

    def test_single(self):
        """
        Test for single elem
        Outcome should be value of elem
        
        """
        nums = [10]
        self.assertEqual(nums, 10, "Expected the max value 10")

    def test_negative(self):
        """
        Test for negative numbers
        Outcome should be max value in list
        
        """
        nums = [-1, -2, -3, -4, -5]
        outcome = max_integer(nums)
        self.assertEqual(outcome, -1, "Expected the max value -1")

    def test_positive(self):
        """
        Test for positive numbers
        Outcome should be max value in list
        
        """
        nums = [1, 2, 3, 4, 5]
        outcome = max_integer(nums)
        self.assertEqual(outcome, 5, "Expected the max value 5")
