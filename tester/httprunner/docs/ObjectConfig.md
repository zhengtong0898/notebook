### Config对象

- 从对象的角度来看, 它没有继承任何对象, 是一个简单的类对象.  
- 源码层面没有任何一个地方对Config进行初始化动作, 所以这个对象是交给框架外部来完成初始化动作.  
- 从框架[使用的角度](../apis/login_test.py)来看, 每个用例必须都要初始化一个Config对象.
- 从框架[分层的角度](../testcases/create-user-ref.yml)来看, 嵌套调用的用例都各自维护着自己的Config对象.

Config对象在单个测试用例的语境中, 它是该用例的模块变量(module variable).  


```python3
import inspect

from typing import Text

from httprunner.models import TConfig


class Config(object):
    def __init__(self, name: Text):
        self.__name = name                          # 测试用例的名称
        self.__variables = {}                       # 模块变量作用域(不含分层)
        self.__base_url = ""                        # 基础域名配置
        self.__verify = False                       # 是否开启 https 验证
        self.__export = []                          # 将变量返回到父用例的模块变量作用域.  
        self.__weight = 1                           # locust 使用的参数

        caller_frame = inspect.stack()[1]           
        self.__path = caller_frame.filename         # 追溯用例文件路径.  

    @property
    def name(self) -> Text:
        return self.__name

    @property
    def path(self) -> Text:
        return self.__path

    @property
    def weight(self) -> int:
        return self.__weight

    def variables(self, **variables) -> "Config":
        self.__variables.update(variables)
        return self

    def base_url(self, base_url: Text) -> "Config":
        self.__base_url = base_url
        return self

    def verify(self, verify: bool) -> "Config":
        self.__verify = verify
        return self

    def export(self, *export_var_name: Text) -> "Config":
        self.__export.extend(export_var_name)
        return self

    def locust_weight(self, weight: int) -> "Config":
        self.__weight = weight
        return self

    def perform(self) -> TConfig:
        return TConfig(
            name=self.__name,
            base_url=self.__base_url,
            verify=self.__verify,
            variables=self.__variables,
            export=list(set(self.__export)),
            path=self.__path,
            weight=self.__weight,
        )

```


&nbsp;  
### TConfig对象

`httprunner`使用了`pydantic`来定义数据模型,   
然后再`make`生成用例阶段会使用`pydantic.validate`来[验证用例的格式](https://github.com/zhengtong0898/httprunner/blob/master/httprunner/make.py#L450) 是否符合标准.  
除此之外并没有用到`pydantic`的其他特性.  


```python3
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


class TConfig(BaseModel):
    name: Name                                                          # 用例名字
    verify: Verify = False                                              # 是否开启https验证
    base_url: BaseUrl = ""                                              # 基础路径
    # Text: prepare variables in debugtalk.py, ${gen_variables()}
    variables: Union[VariablesMapping, Text] = {}                       # 模块变量
    parameters: Union[VariablesMapping, Text] = {}                      # 参数化
    # setup_hooks: Hooks = []
    # teardown_hooks: Hooks = []
    export: Export = []                                                 # 导出变量
    path: Text = None                                                   # 用例路径
    weight: int = 1                                                     # locust 使用的变量

```