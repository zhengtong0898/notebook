### Fixture调用顺序?  

|场景|调用顺序|测试用例|
|---|---|---|
|测试函数参数场景|按参数声明的顺序来调用|[test_fixture_order_with_param.py](./fixtures/test_fixture_order_with_param.py)|    
|测试函数使用装饰器场景|按自下而上的顺序来调用|[test_fixture_order_with_decorator.py](./fixtures/test_fixture_order_with_decorator.py)|
|测试函数混合使用装饰器和参数场景|先自下而上, 再到按参数声明的顺序来调用|[test_fixture_order_with_mixin.py](./fixtures/test_fixture_order_with_mixin.py)|
