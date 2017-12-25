import unittest

import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(15, calc.add(10, 5))
        self.assertEqual(0, calc.add(-1, 1))
        self.assertEqual(-2, calc.add(-1, -1))

    def test_subtract(self):
        self.assertEqual(5, calc.subtract(10, 5))
        self.assertEqual(-2, calc.subtract(-1, 1))
        self.assertEqual(0, calc.subtract(-1, -1))

    def test_multiply(self):
        self.assertEqual(50, calc.multiply(10, 5))
        self.assertEqual(-1, calc.multiply(-1, 1))
        self.assertEqual(1, calc.multiply(-1, -1))

    def test_divide(self):
        self.assertEqual(2, calc.divide(10, 5))
        self.assertEqual(-1, calc.divide(-1, 1))
        self.assertEqual(1, calc.divide(-1, -1))
        self.assertRaises(ValueError, calc.divide, 1, 0)
        #second option: use context manager 'with' as follows:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)



if __name__ == "__main__":
    unittest.main()
