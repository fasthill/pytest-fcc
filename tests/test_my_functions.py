import pytest

import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("i like ", "burgers")
    assert result == "i like burgers"

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)
