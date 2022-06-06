import pytest


if __name__ == '__main__':
    # 执行所有用例, 会有两个失败用例.
    pytest.main()

    # 再次执行所有失败用例, 当出现失败用例时停止程序.
    # 当用例执行成功后, 该用例从last-failed集合中移除.
    # 当用例执行失败后, 失败的和未执行的失败用例继续保留.
    # pytest --last-failed -x

