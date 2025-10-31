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

def test_diamond_Z():
    # Just checks structure, not full text — too large to hardcode
    result = diamond("Z")
    lines = result.split("\n")
    assert len(lines) == (26 * 2 - 1)  # Diamond height = 51
    assert lines[0].strip() == "A"     # Top
    assert lines[-1].strip() == "A"    # Bottom
    assert "Z" in lines[25]            # Middle line (widest point)

def test_diamond_whitespace_input():
    # Should not allow spaces
    import pytest
    with pytest.raises(ValueError):
        diamond(" ")


def test_diamond_special_char():
    import pytest
    with pytest.raises(ValueError):
        diamond("@")