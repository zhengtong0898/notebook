import pytest

if __name__ == '__main__':
    # run pytest
    pytest.main(["-s"])

    # cache-show: 查看缓存
    pytest.main(["--cache-show"])
