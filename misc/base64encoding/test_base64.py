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

    @pytest.mark.parametrize(
        "string,want",
        [
            ["a", ["011000", "010000"]],
            ["ab", ["011000", "010110", "001000"]],
            ["abc", ["011000", "010110", "001001", "100011"]],
            [
                "abcdefg",
                [
                    "011000",
                    "010110",
                    "001001",
                    "100011",
                    "011001",
                    "000110",
                    "010101",
                    "100110",
                    "011001",
                    "110000",
                ],
            ],
        ],
    )
    def test_convert_bit_series(self, string: str, want: list):
        got = Base64.convert_bit_series(string)

        assert got == want

    @pytest.mark.parametrize(
        "string,want",
        [
            ("a", "YQ=="),
            ("ab", "YWI="),
            ("abc", "YWJj"),
            ("hoge", "aG9nZQ=="),
            ("hogehigehage", "aG9nZWhpZ2VoYWdl"),
            ("hogehagehige", "aG9nZWhhZ2VoaWdl"),
            ("EncodeToBase64Formatting", "RW5jb2RlVG9CYXNlNjRGb3JtYXR0aW5n"),
        ],
    )
    def test_base64encode(self, string: str, want: str):
        got = Base64.base64encoding(string)
        assert got == want

    @pytest.mark.parametrize(
        "string,want",
        [
            ("YQ==", "a"),
            ("YWI=", "ab"),
            ("YWJj", "abc"),
            ("aG9nZQ==", "hoge"),
            ("aG9nZWhpZ2VoYWdl", "hogehigehage"),
            ("aG9nZWhhZ2VoaWdl", "hogehagehige"),
            ("RW5jb2RlVG9CYXNlNjRGb3JtYXR0aW5n", "EncodeToBase64Formatting"),
        ],
    )
    def test_base64decode(self, string: str, want: str):
        got = Base64.base64decoding(string)
        assert got == want
