import pytest


@pytest.fixture
def fixture_a():
    print("fixture_a")
    return "a"


@pytest.fixture
def fixture_b():
    print("fixture_b")
    return "b"


@pytest.mark.usefixtures("fixture_a")
@pytest.mark.usefixtures("fixture_b")
def test_fixture_order_decorator_forward():
    """
    执行顺序: 自下而上
    1. fixture_b
    2. fixture_a
    """


@pytest.mark.usefixtures("fixture_b")
@pytest.mark.usefixtures("fixture_a")
def test_fixture_order_decorator_reverse():
    """
    执行顺序: 自下而上
    1. fixture_a
    2. fixture_b
    """
