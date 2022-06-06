import pytest


if __name__ == '__main__':
    # 执行所有用例,
    # 当遇到第一个失败用例时对它进行忽略,
    # 当遇到第二个失败用例时立即停止pytest程序.
    # 记录当前失败位置是第二个失败用例的位置.
    pytest.main(["--stepwise-skip"])

    # 再次执行, 从第二个失败用例位置开始执行.
    # 当再次出现第一个失败用例失败时, 忽略.
    # 当再次出现第二个失败用例失败时, 立即停止pytest程序.
    # 即: 永远忽略第一个失败用例.
    pytest.main(["--stepwise-skip"])


