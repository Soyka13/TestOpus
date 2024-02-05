import unittest


class RedTestCase(unittest.TestCase):
    def test_boolean(self):
        self.assertEqual(True, False)

    def test_sum(self):
        self.assertEqual(2 + 2, 5)

    @unittest.skip
    def test_skipped(self):
        raise Exception("This test should be skipped.")

    @unittest.expectedFailure
    def test_expected_failure(self):
        raise Exception("This test is expected to fail.")


if __name__ == '__main__':
    unittest.main()
