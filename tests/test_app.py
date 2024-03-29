import json
import pytest

# Test status of API


def test_hello(client):
    response = client.get('/calculator/operations/')
    assert response.status_code == 200

# test resources
##
# add uses GET


def test_add(client):
    resp = client.post('/calculator/operations/add?a=10&b=6',
                       data=json.dumps({"a": 10, "b": 6}),
                       content_type='application/json')
    assert resp.status_code == 200
    assert b'{"result":16}' in resp.data


def test_add_error():
    from calculator.calculator import flask_app as app
    test_data = {"a":2, "b": 0}
    with app.test_request_context(
        "calculator/operations/add", method='POST', data=test_data
    ) as ctx:
        # call a function that accesses request
        from calculator.utils.validations import validate_add_operation
        valid = validate_add_operation(test_data)

        assert not valid


def test_substract(client):
    resp = client.post('/calculator/operations/substract',
                       data=json.dumps({'a': 6, 'b': 4}),
                       content_type='application/json')
    assert resp.status_code == 200
    assert json.loads('{"result":2}') == json.loads(resp.get_data())


def test_multiply(client):
    resp = client.post('/calculator/operations/multiply',
                       data=json.dumps({'a': 2, 'b': 2}),
                       content_type='application/json')
    assert resp.status_code == 200
    assert json.loads('{"result":4}') == json.loads(resp.get_data())


def test_divide(client):
    resp = client.post('/calculator/operations/divide',
                       data=json.dumps({'a': 10, 'b': 2}),
                       content_type='application/json')
    assert resp.status_code == 200
    assert json.loads('{"result":5}') == json.loads(resp.get_data())


def test_divide_bad_request(client):
    resp = client.post('/calculator/operations/divide',
                       data=json.dumps({'a': 10, 'b': 0}),
                       content_type='application/json')
    assert resp.status_code == 400
