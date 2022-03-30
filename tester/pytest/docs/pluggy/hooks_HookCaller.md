
### _HookCaller 类对象的介绍  

**_HookCaller** 是一个`hook`管理单元, 一个`_HookCaller`对象对应一个`hook规范签名`.   

**对象关系**  
一个`pm`插件管理器对象代表一个实体插件, 关系是 1:1.  
一个`pm`可以添加多个`hook规范签名`, 关系是 1:N.  

一个`hook规范签名`对应一个`_HookCaller`, 关系是 1:1.  
一个`_HookCaller`对应多个`hookimpl`, 关系是1:N.  

所以总的来说就是`_HookCaller`是一个`hookimpl`的集中存放地, 为调用`hook实现函数`提供服务.  
在调用服务方面提供了两种策略: 一种是`LIFO`策略调用，另外一种是`historic`策略调用, 稍后下面会介绍.    


&nbsp;  
### 参数  
TODO: 待补充



```python3

class _HookCaller:
    
    __slots__ = (
        "name",
        "spec",
        "_hookexec",
        "_hookimpls",
        "_call_history",
    )

    def __init__(
        self,
        name: str,
        hook_execute: _HookExec,
        specmodule_or_class: Optional[_Namespace] = None,
        spec_opts: Optional["_HookSpecOpts"] = None,
    ) -> None:
        self.name: "Final" = name
        self._hookexec: "Final" = hook_execute
        self._hookimpls: "Final[List[HookImpl]]" = []
        self._call_history: Optional[_CallHistory] = None
        self.spec: Optional[HookSpec] = None
        if specmodule_or_class is not None:
            assert spec_opts is not None
            self.set_specification(specmodule_or_class, spec_opts)

    def has_spec(self) -> bool:
        return self.spec is not None

    def set_specification(
        self,
        specmodule_or_class: _Namespace,
        spec_opts: "_HookSpecOpts",
    ) -> None:
        """"""

    def is_historic(self) -> bool:
        return self._call_history is not None

    def _remove_plugin(self, plugin: _Plugin) -> None:
        """"""

    def get_hookimpls(self) -> List["HookImpl"]:
        return self._hookimpls.copy()

    def _add_hookimpl(self, hookimpl: "HookImpl") -> None:
        """Add an implementation to the callback chain."""

    def __repr__(self) -> str:
        return f"<_HookCaller {self.name!r}>"

    def _verify_all_args_are_provided(self, kwargs: Mapping[str, object]) -> None:
        """This is written to avoid expensive operations when not needed."""

    def __call__(self, **kwargs: object) -> Any:
        """"""

    def call_historic(
        self,
        result_callback: Optional[Callable[[Any], None]] = None,
        kwargs: Optional[Mapping[str, object]] = None,
    ) -> None:
        """Call the hook with given ``kwargs`` for all registered plugins and
        for all plugins which will be registered afterwards.

        If ``result_callback`` is provided, it will be called for each
        non-``None`` result obtained from a hook implementation.
        """

    def call_extra(
        self, methods: Sequence[Callable[..., object]], kwargs: Mapping[str, object]
    ) -> Any:
        """Call the hook with some additional temporarily participating
        methods using the specified ``kwargs`` as call parameters."""

    def _maybe_apply_history(self, method: "HookImpl") -> None:
        """Apply call history to a new hookimpl if it is marked as historic."""

```
