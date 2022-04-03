### __SubsetHookCaller 类对象的介绍  

`_SubsetHookCaller`是一个继承了`_HookCaller`的派生类对象,   
这个对象重写了`_hookimpls`方法, 返回提出了`self._remove_plugins`后的`self._hookimpls`集合.  

虽然说是继承, 但是从`spec`和`_call_history`这两个方法来看, `_SubsetHookCaller`更像是一个代理类.


```python3
class _SubsetHookCaller(_HookCaller):
    """A proxy to another HookCaller which manages calls to all registered
    plugins except the ones from remove_plugins."""

    # This class is unusual: in inhertits from `_HookCaller` so all of
    # the *code* runs in the class, but it delegates all underlying *data*
    # to the original HookCaller.
    # `subset_hook_caller` used to be implemented by creating a full-fledged
    # HookCaller, copying all hookimpls from the original. This had problems
    # with memory leaks (#346) and historic calls (#347), which make a proxy
    # approach better.
    # An alternative implementation is to use a `_getattr__`/`__getattribute__`
    # proxy, however that adds more overhead and is more tricky to implement.

    __slots__ = (
        "_orig",
        "_remove_plugins",
        "name",
        "_hookexec",
    )

    def __init__(self, orig: _HookCaller, remove_plugins: AbstractSet[_Plugin]) -> None:
        self._orig = orig
        self._remove_plugins = remove_plugins
        self.name = orig.name  # type: ignore[misc]
        self._hookexec = orig._hookexec  # type: ignore[misc]

    @property  # type: ignore[misc]
    def _hookimpls(self) -> List["HookImpl"]:  # type: ignore[override]
        return [
            impl
            for impl in self._orig._hookimpls
            if impl.plugin not in self._remove_plugins
        ]

    @property
    def spec(self) -> Optional["HookSpec"]:  # type: ignore[override]
        return self._orig.spec

    @property
    def _call_history(self) -> Optional[_CallHistory]:  # type: ignore[override]
        return self._orig._call_history

    def __repr__(self) -> str:
        return f"<_SubsetHookCaller {self.name!r}>"
```
