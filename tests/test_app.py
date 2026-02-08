"""Tests for app.py - you'll add more!"""

from app import add, is_even, multiply,reverse_string


class TestMath:
    """Tests for math functions."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2

class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(4,3) == 12

    def test_multiply_negative(self):
        assert multiply(-1, 1) == -1

    def test_multiply_by_zero(self):
        assert multiply(2,0) == 0
    
    def broken_test(self):
        assert multiply(9,9) == 18

class TestStrings:
    """Tests for string functions."""

    def test_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(3) is False
