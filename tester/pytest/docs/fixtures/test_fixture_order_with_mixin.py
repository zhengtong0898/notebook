import pytest


@pytest.fixture
def fixture_a():
    print("fixture_a")
    return "a"


@pytest.fixture
def fixture_b():
    print("fixture_b")
    return "b"


@pytest.fixture
def fixture_c():
    print("fixture_c")
    return "c"


@pytest.mark.usefixtures("fixture_a")
@pytest.mark.usefixtures("fixture_b")
def test_fixture_order_mixin(fixture_c):
    """
    执行顺序: 先自下而上, 然后再到参数.
    1. fixture_b
    2. fixture_a
    3. fixture_c
    """
