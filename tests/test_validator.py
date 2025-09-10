import pytest
from src.validator import is_valid_email, is_password, is_valid_age

def test_accept_valid_email():
    assert is_valid_email("example@example.com")
    assert is_valid_email("test@test.com.tw")

def reject_invalid_email():
    assert not is_valid_email("invalid")
    assert not is_valid_email("@example.com")
    assert not is_valid_email("example@")

def test_accept_password():
    assert is_password("example123")
    assert is_password("!Aa123")

def test_reject_invalid_password():
    assert not is_password("abc")
    assert not is_password("ABC")
    assert not is_password("!Abc")

def test_accept_valid_range():
    assert is_valid_age(10)
    assert is_valid_age(99)

def test_reject_invalid_age():
    assert not is_valid_age(1)
    assert not is_valid_age(-1)