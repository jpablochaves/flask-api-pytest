import pytest


def test_requestmodel(request_model):
    model = request_model
    assert model.a == 4
    assert model.b == 2


def test_responsemodel(response_model): 
    expected_value:float = 10.0  
    assert response_model.result == expected_value
