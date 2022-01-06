### StepRequestExtraction 对象  

- 从对象的角度来看, 它没有继承任何对象, 是一个简单的类对象.  
- 从对象的角色来看, 它负责提取变量, 目前支持`jmespath`提取, 计划支持`regex`提取.  
  除此之外它还负责收集变量.  


```python3
from typing import Text, Any, Union, Callable

from httprunner.models import (
    TConfig,
    TStep,
    TRequest,
    MethodEnum,
    TestCase,
)

class StepRequestExtraction(object):
    def __init__(self, step_context: TStep):
        self.__step_context = step_context

    # 参数 jmes_path: 提取的关键字.
    # 参数 var_name: 向上传递的变量名.  
    def with_jmespath(self, jmes_path: Text, var_name: Text) -> "StepRequestExtraction":
        self.__step_context.extract[var_name] = jmes_path
        return self

    # def with_regex(self):
    #     # TODO: extract response html with regex
    #     pass
    #
    # def with_jsonpath(self):
    #     # TODO: extract response json with jsonpath
    #     pass

    def validate(self) -> StepRequestValidation:
        return StepRequestValidation(self.__step_context)

    def perform(self) -> TStep:
        return self.__step_context
```