class GreenTestCase:
    @staticmethod
    def test_sum_list():
        assert sum([1, 1, 1]) == 3, "1+1+1 equals 3"

    @staticmethod
    def test_sum_tuple():
        assert sum((1, 1, 1)) == 3, "1+1+1 equals 3"

    @staticmethod
    def different_naming_for_test():
        assert sum((1, 2, 3)) == 6, "1+2+3 equals 6"
