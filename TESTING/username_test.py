from unittest import TestCase

import username

class Test_Username(TestCase):

    def test_that_username_exist(self):
        username.valid_username("Olawale")

    
    def test_that_username_contain_minimum_of_3_numbers(self):
        username_contains_number = username.valid_username("Olawale")
        self.assertTrue( username_contains_number)
