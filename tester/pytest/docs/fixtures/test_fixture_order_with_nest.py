import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def a(order):
    order.append("a")


@pytest.fixture
def b(a, order):
    order.append("b")


@pytest.fixture
def c(a, b, order):
    order.append("c")


@pytest.fixture
def d(c, b, order):
    order.append("d")


@pytest.fixture
def e(d, b, order):
    order.append("e")


@pytest.fixture
def f(e, order):
    order.append("f")


@pytest.fixture
def g(f, c, order):
    order.append("g")


def test_order(g, order):
    """
    按照依赖顺序来执行.

    当前测试用例虽然指定了先执行 fixture g, 然后再执行 fixture order,
    但是由于 fixture g 也指定了要执行 fixture order,
    因此pytest会先执行 fixture order 然后在执行 fixture g.

    参考:
    https://docs.pytest.org/en/6.2.x/fixture.html#fixtures-of-the-same-order-execute-based-on-dependencies
    """
    assert order == ["a", "b", "c", "d", "e", "f", "g"]
