import pytest


"""
当出现失败用例时, 不再执行后续用例, 退出pytest.
"""


if __name__ == '__main__':
    # 期望输出是
    # test_file.py::test_a PASSED                                              [ 33%]
    # test_file.py::test_b FAILED                                              [ 66%]
    # test_file.py::test_c PASSED                                              [100%]
    # pytest.main()

    # 期望输出是
    # test_file.py::test_a PASSED                                              [ 33%]
    # test_file.py::test_b FAILED                                              [ 66%]
    pytest.main(["-x"])
