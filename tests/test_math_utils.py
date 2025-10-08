from src.math_utils import is_prime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src"))

def test_small_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(3) is True

def test_small_composite_number():
    assert is_prime(4) is False
    assert is_prime(9) is False

def test_boundary_cases():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-1) is False

def test_larger_prime_numbers():
    assert is_prime(3) is True
    assert is_prime(5) is True