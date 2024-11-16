import pytest
from math_functions import *

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 7) == 0
    assert multiply(1.5, 2) == 3
    assert multiply(-2, -2) == 4

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-10, 5) == -2
    assert divide(7, 2) == 3.5
    with pytest.raises(ValueError):
        divide(10, 0)
    assert divide(0, 1) == 0

def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(1, 1, 1, 1) == 0
    assert distance(-1, -1, 1, 1) == math.sqrt(8)
    assert distance(0, 0, 0, 0) == 0
    assert distance(2, 3, 6, 7) == 5.656854249492381

def test_quadratic_roots():
    assert quadratic_roots(1, -3, 2) == (2.0, 1.0)
    assert quadratic_roots(1, 2, 1) == (-1.0,)
    assert quadratic_roots(1, 0, -4) == (2.0, -2.0)
    assert quadratic_roots(1, 1, 1) == None
    assert quadratic_roots(2, 5, 3) == (-1.0, -1.5)

def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7
    assert geometric_sum(1, 1, 5) == 5
    assert geometric_sum(2, 3, 2) == 8
    assert geometric_sum(3, 0.5, 4) == 5.625
    assert geometric_sum(0, 5, 10) == 0
#ЧЕРЕМУШКИН АНТОН
