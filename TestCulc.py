import unittest
import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc.Calc()

    def test_plus(self):
        value1 = 2
        value2 = 5
        expected = 7
        actual = self.calc.plus(value1, value2)
        self.assertEqual(expected, actual)

    def test_minus(self):
        value1 = 8
        value2 = 3
        expected = 5
        actual = self.calc.minus(value1, value2)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
