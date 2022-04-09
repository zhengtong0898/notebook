import os


"""
monkeypatch 解决了什么问题?

1. 节省冗余的样板代码(数据备份、数据恢复、异常捕获).  
2. 每个用例的对象/数据篡改都是隔离的, 不会影响其他用例.  
3. 让测试代码更聚焦, 减少样板代码的干扰.  
"""


def test_env_reading_1(monkeypatch):
    monkeypatch.setitem(os.environ, 'ENV1', 'myval')
    val = os.environ.get("ENV1")
    assert val == "myval"


def test_env_reading_2(monkeypatch):
    val = os.environ.get("ENV1")                        # 这里拿不到 test_env_reading_1 中 ENV1 的变量.
    assert val == "myval"
