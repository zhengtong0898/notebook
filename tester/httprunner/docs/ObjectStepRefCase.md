### StepRefCase 对象

- 从对象的角度来看, 它没有继承任何对象, 是一个简单的类对象.  
- 从对象的角色来看, 它只负责收集`export`变量.  

```python3
from typing import Text, Any, Union, Callable

from httprunner.models import (
    TConfig,
    TStep,
    TRequest,
    MethodEnum,
    TestCase,
)

class StepRefCase(object):
    def __init__(self, step_context: TStep):
        self.__step_context = step_context

    # TODO: 待补充.
    def teardown_hook(self, hook: Text, assign_var_name: Text = None) -> "StepRefCase":
        if assign_var_name:
            self.__step_context.teardown_hooks.append({assign_var_name: hook})
        else:
            self.__step_context.teardown_hooks.append(hook)

        return self

    # 将变量名写入到 TStep.export 然后返回自己.
    def export(self, *var_name: Text) -> "StepRefCase":
        self.__step_context.export.extend(var_name)
        return self

    def perform(self) -> TStep:
        return self.__step_context

```
