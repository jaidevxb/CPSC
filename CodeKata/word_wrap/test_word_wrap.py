from word_wrap import word_wrap
import pytest

def test_simple_case():
    text = "The quick brown fox"
    expected = "The quick\nbrown fox"
    assert word_wrap(text, 10) == expected

def test_exact_fit():
    assert word_wrap("Python", 6) == "Python"

def test_single_word_longer_than_column():
    # Word longer than column width should stay on its own line
    text = "supercalifragilisticexpialidocious"
    assert word_wrap(text, 10) == text

def test_short_column():
    text = "Hello world"
    expected = "Hello\nworld"
    assert word_wrap(text, 5) == expected

def test_multiple_spaces():
    text = "This  is   spaced"
    expected = "This  is\nspaced"
    assert word_wrap(text, 7) == expected

def test_empty_string():
    assert word_wrap("", 10) == ""

def test_long_text():
    text = "I am learning the word wrap kata with Jaidev from EEE"
    expected = "I am\nlearning\nthe word\nwrap kata\nwith Jaidev\nfrom EEE"
    assert word_wrap(text, 10) == expected

def test_column_large_enough():
    text = "Short text"
    assert word_wrap(text, 50) == text

def test_trailing_spaces():
    text = "  hello world  "
    expected = "hello\nworld"
    assert word_wrap(text.strip(), 6) == expected
