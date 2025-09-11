import re

def test_include_string():
    assert "hello" in "hello world."

def test_regex_match():
    assert re.match(r'^hello\d+$', "hello world.")

def test_check_length():
    assert len("hello world.") == 12
    assert len("") == 0

def test_string_case():
    text = "hello world"
    assert text.lower() == "hello world"
    assert text.upper() == "HELLO WORLD"