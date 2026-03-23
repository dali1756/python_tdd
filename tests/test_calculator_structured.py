import pytest

from src.calculator import add, divide

class TestCalculatorAddition:
    def test_add_positive_numbers(self):
        assert add(1, 2) == 3

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2

class TestCalculatorBoundary:
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
