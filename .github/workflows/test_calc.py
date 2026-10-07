import pytest
from calc import add, mul, sub, div

def test_add():
    assert add() == 30

def test_mul():
    assert mul(20, 10) == 10

def test_sub():
    assert sub(10, 20) == 200

def test_div():
    assert div(20, 2) == 10