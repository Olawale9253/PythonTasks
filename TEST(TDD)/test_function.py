import unittest
import function

class TestCubeFunction(unittest.TestCase):

    def test_that_cube_function_exists(self):
        function.cube(3)
    def test_that_cube_function_return_correct_result(self):
        actual = function.cube(3)
        expected = 27
        self.assertEqual(actual, expected)
#        actual = function.cube(5)
#        expected = 125
#        self.assertEqual(actual, expected)
#
#    def test_that_cube_function_return_invalid_data_type_with_wrong_input(self):
#        actual = function.cube("musa")
#        expected = "invalid input"
#        self.assertEqual(actual, expected)

