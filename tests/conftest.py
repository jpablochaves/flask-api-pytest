"""
The tests/conftest.py file contains setup functions called fixtures that each test will use. Tests are in Python modules that start with test_, and each test function in those modules also starts with test_.    
"""
import pytest
import os
import sys

# Get the directory where this file is located
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# add the parent directory to the sys.path
sys.path.append(parent)

from calculator.calculator import flask_app as app

@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def utils_model():
    return 10, 5
