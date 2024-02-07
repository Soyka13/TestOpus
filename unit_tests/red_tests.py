from testopus.utils.skip_decorator import skip
from testopus.utils.failure_expected_decorator import failure_expected


class RedTestCase:
    @staticmethod
    def test_boolean():
        x = True
        y = False
        assert x == y, "True is not False"

    @staticmethod
    def test_sum():
        assert 2+2 == 5, "2+2 should be 4"

    @staticmethod
    @skip
    def test_skipped():
        raise Exception("This test should be skipped.")

    @staticmethod
    @failure_expected
    def test_expected_failure():
        raise Exception("This test is expected to fail.")

    @staticmethod
    @failure_expected
    def test_expected_failure_without_exception():
        print("Exception was not raised.")
