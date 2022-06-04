import pytest


if __name__ == '__main__':
    # 运行所有用例
    pytest.main(["-s"])

    # 当没有失败用例的时候, 运行所有用例.
    pytest.main(["--last-failed", "--last-failed-no-failures", "all"])

    # 当没有失败用例的时候, 不运行用例.
    pytest.main(["--last-failed", "--last-failed-no-failures", "none"])
