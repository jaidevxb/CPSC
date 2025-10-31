# test_diamond.py
from diamond import diamond
import pytest

def test_diamond_A():
    assert diamond("A") == "A"

def test_diamond_B():
    expected = " A\nB B\n A"
    assert diamond("B") == expected

def test_diamond_C():
    expected = "  A\n B B\nC   C\n B B\n  A"
    assert diamond("C") == expected

def test_diamond_lowercase_input():
    # lowercase should be accepted (converted to uppercase)
    expected = "  A\n B B\nC   C\n B B\n  A"
    assert diamond("c") == expected

def test_invalid_input_empty():
    with pytest.raises(ValueError):
        diamond("")

def test_invalid_input_multi():
    with pytest.raises(ValueError):
        diamond("AB")

def test_invalid_input_nonalpha():
    with pytest.raises(ValueError):
        diamond("1")
