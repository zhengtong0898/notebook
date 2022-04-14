### Pytest对外暴露的Hooks清单  

|Hook|功能描述|测试用例|
|---|---|---|
|pytest_load_initial_conftests|在加载`conftest.py`和`pytest.ini`之前先执行`当前函数`.<br/>所以在`conftest.py`文件中定义`当前hook`是无效的 <br/> 只能在自定义插件(即: pip install 的插件)中定义才会被执行.<br/>**注-1:**<br/>`pytest_cmdline_preparse`不建议再使用, 而是用`当前Hook`.<br/>**注-2:**<br/>TODO: 使用场景(低频)待补充.|[自定义插件代码](./hooks/pytest-loadinitialconftests) <br/> [测试用例](./hooks/pytest-loadinitialconftests/testing)|
|pytest_cmdline_parse|此时已加载好`conftest.py`和`pytest.ini`.<br/>在解析命令行参数之前先执行`当前hook`.<br/>**注-1:**<br/>满足两个条件才会被触发: <br>1. 必须由pytest.main来驱动<br/>2. pytest.main必须指定plugins.<br/>**注-2:**<br/>我们可以在这个阶段插入额外的命令行参数.|[测试用例](./hooks/pytest-cmdlineparse)|
|pytest_cmdline_main|此时已解析好命令行参数, 生成一个`pytest.Config`对象.<br/>在处理命令行参数之前先执行 `当前hook`.<br/>**注-1:** <br/>我们可以在这个阶段根据修改`config.option`的默认值.|[测试用例](./hooks/pytest-cmdlineparse)|