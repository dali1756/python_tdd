import math, pytest

def test_greater_than():
    assert 2 > 1

def test_greater_equal():
    assert 1 == 1

def test_greater_than_or_equal():
    assert 2 >= 1
    assert 2 >= 2

def test_less_than():
    assert 1 < 2

def test_less_than_or_equal():
    assert 1 <= 1
    assert 1 <= 2

def test_range_check():
    value = 10
    assert 1 <= value <= 10

def test_float():
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert math.pi == pytest.approx(3.14)