import unittest

from main import convert_dollar_to_cent


def create_want_result(quarter: int, dim: int, nickel: int, penny: int):
    return {"quarter": quarter, "dim": dim, "nickel": nickel, "penny": penny}


class TestConvertDollarToCent(unittest.TestCase):
    def test_100(self):
        dollar = 1.00
        got = convert_dollar_to_cent(dollar)
        want = create_want_result(4, 0, 0, 0)

        self.assertEqual(got, want)

    def test_099(self):
        dollar = 0.99
        got = convert_dollar_to_cent(dollar)
        want = create_want_result(3, 2, 0, 4)

        self.assertEqual(got, want)

    def test_058(self):
        dollar = 0.58
        got = convert_dollar_to_cent(dollar)
        want = create_want_result(2, 0, 1, 3)

        self.assertEqual(got, want)

    def test_009(self):
        dollar = 0.09
        got = convert_dollar_to_cent(dollar)
        want = create_want_result(0, 0, 1, 4)

        self.assertEqual(got, want)

    def test_1(self):

        dollar = 0.01
        got = convert_dollar_to_cent(dollar)
        want = create_want_result(0, 0, 0, 1)

        self.assertEqual(got, want)
