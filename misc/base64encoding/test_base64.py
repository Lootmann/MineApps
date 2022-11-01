import pytest

from mybase64 import Base64


class TestBase64EncodingUtils:
    @pytest.mark.parametrize(
        "bits,want",
        [
            ("000000", "A"),
            ("001011", "L"),
            ("011001", "Z"),
            ("011010", "a"),
            ("110011", "z"),
            ("111001", "5"),
            ("111110", "+"),
            ("111111", "-"),
        ],
    )
    def test_bit2char(self, bits: str, want: str):
        got = Base64.bit2char(bits)
        assert got == want

    @pytest.mark.parametrize(
        "char,want",
        [
            ("A", "000000"),
            ("L", "001011"),
            ("Z", "011001"),
            ("a", "011010"),
            ("z", "110011"),
            ("5", "111001"),
            ("6", "111010"),
            ("+", "111110"),
            ("-", "111111"),
        ],
    )
    def test_char2bit(self, char: str, want: str):
        got = Base64.char2bit(char)
        assert got == want
