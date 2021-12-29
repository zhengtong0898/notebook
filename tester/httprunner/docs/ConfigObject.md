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