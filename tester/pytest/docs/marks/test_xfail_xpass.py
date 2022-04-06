import pytest


def test_correct():
    assert 1 == 1


def test_error():
    assert 2 == 1


@pytest.mark.xfail
def test_xfail_example():
    """
    xfail 跟常规的测试用例一样会被执行, 错误堆栈信息会被打印出来.
    xfail 的测试用例, 失败了会被归纳到 xfailed 集合中.
    xfail 意味着失败用例是已知Bug导致, 符合预期.
    """
    assert 2 == 1


@pytest.mark.xfail
def test_xpass_example():
    """
    xfail 的测试用例, 成功了会被归纳到 xpassed 集合中.
    xpassed 意味着Bug已经被修复了, 应该将当前标记去掉.
    """
    assert 1 == 1


"""
============================= test session starts ==============================
collecting ... collected 4 items

test_xfail_xpass.py::test_error FAILED                                   [ 25%]
test_xfail_xpass.py:3 (test_error)
2 != 1

Expected :1
Actual   :2
<Click to see difference>

def test_error():
>       assert 2 == 1
E       assert 2 == 1

test_xfail_xpass.py:5: AssertionError

test_xfail_xpass.py::test_xfail_example XFAIL                            [ 50%]
@pytest.mark.xfail
    def test_xfail_example():
>       assert 2 == 1
E       assert 2 == 1

test_xfail_xpass.py:10: AssertionError

test_xfail_xpass.py::test_xpass_example XPASS                            [ 75%]
test_xfail_xpass.py::test_correct PASSED                                 [100%]

============== 1 failed, 1 passed, 1 xfailed, 1 xpassed in 0.12s ===============
"""
