
这是一个`hook规范签名`指标数据集合的类对象.  
将原本是字典的数据, 全部提取出来变成类的属性.  

|属性|说明|
|---|---|
|**self.namespace**|是一个类或一个模块|
|**self.function**|如果`self.namespace`是一个类, 那么`self.function`是一个方法,<br/>如果`self.namespace`是一个模块, 那么`self.function`是一个函数. |
|**self.name**|通常是`self.function`的函数名. |
|**self.argnames**|函数的固定参数清单.|
|**self.kwargnames**|函数的字典参数清单.|
|**self.opts**|`hook规范签名`的属性.|
|**self.warn_on_impl**|从`self.opts`中单独拎出来的冗余的属性.|
 

```python3
class HookSpec:
    __slots__ = (
        "namespace",
        "function",
        "name",
        "argnames",
        "kwargnames",
        "opts",
        "warn_on_impl",
    )

    def __init__(self, namespace: _Namespace, name: str, opts: "_HookSpecOpts") -> None:
        self.namespace = namespace
        self.function: Callable[..., object] = getattr(namespace, name)
        self.name = name
        self.argnames, self.kwargnames = varnames(self.function)
        self.opts = opts
        self.warn_on_impl = opts.get("warn_on_impl")

```