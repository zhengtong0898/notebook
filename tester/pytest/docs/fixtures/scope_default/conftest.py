import pytest


"""
在定义这些fixture的时候, 特意按乱序方式排列,
期望执行结果按 session , package , module , class , function 的顺序来执行.
"""


@pytest.fixture(scope="function", autouse=True)
def scope_function_function():
    print("scope_function_function")


@pytest.fixture(scope="module", autouse=True)
def scope_module_function():
    print("scope_module_function")


@pytest.fixture(scope="session", autouse=True)
def scope_session_function():
    print("scope_session_function")


@pytest.fixture(scope="package", autouse=True)
def scope_package_function():
    print("scope_package_function")


@pytest.fixture(scope="class", autouse=True)
def scope_class_function():
    print("scope_class_function")


