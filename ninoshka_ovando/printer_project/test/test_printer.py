import unittest
from src.figure import Rectangle, Triangle, Rhombus
from test.test_data import *


class Test(unittest.TestCase):

    def test_printer_triangle_height_3(self):
        triangle = Triangle("Triangle", 3, "%")

        self.assertEqual(triangle.output_shape, TRIANGLE_3)

    def test_printer_triangle_height_9(self):
        triangle = Triangle("Triangle", 9, "*")

        self.assertEqual(triangle.output_shape, TRIANGLE_9)

    def test_printer_rectangle_5_4(self):
        rectangle_5_4 = Rectangle("Rectangle", 5, 4,  "%")

        self.assertEqual(rectangle_5_4.output_shape, RECTANGLE_5_4)

    def test_printer_rectangle_7_3(self):
        rectangle_7_3 = Rectangle("Rectangle", 7, 3, "*")

        self.assertEqual(rectangle_7_3.output_shape, RECTANGLE_7_3)

    def test_printer_rhombus_3(self):
        rhombus_3 = Rhombus("Rhombus", 3,  "*")

        self.assertEqual(rhombus_3.output_shape, RHOMBUS_3)

    def test_printer_rhombus_9(self):
        rhombus_9 = Rhombus("Rhombus", 9, "%")

        self.assertEqual(rhombus_9.output_shape, RHOMBUS_9)