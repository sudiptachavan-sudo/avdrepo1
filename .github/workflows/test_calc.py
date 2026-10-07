import pytest
from calc import add, mul, sub, div

def test_add(a, b):
    assert add(10, 20) == 30

def test_mul(a, b):
    assert mul(20, 10) == 10

def test_sub(a, b):
    assert sub(10, 20) == 200

def test_div(a, b):
    assert div(20, 2) == 10