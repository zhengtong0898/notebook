import pytest


if __name__ == '__main__':
    # 需要安装 coverage 和 pytest-cov
    pytest.main(["--cov=src", "--cov-report", "html", "-s"])
