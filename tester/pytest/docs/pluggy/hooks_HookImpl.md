### HookImpl 类对象的介绍  

这是一个`hook实现函数`指标数据集合的类对象.  
将原本是字典的数据, 全部提取出来变成类的属性.  

```python3

_HookImplFunction = Callable[..., Union[_T, Generator[None, _Result[_T], None]]]


class HookImpl:
    
    __slots__ = (
        "function",
        "argnames",
        "kwargnames",
        "plugin",
        "opts",
        "plugin_name",
        "hookwrapper",
        "optionalhook",
        "tryfirst",
        "trylast",
    )

    def __init__(
        self,
        plugin: _Plugin,
        plugin_name: str,
        function: _HookImplFunction[object],
        hook_impl_opts: "_HookImplOpts",
    ) -> None:
        self.function: "Final" = function
        self.argnames, self.kwargnames = varnames(self.function)
        self.plugin = plugin
        self.opts = hook_impl_opts
        self.plugin_name = plugin_name
        self.hookwrapper = hook_impl_opts["hookwrapper"]
        self.optionalhook = hook_impl_opts["optionalhook"]
        self.tryfirst = hook_impl_opts["tryfirst"]
        self.trylast = hook_impl_opts["trylast"]

    def __repr__(self) -> str:
        return f"<HookImpl plugin_name={self.plugin_name!r}, plugin={self.plugin!r}>"
```