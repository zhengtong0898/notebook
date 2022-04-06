### Fixture调用顺序?  

|场景|调用顺序|测试用例|
|---|---|---|
|测试函数参数场景|按参数声明的顺序来调用|[test_fixture_order_with_param.py](./fixtures/test_fixture_order_with_param.py)|    
|测试函数使用装饰器场景|按自下而上的顺序来调用|[test_fixture_order_with_decorator.py](./fixtures/test_fixture_order_with_decorator.py)|
|测试函数混合使用装饰器和参数场景|先自下而上, 再到按参数声明的顺序来调用|[test_fixture_order_with_mixin.py](./fixtures/test_fixture_order_with_mixin.py)|
|Fixture Scope (作用域)|`session` 整个程序从开始到结束仅执行一次.<br/>`package` __init__文件夹内的程序仅执行一次.<br/>`module` 单个文件内的程序仅执行一次.<br/>`class` 单个类仅执行一次.<br/>`function` 单个函数或方法仅执行一次(**默认**).<br/>按自上而下的顺序来调用.|[test_fixture_scope_order_default.py](./fixtures/scope_default/test_fixture_scope_order_default.py)|
