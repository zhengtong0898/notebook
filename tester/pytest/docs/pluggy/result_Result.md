### _Result 类对象的介绍  

这是一个`结果`或`异常对象`存放类对象.

```python3


class _Result(Generic[_T]):
    __slots__ = ("_result", "_excinfo")

    def __init__(self, result: Optional[_T], excinfo: Optional[_ExcInfo]) -> None:
        self._result = result
        self._excinfo = excinfo

    @property
    def excinfo(self) -> Optional[_ExcInfo]:
        return self._excinfo

    @classmethod
    def from_call(cls, func: Callable[[], _T]) -> "_Result[_T]":
        """"""

    def force_result(self, result: _T) -> None:
        """"""

    def get_result(self) -> _T:
        """"""

```

&nbsp;  
### excinfo 属性方法
这是一个代理方法, 用于访问类内的私有属性.


&nbsp;  
### from_call 方法  

该方法其实就是执行一个函数, 并且通过`try`来捕获异常,   
将执行结果和异常信息保存到一个新的`_Result`类对象中并作为结果返回给调用者.  
注: `_Result`之所以提供这个方法, 目的是为了让调用和返回的行为和结果保持统一.  

```python3

class _Result(Generic[_T]):

    @classmethod
    def from_call(cls, func: Callable[[], _T]) -> "_Result[_T]":
        __tracebackhide__ = True
        result = excinfo = None
        try:
            result = func()
        except BaseException:
            _excinfo = sys.exc_info()
            assert _excinfo[0] is not None
            assert _excinfo[1] is not None
            assert _excinfo[2] is not None
            excinfo = (_excinfo[0], _excinfo[1], _excinfo[2])

        return cls(result, excinfo)
```

&nbsp;  
### force_result 方法
该方法强制将参数`result`写入到`self._result`, 并且强制将`self._excinfo`(异常信息)置为`None`.  

```python3

class _Result(Generic[_T]):
    
    def force_result(self, result: _T) -> None:
        """Force the result(s) to ``result``.

        If the hook was marked as a ``firstresult`` a single value should
        be set, otherwise set a (modified) list of results. Any exceptions
        found during invocation will be deleted.
        """
        self._result = result
        self._excinfo = None
```




&nbsp;  
### get_result 方法  
该方法会根据`self._excinfo`的值来决定返回什么内容,  
当`self._excinfo`是`None`时, 返回`self._result`的内容,
当`self._excinfo`不是`None`时, 返回`self._excinfo.with_traceback(self._excinfo[2])`的内容.  

```python3

class _Result(Generic[_T]):

    def get_result(self) -> _T:
        """Get the result(s) for this hook call.

        If the hook was marked as a ``firstresult`` only a single value
        will be returned, otherwise a list of results.
        """
        __tracebackhide__ = True
        if self._excinfo is None:
            return cast(_T, self._result)
        else:
            ex = self._excinfo
            raise ex[1].with_traceback(ex[2])
```