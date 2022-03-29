
### HookimplMarker 类对象的介绍

**HookimplMarker**类是一个装饰器类, 用于将函数`标记`为是`hook实现函数`.  

**HookimplMarker**类通过实例化成为一个装饰器, 实例化需要提供一个`project_name`字符串参数, 像这样:  
`hookimpl = pluggy.HookimplMarker(project_name="myproject")`
此时 `hookimpl` 是一个装饰器, 可以用来挂载在函数或者方法中, 标记该方法是一个`hook实现函数`.  
通常装饰器有两种写法, 一种是直接挂载装饰器, 另外一种是挂载装饰器的同时带一些参数.  

**第一种写法:** 不带任何参数直接使用装饰器 
```python3
class Plugin_1:

    @hookimpl
    def myhook(self, arg1, arg2):                           # 定义一个接口实现, 参数必须与接口(规范)签名一致.
        print("inside Plugin_1.myhook()")
        return arg1 + arg2
```


**第二种写法:** 带参数使用装饰器.
```python3

def test_hookwrapper() -> None:
    out = []

    @hookimpl(hookwrapper=True)
    def m1():
        out.append("m1 init")
        yield None
        out.append("m1 finish")

```

TODO: 参数补充说明.

&nbsp;  
**HookspecMarker**代码片段
```python3
from typing import (
    AbstractSet,
    Any,
    Callable,
    Generator,
    List,
    Mapping,
    Optional,
    overload,
    Sequence,
    Tuple,
    TypeVar,
    TYPE_CHECKING,
    Union,
)


_F = TypeVar("_F", bound=Callable[..., object])


class HookimplMarker:
    """Decorator for marking functions as hook implementations.

    Instantiate it with a ``project_name`` to get a decorator.
    Calling :meth:`PluginManager.register` later will discover all marked
    functions if the :class:`PluginManager` uses the same project_name.
    """

    __slots__ = ("project_name",)

    def __init__(self, project_name: str) -> None:
        self.project_name: "Final" = project_name

    def __call__(  # noqa: F811
        self,
        function: Optional[_F] = None,
        hookwrapper: bool = False,
        optionalhook: bool = False,
        tryfirst: bool = False,
        trylast: bool = False,
        specname: Optional[str] = None,
    ) -> Union[_F, Callable[[_F], _F]]:
        """If passed a function, directly sets attributes on the function
        which will make it discoverable to :meth:`PluginManager.register`.

        If passed no function, returns a decorator which can be applied to a
        function later using the attributes supplied.

        If ``optionalhook`` is ``True``, a missing matching hook specification
        will not result in an error (by default it is an error if no matching
        spec is found).

        If ``tryfirst`` is ``True``, this hook implementation will run as early
        as possible in the chain of N hook implementations for a specification.

        If ``trylast`` is ``True``, this hook implementation will run as late as
        possible in the chain of N hook implementations.

        If ``hookwrapper`` is ``True``, the hook implementations needs to
        execute exactly one ``yield``. The code before the ``yield`` is run
        early before any non-hookwrapper function is run. The code after the
        ``yield`` is run after all non-hookwrapper function have run  The
        ``yield`` receives a :class:`_Result` object representing the exception
        or result outcome of the inner calls (including other hookwrapper
        calls).

        If ``specname`` is provided, it will be used instead of the function
        name when matching this hook implementation to a hook specification
        during registration.
        """

        def setattr_hookimpl_opts(func: _F) -> _F:
            opts: "_HookImplOpts" = {
                "hookwrapper": hookwrapper,
                "optionalhook": optionalhook,
                "tryfirst": tryfirst,
                "trylast": trylast,
                "specname": specname,
            }
            setattr(func, self.project_name + "_impl", opts)
            return func

        if function is None:
            return setattr_hookimpl_opts
        else:
            return setattr_hookimpl_opts(function)
```