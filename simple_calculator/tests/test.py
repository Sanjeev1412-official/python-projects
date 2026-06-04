import unittest
from calculator import add,sub,mul,div

class TestCalculatorEngine(unittest.TestCase):

    def test_addition(self):
        """Should correctly compute sums including floating points."""
        self.assertEqual(add(10, 5), 15.0)
        self.assertEqual(add(-1, 1), 0.0)

    def test_subtraction(self):
        """Should correctly compute differences."""
        self.assertEqual(sub(10, 5), 5.0)

    def test_multiplication(self):
        """Should correctly compute products."""
        self.assertEqual(mul(4, 2.5), 10.0)

    def test_division(self):
        """Should compute normal quotients cleanly."""
        self.assertEqual(div(10, 2), 5.0)

    def test_division_by_zero_raises_exception(self):
        """Should explicitly raise a ZeroDivisionError for zero denominators."""
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

if __name__ == "__main__":
    unittest.main()