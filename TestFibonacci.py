import unittest
import Fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci.Fibonacci()

    def test_plus(self):
        cases = [[0, 0], [1, 1], [2, 1], [3, 2]]
        for case in cases:
            self.assertEqual(case[1], self.fibonacci.fib(case[0]))


if __name__ == "__main__":
    unittest.main()
