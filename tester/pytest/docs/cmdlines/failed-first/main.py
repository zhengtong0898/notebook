import pytest


"""
测试场景
test_cases.py 文件中准备一个成功用例，两个失败用例

期望效果
pytest --failed-first
先跑失败用例, 再跑剩下的其他用例.
"""


if __name__ == '__main__':
    # 执行全量用例.
    pytest.main(["-s"])
    """
    输出:
    ============================= test session starts ==============================
    platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-0.13.1
    rootdir: notebook/tester/pytest/docs/cmdlines/failed-first
    plugins: xdist-2.5.0, allure-pytest-2.9.45, loadinitialconftests-0.0.0, cmdlineparse-0.0.0, forked-1.4.0
    collected 3 items
    
    test_cases.py::test_a PASSED
    test_cases.py::test_b FAILED
    test_cases.py::test_c FAILED
    
    =================================== FAILURES ===================================
    ____________________________________ test_b ____________________________________
    
        def test_b():
    >       "b" + 1
    E       TypeError: can only concatenate str (not "int") to str
    
    test_cases.py:8: TypeError
    ____________________________________ test_c ____________________________________
    
        def test_c():
    >       "c" + 1
    E       TypeError: can only concatenate str (not "int") to str
    
    test_cases.py:12: TypeError
    =========================== short test summary info ============================
    FAILED test_cases.py::test_b - TypeError: can only concatenate str (not "int"...
    FAILED test_cases.py::test_c - TypeError: can only concatenate str (not "int"...
    ========================= 2 failed, 1 passed in 0.09s ==========================
    """

    # 重跑失败用例
    pytest.main(["--failed-first"])
    """
    注意: 先跑失败用例, 再跑剩下的其他用例.
    输出: 
    ============================= test session starts ==============================
    platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-0.13.1
    rootdir: notebook/tester/pytest/docs/cmdlines/failed-first
    plugins: xdist-2.5.0, allure-pytest-2.9.45, loadinitialconftests-0.0.0, cmdlineparse-0.0.0, forked-1.4.0
    collected 3 items
    run-last-failure: rerun previous 2 failures first
    
    test_cases.py::test_b FAILED                                             [ 33%]
    test_cases.py::test_c FAILED                                             [ 66%]
    test_cases.py::test_a PASSED                                             [100%]
    
    =================================== FAILURES ===================================
    ____________________________________ test_b ____________________________________
    
        def test_b():
    >       "b" + 1
    E       TypeError: can only concatenate str (not "int") to str
    
    test_cases.py:8: TypeError
    ____________________________________ test_c ____________________________________
    
        def test_c():
    >       "c" + 1
    E       TypeError: can only concatenate str (not "int") to str
    
    test_cases.py:12: TypeError
    =========================== short test summary info ============================
    FAILED test_cases.py::test_b - TypeError: can only concatenate str (not "int"...
    FAILED test_cases.py::test_c - TypeError: can only concatenate str (not "int"...
    ========================= 2 failed, 1 passed in 0.03s ==========================
    """