import pytest


@pytest.mark.parametrize("num", [1, 2, 3])
def test_case_1(num):
    print("test case 1")


def test_case_2():
    print("test case 2")
