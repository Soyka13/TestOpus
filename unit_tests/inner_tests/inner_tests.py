
def test_non_class():
    assert sum([2, 2, 2]) == 6, "2+2+2 equals 6"


class InnerTestCase:
    @staticmethod
    def test_sum():
        assert sum([5, 5, 5]) == 15, "5+5+5 equals 15"
