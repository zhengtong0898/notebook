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


&nbsp;  
### TStep对象

`httprunner`使用了`pydantic`来定义数据模型,   
然后再`make`生成用例阶段会使用`pydantic.validate`来[验证用例的格式](https://github.com/zhengtong0898/httprunner/blob/master/httprunner/make.py#L450) 是否符合标准.  
除此之外并没有用到`pydantic`的其他特性.  

```python3
from enum import Enum
from typing import Any
from typing import Dict, Text, Union, Callable
from typing import List

from pydantic import BaseModel, Field
from pydantic import HttpUrl


Name = Text
Url = Text
BaseUrl = Union[HttpUrl, Text]
VariablesMapping = Dict[Text, Any]
FunctionsMapping = Dict[Text, Callable]
Headers = Dict[Text, Text]
Cookies = Dict[Text, Text]
Verify = bool
Hooks = List[Union[Text, Dict[Text, Text]]]
Export = List[Text]
Validators = List[Dict]
Env = Dict[Text, Any]


class MethodEnum(Text, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"


class TRequest(BaseModel):
    """requests.Request model"""

    method: MethodEnum                                                # requests method
    url: Url                                                          # requests url
    params: Dict[Text, Text] = {}                                     # requests params
    headers: Headers = {}                                             # requests headers
    req_json: Union[Dict, List, Text] = Field(None, alias="json")     # requests json
    data: Union[Text, Dict[Text, Any]] = None                         # requests data
    cookies: Cookies = {}                                             # requests cookies
    timeout: float = 120                                              # requests timeout
    allow_redirects: bool = True                                      # requests allow_redirects
    verify: Verify = False                                            # requests verify
    upload: Dict = {}  # used for upload files                        # requests upload


class TStep(BaseModel):
    name: Name                                                        # 测试步骤名字
    request: Union[TRequest, None] = None                             # requests请求参数对象
    testcase: Union[Text, Callable, None] = None                      # 测试用例
    variables: VariablesMapping = {}                                  # 函数变量(function variable) + 
                                                                      # 上一个步骤的提取变量(extract variable) +
                                                                      # 模块变量(module variable)
    setup_hooks: Hooks = []                                           # 测试用例的前置
    teardown_hooks: Hooks = []                                        # 测试用例的后置
    # used to extract request's response field
    extract: VariablesMapping = {}                                    # 提取变量(extract variable)
    # used to export session variables from referenced testcase
    export: Export = []                                               # 导出变量给父用例
    validators: Validators = Field([], alias="validate")              # 断言
    validate_script: List[Text] = []
```