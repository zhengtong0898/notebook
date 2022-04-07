### Fixture内置对象  

|Fixture|功能描述|测试用例|
|---|---|---|
|config.cache|可以跨 测试用例、跨运行会话(Session) 存储和访问自定义的缓存数据.<br/>缓存数据会被持久化存储在`.pytest_cache`目录中, 因此可以跨用例访问.|[test_config_cache.py](./fixtures/test_fixture_config_cache.py)|  
|capsys|`capsys.readouterr()`会将常规的标准输出、标准错误(`print`)进行拦截|[test_fixture_capsys.py](./fixtures/test_fixture_capsys.py)|
