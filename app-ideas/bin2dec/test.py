import pytest

from main import bin2decimal, validate

success_tests = [
    ("0", 0),
    ("1", 1),
    ("10", 2),
    ("11", 3),
    ("100", 4),
    ("101", 5),
    ("110", 6),
    ("111", 7),
    ("1000", 8),
    ("1001", 9),
    ("1010", 10),
    ("1011", 11),
    ("1100", 12),
    ("1101", 13),
    ("1110", 14),
    ("1111", 15),
    ("00000000", 0),
    ("00000001", 1),
]

fail_tests = [
    ("a", -1),
    ("0000c", -1),
    ("-000c", -1),
    ("0100a0", -1),
    ("100-000", -1),
    ("10000.", -1),
]


def test_success_bin2decimal():
    for (binary, want) in success_tests:
        got = bin2decimal(binary)
        assert want == got


def test_fail_bin2decimal():
    for (binary, _) in fail_tests:
        with pytest.raises(ValueError):
            validate(binary)
