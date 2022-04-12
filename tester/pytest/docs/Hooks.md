### Pytest对外暴露的Hooks清单  

|Hook|功能描述|测试用例|
|---|---|---|
|pytest_load_initial_conftests|先执行`当前hook实现`再加载`conftest.py` <br/> 因此在`conftest.py`里面定义`当前hook`是无效的 <br/> 只能在自定义插件(即: pip install 的插件)中定义才会被执行.<br/> **注:** `pytest_cmdline_preparse`不建议再使用, 而是用`当前Hook`.|[自定义插件代码](./hooks/pytest-loadinitialconftests) <br/> [测试用例](./hooks/pytest-loadinitialconftests/testing)|