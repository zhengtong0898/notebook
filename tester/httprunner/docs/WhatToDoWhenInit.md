### httprunner框架的用例初始化阶段在做什么?
已知用例运行入口是在 [HttpRunner.test_start](./EntryPoint.md) 之后, 这里关注的是 `self.__init_tests__()` 在做什么.  

- `self.config.perform()` 返回的是 `TConfig` 对象.  
- `step.perform()` 返回的是 `TStep` 对象.

通过这两个`.perform()`动作可以看出, `HttpRunner`是将类对象转换成了数据模型对象.  
换句话说就是 [由httprunner框架生成的测试用例](../testcases/create_user_ref_test.py) 只是一个数据承接载体, 这些对象的目的是为了有效的收集数据. 


```python3
from typing import Dict, NoReturn


class HttpRunner(object):

    config: Config
    teststeps: List[Step]
    
    __config: TConfig
    __teststeps: List[TStep]
    
    def __init_tests__(self) -> NoReturn:
        self.__config = self.config.perform()                  # self.config.perform() 返回的是 TConfig 对象.
        self.__teststeps = []
        for step in self.teststeps:                            
            self.__teststeps.append(step.perform())            # step.perform() 返回的是 TStep 对象.  
    
    def test_start(self, param: Dict = None) -> "HttpRunner":
        """main entrance, discovered by pytest"""
        self.__init_tests__()                                  # 当前文章关注点在这里.  

```
