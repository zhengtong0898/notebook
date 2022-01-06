### RequestWithOptionalArgs 对象

- 从对象的角度来看, 它没有继承任何对象, 是一个简单的类对象.  
- 从对象的角色来看, 它主要是围绕`requests`的参数规格提供了一系列方法来收集对应的参数.

```python3
from typing import Text, Any, Union, Callable

from httprunner.models import (
    TConfig,
    TStep,
    TRequest,
    MethodEnum,
    TestCase,
)

class RequestWithOptionalArgs(object):
    def __init__(self, step_context: TStep):
        self.__step_context = step_context

    def with_params(self, **params) -> "RequestWithOptionalArgs":
        self.__step_context.request.params.update(params)
        return self

    def with_headers(self, **headers) -> "RequestWithOptionalArgs":
        self.__step_context.request.headers.update(headers)
        return self

    def with_cookies(self, **cookies) -> "RequestWithOptionalArgs":
        self.__step_context.request.cookies.update(cookies)
        return self

    def with_data(self, data) -> "RequestWithOptionalArgs":
        self.__step_context.request.data = data
        return self

    def with_json(self, req_json) -> "RequestWithOptionalArgs":
        self.__step_context.request.req_json = req_json
        return self

    def set_timeout(self, timeout: float) -> "RequestWithOptionalArgs":
        self.__step_context.request.timeout = timeout
        return self

    def set_verify(self, verify: bool) -> "RequestWithOptionalArgs":
        self.__step_context.request.verify = verify
        return self

    def set_allow_redirects(self, allow_redirects: bool) -> "RequestWithOptionalArgs":
        self.__step_context.request.allow_redirects = allow_redirects
        return self

    def upload(self, **file_info) -> "RequestWithOptionalArgs":
        self.__step_context.request.upload.update(file_info)
        return self

    def teardown_hook(
        self, hook: Text, assign_var_name: Text = None
    ) -> "RequestWithOptionalArgs":
        if assign_var_name:
            self.__step_context.teardown_hooks.append({assign_var_name: hook})
        else:
            self.__step_context.teardown_hooks.append(hook)

        return self

    def extract(self) -> StepRequestExtraction:
        return StepRequestExtraction(self.__step_context)

    def validate(self) -> StepRequestValidation:
        return StepRequestValidation(self.__step_context)

    def perform(self) -> TStep:
        return self.__step_context

```