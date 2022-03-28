
### HookspecMarker 类对象的介绍

**HookspecMarker**类是一个装饰器类, 用于将函数`标记`为是`hook规范`.   
`hook规范`指的是根据 `函数名` + `函数参数` 组成的一个约束, 所有的`hook实现`都必须与该规范保持一致才能被识别和执行.  
`标记`指的是在`代码load阶段`为其注入一些`键值属性`, 其中`Key`=`project_name_spec` 而 `value`是一个子键值字典.  

**HookspecMarker**类通过实例化成为一个装饰器, 实例化需要提供一个`project_name`字符串参数, 像这样:  
`hookspec = pluggy.HookspecMarker(project_name="myproject")`  
此时 `hookspec` 是一个装饰器, 可以用来挂载在函数或者方法中, 标记该方法是一个`hook接口规范`.  
通常装饰器有两种写法, 一种是直接挂载装饰器, 另外一种是挂载装饰器的同时带一些参数.  

**第一种写法:** 不带任何参数直接使用装饰器   
`hookspec`装饰器会给`myhook方法`添加一个字典属性,   
`key`==`"myproject_spec"`,    
`value`==`dict(firstresult=False,historic=False,warn_on_impl=None)`   
```python3
class MySpec:

    @hookspec                                   # 不带任何参数, 隐藏信息: myhook方法作为function的参数
    def myhook(self, arg1, arg2):                                  
        pass
```

**第二种写法:** 带参数使用装饰器.
```python3
@hookspec(historic=True)                        # 带参数使用装饰器, 隐藏信息: function参数的值是None
def pytest_addhooks(pluginmanager: "PytestPluginManager") -> None:
    pass
```

**firstresult:** 当 `firstresult` 参数是 `True` 时, 任意一个`implement`返回值是非None时, 就停止执行后续的`implement`.   
验证依据: pluggy/testing/test_invocations.test_firstresult_definition 在这个测试用例中断点调试.  


**historic:** 当 `historic` 参数是 `True` 时,   
每次注册`hook实现函数`时会尝试执行该实现, 每次`call_historic`都会增加一个`_cal_history`.  

**warn_on_impl:** 这是一个警告对象参数, 通常用于通知插件即将过期或者即将废弃.  

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



class HookspecMarker:
    """Decorator for marking functions as hook specifications.

    Instantiate it with a project_name to get a decorator.
    Calling :meth:`PluginManager.add_hookspecs` later will discover all marked
    functions if the :class:`PluginManager` uses the same project_name.
    """

    __slots__ = ("project_name",)

    def __init__(self, project_name: str) -> None:
        self.project_name: "Final" = project_name

    def __call__(  # noqa: F811
        self,
        function: Optional[_F] = None,
        firstresult: bool = False,
        historic: bool = False,
        warn_on_impl: Optional[Warning] = None,
    ) -> Union[_F, Callable[[_F], _F]]:
        """
        if passed a function, directly sets attributes on the function
        which will make it discoverable to :py:meth:`.PluginManager.add_hookspecs`.
        
        If passed no function, returns a decorator which can be applied to a function
        later using the attributes supplied.
        
        If ``firstresult`` is ``True`` the 1:N hook call (N being the number of registered
        hook implementation functions) will stop at I<=N when the I'th function
        returns a non-``None`` result.
        
        If ``historic`` is ``True`` calls to a hook will be memorized and replayed
        on later registered plugins.  

        """

        def setattr_hookspec_opts(func: _F) -> _F:
            if historic and firstresult:
                raise ValueError("cannot have a historic firstresult hook")
            opts: "_HookSpecOpts" = {
                "firstresult": firstresult,
                "historic": historic,
                "warn_on_impl": warn_on_impl,
            }
            setattr(func, self.project_name + "_spec", opts)
            return func

        if function is not None:
            return setattr_hookspec_opts(function)
        else:
            return setattr_hookspec_opts

```