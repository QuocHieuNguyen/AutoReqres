import requests
import pytest


def calc_addition(a, b):
    return a + b


def test_calc_addition():
    # Verify the output of `calc_addition` function
    output = calc_addition(2, 4)
    assert output == 6
