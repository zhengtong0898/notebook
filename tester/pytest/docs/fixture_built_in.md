### Fixture内置对象  

|Fixture|功能描述|测试用例|
|---|---|---|
|config.cache|可以跨 测试用例、跨运行会话(Session) 存储和访问自定义的缓存数据.<br/>缓存数据会被持久化存储在`.pytest_cache`目录中, 因此可以跨用例访问.|[test_config_cache.py](./fixtures/test_fixture_config_cache.py)|  
|capsys|`capsys.readouterr()`会将常规的标准输出、标准错误(`print`)进行拦截|[test_fixture_capsys.py](./fixtures/test_fixture_capsys.py)|
|request|**request.config.inicfg:** 存储`pytest.ini`键值信息.<br/> **request.config.invocation_params:** 存储命令行参数信息.<br/> **request.config.option:** 存储全量的配置信息,这些信息可以配置在`pytest.ini`.<br/> **request.config.rootpath:** 存储项目根路径.<br/> **request.config.cache:** 存储的是`config.cache`对象.<br/> **request.config.pluginmanager:** 存储`pytest`的全局`pluginmanager`对象.<br/> **request.config._inicache:** 存储关键的运行配置. |[pytest.ini](./fixtures/request_config/pytest.ini)<br/> [test_fixture_request.py](./fixtures/request_config/test_fixture_request.py)|
|caplog|拦截`logging日志`并写入到`caplog`对象 |[test_fixture_caplog.py](./fixtures/test_fixture_caplog.py)|
|[monkeypatch](https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/)|通过`运行时`动态的修改对象(属性、方法)或数据(字段、值)来完成不同场景的测试目标 |[test_fixture_monkey_patch.py](./fixtures/test_fixture_monkey_patch.py)|
|pytester|**适用于自研插件的测试场景:** <br/>在pytester之前, 测试插件的话需要用目录来隔离独立的testcase. <br/>在pytester之后, 可以将testcase写在一个测试函数中, 可以做到统一执行.  |[官网教程](https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html#testing-plugins) <br/>[test_assertion.py](https://github.com/pytest-dev/pytest/blob/7.1.1/testing/test_assertion.py#L33)|  
|tmp_path|为测试用例创建一个独立的(隔离的)临时文件夹.<br/> 测试用例产生的临时文件都可以放在这里.|[test_fixture_tmp_path.py](./fixtures/test_fixture_tmp_path.py)|
