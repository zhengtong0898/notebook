### Step对象

- 从对象的角度来看, 它没有继承任何对象, 是一个简单的类对象.  
- 源码层面没有任何一个地方对Config进行初始化动作, 所以这个对象是交给框架外部来完成初始化动作.  
- 从框架[使用的角度](../testcases/create_user_ref_test.py)来看, `testcases属性`中的每一个步骤都必须包含一个`Step`对象.  
- 从对象初始化的参数要求来看, `step_context`是由外部传入进来(已实例化)的对象, 它们都有一个共同特征就是`.perform()`会返回`TStep`数据模型对象.  

Step对象并没有更多的实质用处, 它的目的就是为了统一用例的组织口径.  

```python3
from typing import Union

from httprunner.models import (
    TStep,
    TRequest,
    TestCase,
)

class Step(object):
    def __init__(
        self,
        step_context: Union[
            StepRequestValidation,                      # StepRequestValidation.perform()   将会返回 TStep 数据模型对象.
            StepRequestExtraction,                      # StepRequestExtraction.perform()   将会返回 TStep 数据模型对象.
            RequestWithOptionalArgs,                    # RequestWithOptionalArgs.perform() 将会返回 TStep 数据模型对象.
            RunTestCase,                                # RunTestCase.perform()             将会返回 TStep 数据模型对象.
            StepRefCase,                                # StepRefCase.perform()             将会返回 TStep 数据模型对象.
        ],
    ):
        self.__step_context = step_context.perform()    # self.__step_context 的类型是 TStep.
                                                        # TODO 为什么加上:TStep 会报黄, 这里可能是个Bug, 先标记作为待处理事项. 

    @property
    def request(self) -> TRequest:
        return self.__step_context.request              

    @property
    def testcase(self) -> TestCase:
        return self.__step_context.testcase

    def perform(self) -> TStep:
        return self.__step_context

```