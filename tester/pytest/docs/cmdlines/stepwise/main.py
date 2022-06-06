import pytest


if __name__ == '__main__':
    # 执行所有用例, 遇到失败用例时立即停止pytest程序.
    pytest.main(["--stepwise"])

    # 仅执行失败用例和后面未执行的用例.
    pytest.main(["--stepwise"])
