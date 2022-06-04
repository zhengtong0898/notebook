import pytest

"""
测试场景准备:

    测试用例文件          最后修改时间
    test_file_a.py      2022-06-04 19:14:24
    test_file_z.py      2022-06-04 19:15:12
    
"""


if __name__ == '__main__':
    # 测试用例文件          最后修改时间
    # test_file_a.py      2022-06-04 19:14:24
    # test_file_z.py      2022-06-04 19:15:12

    # 期望执行顺序是:
    # test_file_a.py::test_b PASSED                                            [ 50%]
    # test_file_z.py::test_a PASSED                                            [100%]
    pytest.main()

    # 执行顺序是:
    # test_file_z.py::test_a PASSED                                            [ 50%]
    # test_file_a.py::test_b PASSED                                            [100%]
    # pytest.main(["--new-first"])
