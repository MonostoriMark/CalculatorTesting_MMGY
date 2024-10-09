import pytest
from calculator import sum, sub, mult, div

def test_sum():
    assert sum(1, 2) == 3
    assert sum(-1, 2) == 1
    assert sum(-1, -2) == -3
    assert sum(0, 0) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(-1, 2) == -3
    assert sub(-1, -2) == 1
    assert sub(0, 0) == 0
    
def test_mult():
    assert mult(5, 2) == 10
    assert mult(-1, 2) == -2
    assert mult(-1, -2) == 2
    assert mult(0, 0) == 0

def test_div():
    assert div(10, 2) == 5
    assert div(-2, 1) == -2
    assert div(-6, -2) == 3
    assert div(0, 0) == 0