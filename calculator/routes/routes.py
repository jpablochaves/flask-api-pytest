from flask import jsonify
from calculator import flask_app as app
from calculator.models.models import (
	RequestOperation,
	ResponseOperation,
)
import calculator.utils.calculator_operations as oper
from flask_pydantic import validate


__URL='/calculator/operations'

@app.route(f'{__URL}/')
def index():
    return 'Web Service is Alive!'

@app.route(f"{__URL}/add", methods=["GET"])
@validate()
def add_operation(query: RequestOperation):
    res = oper.add(query.a, query.b)
    return ResponseOperation(result=res)

@app.post(f"{__URL}/substract")
@validate()
def substract_operation(body: RequestOperation):
    res = oper.substract(body.a, body.b)
    return ResponseOperation(result=res)

@app.post(f'{__URL}/multiply')
@validate()
def multiply_operation(body: RequestOperation):
    res = oper.multiply(body.a, body.b)
    return ResponseOperation(result=res)

@app.post(f'{__URL}/divide')
@validate()
def divide_operation(body: RequestOperation): 
    print(body, type(body))   
    try:
        res = oper.divide(body.a, body.b)
    except ZeroDivisionError:
        return jsonify({"error":"Invalid division!"}), 400
    return ResponseOperation(result=res)
