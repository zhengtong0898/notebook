### _multicall 函数的介绍  

执行一组签名相同的`hook实现函数`, 返回一组结果.  

```python3

def _multicall(
    hook_name: str,
    hook_impls: Sequence["HookImpl"],
    caller_kwargs: Mapping[str, object],
    firstresult: bool,
) -> Union[object, List[object]]:
    __tracebackhide__ = True
    results: List[object] = []
    excinfo = None
    try:  # run impl and wrapper setup functions in a loop
        teardowns = []
        try:
            for hook_impl in reversed(hook_impls):
                try:
                    args = [caller_kwargs[argname] for argname in hook_impl.argnames]
                except KeyError:
                    for argname in hook_impl.argnames:
                        if argname not in caller_kwargs:
                            raise HookCallError(
                                f"hook call must provide argument {argname!r}"
                            )

                if hook_impl.hookwrapper:
                    try:
                        # If this cast is not valid, a type error is raised below,
                        # which is the desired response.
                        res = hook_impl.function(*args)
                        gen = cast(Generator[None, _Result[object], None], res)
                        next(gen)  # first yield
                        teardowns.append(gen)
                    except StopIteration:
                        _raise_wrapfail(gen, "did not yield")
                else:
                    res = hook_impl.function(*args)
                    if res is not None:
                        results.append(res)
                        if firstresult:  # halt further impl calls
                            break
        except BaseException:
            _excinfo = sys.exc_info()
            assert _excinfo[0] is not None
            assert _excinfo[1] is not None
            assert _excinfo[2] is not None
            excinfo = (_excinfo[0], _excinfo[1], _excinfo[2])
    finally:
        if firstresult:  # first result hooks return a single value
            outcome: _Result[Union[object, List[object]]] = _Result(
                results[0] if results else None, excinfo
            )
        else:
            outcome = _Result(results, excinfo)

        # run all wrapper post-yield blocks
        for gen in reversed(teardowns):
            try:
                gen.send(outcome)
                _raise_wrapfail(gen, "has second yield")
            except StopIteration:
                pass

        return outcome.get_result()

```


&nbsp;  
### 参数  
**hook_name:** 要求必填, 但是未使用.  
**hook_impls:** 一组`hook实现函数`.  
**caller_kwargs:** 作为执行这一组`hook实现函数`的参数.  
**firstresult:** 只返回第一个结果.  


&nbsp;  
### 遍历`hook_impls`

**第一段代码:** `caller_kwargs.keys()`必须涵盖所有`hook_impl.argnames`的参数名.  
**第二段代码:** 当`hook_impl.hookwrapper=True`时, 实例化和执行(`next`)生成器, 将挂起的生成器添加到`teardowns`列表中.  
**第三段代码:** 当`hook_impl.hookwrapper=False`时, 执行`hook实现函数`并将执行结果写入到`results`列表中.  

```python3

for hook_impl in reversed(hook_impls):
    
    # 第一段代码
    try:
        args = [caller_kwargs[argname] for argname in hook_impl.argnames]
    except KeyError:
        for argname in hook_impl.argnames:
            if argname not in caller_kwargs:
                raise HookCallError(
                    f"hook call must provide argument {argname!r}"
                )

    # 第二段代码
    if hook_impl.hookwrapper:
        try:
            # If this cast is not valid, a type error is raised below,
            # which is the desired response.
            res = hook_impl.function(*args)
            gen = cast(Generator[None, _Result[object], None], res)
            next(gen)  # first yield
            teardowns.append(gen)
        except StopIteration:
            _raise_wrapfail(gen, "did not yield")
            
    # 第三段代码
    else:
        res = hook_impl.function(*args)
        if res is not None:
            results.append(res)
            if firstresult:  # halt further impl calls
                break

```


&nbsp;  
### 收集异常信息

当函数执行抛异常时, 将异常信息收集在excinfo变量中.  

```python3

try:
    for hook_impl in reversed(hook_impls):
        ...
except BaseException:
    _excinfo = sys.exc_info()
    assert _excinfo[0] is not None
    assert _excinfo[1] is not None
    assert _excinfo[2] is not None
    excinfo = (_excinfo[0], _excinfo[1], _excinfo[2])
```

&nbsp;  
### 二次收集执行结果  

**第一段代码:** 当`firstresult=True`时, 只将`第一个执行结果`和`异常信息`作为参数实例化`_Result`.  
**第二段代码:** 当`firstresult=False`时, 将`整个执行结果列表`和`异常信息`作为参数实例化`_Result`.  
**第三段代码:** 继续触发执行那些(`teardowns`)挂起来的`hook实现函数`, `_Result`作为参数传递进去.  
**第四段代码:** 当`excinfo is None`时, 返回执行结果列表(`results`); 当`excinfo is not None`时, 执行`raise`抛异常.  

```python3
try:
    try:
        for hook_impl in reversed(hook_impls):
            ...
    except BaseException:
        ...
finally:
    
    # 第一段代码
    if firstresult:  # first result hooks return a single value
        outcome: _Result[Union[object, List[object]]] = _Result(
            results[0] if results else None, excinfo
        )
        
    # 第二段代码
    else:
        outcome = _Result(results, excinfo)

    # 第三段代码
    # run all wrapper post-yield blocks
    for gen in reversed(teardowns):
        try:
            gen.send(outcome)
            _raise_wrapfail(gen, "has second yield")
        except StopIteration:
            pass

    # 第四段代码
    return outcome.get_result()
```

