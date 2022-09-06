def add(a, b) -> float:
    return a + b

def substract(a, b) -> float:
    return a - b

def multiply(a, b) -> float:
    return a * b

def divide(a, b) -> float:
    try:
        div = a / b
    except ZeroDivisionError:
         raise ZeroDivisionError('Zero Division error!')
    return div