import pytest


@pytest.fixture(autouse=True)
def before_test():
    print("...Soon to be tested")


@pytest.fixture
def input():
    return 6


def test_subtraction(input):
    assert input - 6 == 12, "test failed"
