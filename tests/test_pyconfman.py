from __future__ import print_function

import unittest

from pyconfman import PyConfMan

# Import tested class

class TestPyConfMan(unittest.TestCase):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_01_validate_name(self):
        pyconfman = PyConfMan()
        test_name = 'good_test_name'
        self.assertEqual(test_name, pyconfman.validate_name(test_name))
        test_name = 'bad test_name_space'
        with self.assertRaises(RuntimeError):
            pyconfman.validate_name(test_name)
        test_name = '_bad_test_name_leading_underscore'
        with self.assertRaises(RuntimeError):
            pyconfman.validate_name(test_name)
        test_name = '_bad_test_Name_upper_case'
        with self.assertRaises(RuntimeError):
            pyconfman.validate_name(test_name)
        return

    def test_02(self):
        pass
