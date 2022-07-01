import pytest


if __name__ == '__main__':
    # 运行一个模块(文件)中的所有测试用力.
    pytest.main(["dir_1", "dir_2", "-s"])               # 等同于: pytest dir_1
