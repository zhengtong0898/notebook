import pytest


@pytest.fixture
def fixture_a():
    print("fixture_a")
    return "a"


@pytest.fixture
def fixture_b():
    print("fixture_b")
    return "b"


def test_fixture_order_forward(fixture_a, fixture_b):
    """
    执行顺序:
    1. fixture_a
    2. fixture_b
    """
    assert (fixture_a, fixture_b) == ("a", "b")


def test_fixture_order_reverse(fixture_b, fixture_a):
    """
    执行顺序:
    1. fixture_b
    2. fixture_a
    """
    assert (fixture_a, fixture_b) == ("a", "b")
