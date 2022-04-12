### Pytest对外暴露的Hooks清单  

|Hook|功能描述|测试用例|
|---|---|---|
|pytest_load_initial_conftests|先执行`当前hook实现`再加载`conftest.py` <br/> 因此在`conftest.py`里面定义`当前hook`是无效的 <br/> 只能在自定义插件(即: pip install 的插件)中定义才会被执行.<br/> **注:** `pytest_cmdline_preparse`不建议再使用, 而是用`当前Hook`.|[自定义插件代码](./hooks/pytest-loadinitialconftests) <br/> [测试用例](./hooks/pytest-loadinitialconftests/testing)|
|pytest_cmdline_parse|加载`pytest.ini`和`conftest`之后执行`当前hook`, <br/>总之就是在解析命令行参数`hook`之前执行 `当前hook`.<br/>注: 满足两个硬件条件才会被出发. <br>必须由pytest.main来驱动, 以及pytest.main必须指定plugins.|[测试用例](./hooks/pytest-cmdlineparse)|