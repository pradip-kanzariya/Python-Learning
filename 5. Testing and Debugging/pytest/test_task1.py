import pytest
from task1 import reverse_string, capitalize_words, remove_punctuation, is_palindrome

# Parameterized
@pytest.mark.parametrize("input_var, output_var", [
    ("abc", "cba"),
    ("lmn", "nml")
])
def test_reverse_string_valid(input_var, output_var):
    assert reverse_string(input_var) == output_var

@pytest.mark.parametrize("wrong_input", [
    123,
    None,
    {"abc": "pqr"},
    ["abc", "pqr"],
    12.3,
    {"a", "b", "c"}
])
def test_reverse_string_invalid(wrong_input):
    with pytest.raises(TypeError):
        reverse_string(wrong_input)
    

# Not Parameterized
def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("321") == "123"
    with pytest.raises(TypeError):
        reverse_string(123)

def test_capitalize_words():
    assert capitalize_words("abc") == "Abc"
    assert capitalize_words(" hello   word") == "Hello Word"
    assert capitalize_words("HELLO") == "Hello"
    with pytest.raises(TypeError):
        capitalize_words(None)

def test_remove_punctuation():
    assert remove_punctuation("abc.abc") == "abcabc"
    assert remove_punctuation("abc . abc") == "abc  abc"

def test_is_palindrome():
    assert is_palindrome("aba") == True
    assert is_palindrome("abc") == False
    assert is_palindrome("a") == True
