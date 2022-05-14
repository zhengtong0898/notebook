### Debug打印pluginmanager的_wrappers和_nonwrappers代码
```python3
for key, value in pluginmanager.hook.__dict__.items():
    if not isinstance(value, pluggy.hooks._HookCaller): continue
    if not value._nonwrappers and not value._wrappers: continue
    print(f"{key} {value}")
    print(f"        _nonwrappers: {value._nonwrappers}")
    print(f"        _wrappers: {value._wrappers}")
```
