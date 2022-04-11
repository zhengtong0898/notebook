

# 由三种方式可以驱动插件:
# 1. 在 conftest.py 中定义 pytest_plugins = "loadinitialconftests".
# 2. 在命令行中执行 pytest -p loadinitialconftests.
# 3. 在 pytest.ini 中定义 addopts = -p loadinitialconftests.
pytest_plugins = "loadinitialconftests"
