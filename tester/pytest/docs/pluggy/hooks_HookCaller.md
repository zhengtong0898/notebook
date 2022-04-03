
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
### 对象属性  

**self.name:**   
`hook`的名称, 通常与`hook规范函数名`一致.  

**self._hookexec:**  
`hook实现函数`的执行器, 一般情况下它是`PluginManager._hookexec`, 它其实是一个代理方法.  
使用这个方法的目的是为了能够让 `PluginManager._inner_hookexec` 可被替换, 加强它的可替代性.  

**self._call_history:**  
该属性是一个历史参数集合, 也就是说`_call_history`里面有多少个元素, 那么每个`hook实现函数`就执行多少次.  
如果有多个`hook实现函数`, 那么执行次数就是 `n * n` 次.  

**self.spec:**  
该属性是一个`HookSpec`类型对象, 作用是存储`hook规范签名`的类对象、方法名、方法参数、方法的属性等信息.  
该属性通常被用来做一些`签名验证`动作: `hook实现`的方法名、参数名、参数数量与`hookspec`的方法名、参数名、参数数量是否一致.   


&nbsp;  
**HookCaller**代码片段
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

&nbsp;  
### set_specification 方法

`spec_opts: _HookSpecOpts`是字典数据, 将该字典作为参数实例化`HookSpec`对象, 完成`hook.spec`属性初始化动作.   

```python3

class _HookCaller:
    
    def set_specification(
        self,
        specmodule_or_class: _Namespace,
        spec_opts: "_HookSpecOpts",
    ) -> None:
        assert not self.has_spec()
        self.spec = HookSpec(specmodule_or_class, self.name, spec_opts)
        if spec_opts.get("historic"):
            self._call_history = []

```


&nbsp;  
### _remove_plugin 方法

由于一个`hook规范签名`可以注册多个`plugin`(实例对象),   
只要`plugin`(实例对象)的方法与`hook规范签名`一致,   
都会被加入到`_HookCaller._hookimpls`列表中.    

因此当前方法是按`plugin`在`_HookCaller._hookimpls`找到对应的`hook实现函数`并删除该对象.  
注: 一个`plugin`之会有一个`hook实现函数`, 因此这里做完删除动作后就直接`return`了.  

```python3

class _HookCaller:

    def _remove_plugin(self, plugin: _Plugin) -> None:
        for i, method in enumerate(self._hookimpls):
            if method.plugin == plugin:
                del self._hookimpls[i]
                return
        raise ValueError(f"plugin {plugin!r} not found")
```


&nbsp;  
### _add_hookimpl 方法 

当前方法维护一个"有序"列表,   
`hookimpl.tryfirst=True`会被排在列表的右侧,  
`hookimpl.trylast=True`会被排在列表的左侧,  
`hookimpl`会被排在`tryfirst`的左侧,   
`hookimpl.hookwrapper=True`会被排在和上一个`hookimpl.hookwrapper=True`的右侧.  

所以整个列表存放的顺序是: [`hookimpl.trylast=True`, `hookimpl`, `hookimpl.hookwrapper=True`, `hookimpl.tryfirst`]  

**第一段代码**  
计算出`splitpoint`的位置.


**第二段代码**  
根据`splitpoint`计算出游标位置.  


**第三段代码**  

当`hookimpl.hookwrapper=True`时,   
从左往右遍历`self._hookimpls`寻找第一个`method.hookwrapper=True`的元素位置,     
目的是为了让当前的`hookimpl`对象插入第一个`hookimpl.hookwrapper=True`的元素的右侧.  

当`hookimpl.hookwrapper=False`时,
插入在第一个`hookimpl.hookwrapper=True`元素的左侧.  

**测试用例**  
由于这个算法有点复杂, 所以需要设计几个测试用例来验证上面的表述是正确的.  
测试场景-1: [所有插件的实现都声明hookwrapper=True, 期望效果像append一样.](./testing/test_add_hookimpl.py#L4)  
测试场景-2: [混合注册插件, 期望是按trylast, normal, tryfirst, hookwrapper的分类顺序](./testing/test_add_hookimpl.py#L57)

```python3

class _HookCaller:

    def _add_hookimpl(self, hookimpl: "HookImpl") -> None:
        """Add an implementation to the callback chain."""
        for i, method in enumerate(self._hookimpls):
            if method.hookwrapper:
                splitpoint = i
                break
        else:
            splitpoint = len(self._hookimpls)

        if hookimpl.hookwrapper:
            start, end = splitpoint, len(self._hookimpls)
        else:
            start, end = 0, splitpoint

        if hookimpl.trylast:
            self._hookimpls.insert(start, hookimpl)
        elif hookimpl.tryfirst:
            self._hookimpls.insert(end, hookimpl)
        else:
            # find last non-tryfirst method
            i = end - 1
            while i >= start and self._hookimpls[i].tryfirst:
                i -= 1
            self._hookimpls.insert(i + 1, hookimpl)

```

&nbsp;  
### _verify_all_args_are_provided 方法
检查 `kwargs` 与 `hook规范签名` 的参数是否匹配.  
如果不匹配则将警告信息打印到控制台.  
注: 这个方法不会中断程序, [测试用例](./testing/test_add_hookimpl.py#L201).  
```python3

class _HookCaller:

    def _verify_all_args_are_provided(self, kwargs: Mapping[str, object]) -> None:
        # This is written to avoid expensive operations when not needed.
        if self.spec:
            for argname in self.spec.argnames:
                if argname not in kwargs:
                    notincall = ", ".join(
                        repr(argname)
                        for argname in self.spec.argnames
                        # Avoid self.spec.argnames - kwargs.keys() - doesn't preserve order.
                        if argname not in kwargs.keys()
                    )
                    warnings.warn(
                        "Argument(s) {} which are declared in the hookspec "
                        "cannot be found in this hook call".format(notincall),
                        stacklevel=2,
                    )
                    break
```

&nbsp;  
### __call__ 方法

检查所有入参(`kwargs`)和`hook规范签名`的参数是否一致, 不一致则抛出警告,  
执行所有`self._hookimpls`中的`hook实现函数`.  

```python3

class _HookCaller:
    
    def __call__(self, **kwargs: object) -> Any:
        assert (
            not self.is_historic()
        ), "Cannot directly call a historic hook - use call_historic instead."
        self._verify_all_args_are_provided(kwargs)
        firstresult = self.spec.opts.get("firstresult", False) if self.spec else False
        return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
```

&nbsp;  
### call_historic 方法  

和`self.__call__`相同, 都是根据提供的`kwargs`去执行所有个`self._hookimpls`函数,   
和`self.__call__`不同的是, 当前方法多出了两个动作:    
1. 将这次执行的`kwargs`写入到`self._call_history`中进行保存.   
2. 执行完所有的`self._hookimpls`函数后, 将返回值作为参数传给回调函数`result_callback`.    

```python3

class _HookCaller:

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
        assert self._call_history is not None
        kwargs = kwargs or {}
        self._verify_all_args_are_provided(kwargs)
        self._call_history.append((kwargs, result_callback))
        # Historizing hooks don't return results.
        # Remember firstresult isn't compatible with historic.
        res = self._hookexec(self.name, self._hookimpls, kwargs, False)
        if result_callback is None:
            return
        if isinstance(res, list):
            for x in res:
                result_callback(x)
```
