import unittest


class RedTestCase(unittest.TestCase):
    def test_boolean(self):
        self.assertEqual(True, False)

    def test_sum(self):
        self.assertEqual(2 + 2, 5)


if __name__ == '__main__':
    unittest.main()
