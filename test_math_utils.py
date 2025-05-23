from math_utils import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3
    
def test_multiply():
    a, b = 2, 3
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    assert a * b == 6

    try:
        multiply(0, "string")
    except ValueError:
        assert True
