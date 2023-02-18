"""
The tests/conftest.py file contains setup functions called fixtures that each test will use. Tests are in Python modules that start with test_, and each test function in those modules also starts with test_.    
"""
import pytest
#from calculator.models.models import (RequestOperation, ResponseOperation)
from typing import Type
from calculator import flask_app as app


@pytest.fixture
def client():
    return app.test_client()


#@pytest.fixture
#def request_model() -> Type[RequestOperation]:
#    query = RequestOperation(a=4,b=2)
#    return query

#@pytest.fixture
#def response_model() -> ResponseOperation:
#    return ResponseOperation(result=10.0)


@pytest.fixture
def utils_model():
    return 10, 5
