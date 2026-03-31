import pytest
from simplecalc import Calculator


def test_add():
    
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(2.5, 3.5) == 6.0


def test_subtract():
   
    assert Calculator.subtract(10, 5) == 5
    assert Calculator.subtract(0, 5) == -5


def test_multiply():
    
    assert Calculator.multiply(4, 3) == 12
    assert Calculator.multiply(2.5, 2) == 5.0


def test_divide():
    
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(7, 2) == 3.5
    
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(5, 0)


def test_power():
    
    assert Calculator.power(2, 3) == 8
    assert Calculator.power(4, 0.5) == 2.0