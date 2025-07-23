import unittest
from .maxProfit import Solution

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_profit(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution.maxProfit([]), 0)

    def test_negative_prices(self):
        with self.assertRaises(ValueError):
            self.solution.maxProfit([1, -5, 3])

if __name__ == '__main__':
    unittest.main()
