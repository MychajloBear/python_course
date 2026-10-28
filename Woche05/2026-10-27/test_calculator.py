import pytest
import calculator
import pandas as pd

def test_add_positive_numbers():
    assert calculator.add(2, 5) == 7
    assert calculator.add(1, 1) == 2

def test_add_typerrror():
    with pytest.raises(TypeError):
        calculator.add('a', 2)