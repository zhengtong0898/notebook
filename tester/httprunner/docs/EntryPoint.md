### 用例运行入口在哪里?   
`httprunner-3.x`是基于`pytest`进行封装, 所以用例的驱动将遵循`pytest`的[运行规则](../../pytest/docs/CreateTestCase.md)来进行.  
`httprunner-3.x`的用例驱动入口是在 [HttpRunner.test_start](https://github.com/zhengtong0898/httprunner/blob/master/httprunner/runner.py#L424) .


> 问题:  
> 
> HttpRunner 这个类对象并没有以Test打头, 为什么`pytest`能够识别这个对象呢?  
> 
> 这是因为 `httprunner-3.x` 将 `yaml` 文件转换成 `.py` 测试用例文件时,  
> 会在 `.py` 文件中生成一个以Test打头的类对象, 并且让这个类对象继承 `HttpRunner` 类对象,    
> 所以用例驱动的入口最终会落在 [HttpRunner.test_start](https://github.com/zhengtong0898/httprunner/blob/master/httprunner/runner.py#L424) .
