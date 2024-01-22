import unittest


class GreenTestCase(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum([1, 1, 1]), 3)

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 1, 1)), 3)
