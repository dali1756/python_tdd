import pytest
from src.calculator import add, subtract, multiply, divide, modulo, power

def test_add():
    result = add(1, 2)
    assert result == 3

def test_subtract():
    result = subtract(1, 1)
    assert result == 0

def test_multiplie():
    result = multiply(2, 2)
    assert result == 4

def test_divide():
    result = divide(10, 2)
    assert result == 5

def test_modulo():
    result = modulo(3, 2)
    assert result == 1

def power():
    result = power(2, 3)
    assert result == 8