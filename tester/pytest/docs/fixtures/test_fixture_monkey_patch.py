import os


"""
monkeypatch 解决了什么问题?

1. 节省冗余的样板代码(数据备份、数据恢复、异常捕获).  
2. 每个用例的对象/数据篡改都是隔离的, 不会影响其他用例.  
3. 让测试代码更聚焦, 减少样板代码的干扰.  

参考:  
https://holgerkrekel.net/2009/03/03/monkeypatching-in-unit-tests-done-right/
https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html#monkeypatching
"""


def test_env_reading_1(monkeypatch):
    monkeypatch.setitem(os.environ, 'ENV1', 'myval')
    val = os.environ.get("ENV1")
    assert val == "myval"


def test_env_reading_2(monkeypatch):
    val = os.environ.get("ENV1")                        # 这里拿不到 test_env_reading_1 中 ENV1 的变量, 符合预期
    assert val == "myval"                               # 因为 monekypatch 是以测试用例为单位来做隔离的.


"""
期望:
test_env_reading_1 成功
test_env_reading_2 失败

输出结果:

============================= test session starts ==============================
collecting ... collected 2 items

test_fixture_monkey_patch.py::test_env_reading_1 PASSED                  [ 50%]
test_fixture_monkey_patch.py::test_env_reading_2 FAILED                  [100%]
test_fixture_monkey_patch.py:22 (test_env_reading_2)
None != myval

Expected :myval
Actual   :None
<Click to see difference>

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f6cc9fd74c0>

    def test_env_reading_2(monkeypatch):
        val = os.environ.get("ENV1")                        # 这里拿不到 test_env_reading_1 中 ENV1 的变量, 符合预期
>       assert val == "myval"                               # 因为 monekypatch 是以测试用例为单位来做隔离的.
E       AssertionError: assert None == 'myval'

test_fixture_monkey_patch.py:25: AssertionError


========================= 1 failed, 1 passed in 0.10s ==========================
"""
