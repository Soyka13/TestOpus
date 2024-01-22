import unittest


class GreenTestCase(unittest.TestCase):
    @staticmethod
    def test_sum_list():
        assert sum([1, 1, 1]) == 3

    @staticmethod
    def test_sum_tuple():
        assert sum((1, 1, 1)) == 3
