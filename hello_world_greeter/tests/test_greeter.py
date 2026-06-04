import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from greeter import greeter

class TestGreeter(unittest.TestCase):
    
    def test_valid_name_greeting(self):
        self.assertEqual(greeter("Sanjeev"), "It is great to meet you, Sanjeev!")

    def test_name_with_whitespace_padding(self):
        self.assertEqual(greeter("   Sanjeev   "), "It is great to meet you, Sanjeev!")

    def test_empty_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            greeter("")

    def test_whitespace_only_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            greeter("     ")

if __name__ == "__main__":
    unittest.main()
    
    