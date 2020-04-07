# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: zhiqiang huang
"""
import unittest
from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalid(self):
        self.assertEqual(classifyTriangle(-1, 2, 4), 'InvalidInput')  # one input is negative
        self.assertEqual(classifyTriangle(0, 3, 3), 'InvalidInput')  # one input is zero
        self.assertEqual(classifyTriangle('a', 199, 200), 'InvalidInput')  # one input is equal to 200
        self.assertEqual(classifyTriangle(5, 199, 201), 'InvalidInput')  # one input is greater than 200

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(2, 4, 6), 'NotATriangle')  # sum of two sides is equal to the third side
        self.assertEqual(classifyTriangle(2, 4, 7), 'NotATriangle')  # sum of two sides is smaller than the third side

    def testRightTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'RightScalene')
        """sum of any two sides equals the square of the third side with one input sequence"""
        self.assertEqual(classifyTriangle(5, 3, 4), 'RightScalene')
        """sum of any two sides equals the square of the third side with another input sequence"""

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')  # every sides are equal

    def testIsoceles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')
        """two sides are equal but the third side is not with one input sequence"""
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles')
        """two sides are equal but the third side is not with another input sequence"""

    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 5, 6), 'Scalene')
        """ all of the sides are not equal with one input sequence"""
        self.assertEqual(classifyTriangle(5, 3, 6), 'Scalene')
        """ all of the sides are not equal with another input sequence"""
        self.assertEqual(classifyTriangle(3, 4, 5), 'RightScalene')
        """ all of the sides are not equal but satisfy with the requirement of right angle"""


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
