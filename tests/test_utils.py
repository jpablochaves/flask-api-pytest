import pytest
from calculator.utils import calculator_operations as util

# test utils
def test_add(utils_model):
    a, b = utils_model
    assert util.add(a,b) == 15

def test_substract(utils_model):
    a, b = utils_model
    assert util.substract(a,b) == 5

def test_multipy(utils_model):
    a, b = utils_model
    assert util.multiply(a,b) == 50
    
def test_divide(utils_model):
    a, b = utils_model
    assert util.divide(a,b) == 2
    with pytest.raises(ZeroDivisionError):
        util.divide(2,0)