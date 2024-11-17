import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def rem_div(d, dr):
    if dr == 0:
        raise ValueError('На ноль делить нельзя')
    return d % dr


