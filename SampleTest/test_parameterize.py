import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected, "the test is failed"


@pytest.mark.addition
def test_addition():
    assert 6 + 5 == 12, "test failed"
