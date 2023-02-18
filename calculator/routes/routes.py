from flask import jsonify, request
from calculator.calculator import flask_app as app
import calculator.utils.calculator_operations as oper


__URL = '/calculator/operations'


@app.route(f'{__URL}/')
def index():
    return 'Web Service is Alive!'


@app.route(f"{__URL}/add", methods=["POST"])
def add_operation():
    content = request.json
    res = oper.add(content["a"], content["b"])
    return jsonify({"result": res}), 200


@app.route(f"{__URL}/substract", methods=["POST"])
def substract_operation():
    content = request.json
    a = content["a"]
    b = content["b"]
    res = oper.substract(a, b)
    return jsonify({"result": res}), 200


@app.route(f'{__URL}/multiply', methods=["POST"])
def multiply_operation():
    content = request.json
    a = content["a"]
    b = content["b"]
    res = oper.multiply(a, b)
    return jsonify({"result": res}), 200


@app.route(f'{__URL}/divide', methods=["POST"])
def divide_operation():
    try:
        content = request.json
        a = content["a"]
        b = content["b"]
        res = oper.divide(a, b)
    except ZeroDivisionError:
        return jsonify({"error": "Invalid division!"}), 400
    return jsonify({"result": res}), 200
