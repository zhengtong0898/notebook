### varnames 函数的介绍  

提取函数或方法的形参(也就是所谓的签名).  
注: 只支持常规的`必填参数`和`可选参数`, 不支持`可变长参数`、`关键字参数`、`固定参数`, 不理解这几个词汇请参考[这里](../../../../python/ArgumentParameter.md).  

```python3

_PYPY = hasattr(sys, "pypy_version_info")


def varnames(func: object) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    # 第一段代码, 是泛化.
    # 如果func是类对象, 那么就将 func.__init__ 泛化成一个函数.
    # 如果func是一个协程对象, 那么就将 func.__call__ 泛化成一个函数.
    if inspect.isclass(func):
        try:
            func = func.__init__
        except AttributeError:
            return (), ()
    elif not inspect.isroutine(func):  # callable object?
        try:
            func = getattr(func, "__call__", func)
        except Exception:
            return (), ()

    # 第二段代码, 是提取函数的签名.
    # 参考: https://reurl.cc/RjpLRD
    try:  # func MUST be a function or method here or we won't parse any args
        spec = inspect.getfullargspec(func)
    except TypeError:
        return (), ()

    # 第三段代码, 只提取函数的形参, 不要实参.
    args, defaults = tuple(spec.args), spec.defaults
    if defaults:
        index = -len(defaults)
        args, kwargs = args[:index], tuple(args[index:])
    else:
        kwargs = ()

    # 第四段代码, 剔除self签名.
    # 为了支持pypy, 增加剔除obj签名.
    if not _PYPY:
        implicit_names: Tuple[str, ...] = ("self",)
    else:
        implicit_names = ("self", "obj")
        
    # 第五段代码, 二次处理args签名.
    # 如果func是一个方法, 那么就剔除掉self这个签名.  
    if args:
        qualname: str = getattr(func, "__qualname__", "")
        if inspect.ismethod(func) or ("." in qualname and args[0] in implicit_names):
            args = args[1:]

    return args, kwargs
```