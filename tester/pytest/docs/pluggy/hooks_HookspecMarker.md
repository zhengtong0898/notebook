
### HookspecMarker 类对象的介绍

**HookspecMarker**类是一个装饰器类, 用于将函数`标记`为是`hook规范`.   
`hook规范`指的是根据 `函数名` + `函数参数` 组成的一个约束, 所有的`hook实现`都必须与该规范保持一致才能被识别和执行.  
`标记`指的是在`代码load阶段`为其注入一些`键值属性`, 其中`Key`=`project_name_spec` 而 `value`是一个子键值字典.  

**HookspecMarker**类通过实例化成为一个装饰器, 实例化需要提供一个`project_name`字符串参数, 像这样:  
`pm = pluggy.PluginManager(project_name="myproject")`  
`标记`、`查找`、`注册` 全部都是围绕 `project_name` 来展开, 所以这个参数至关重要, 举例:  

当执行`pm.add_hookspecs(MySpec)`时, 它会去查找`MySpec`类中的所有方法,   
那些属性中包含了`myproject_spec`的方法, 都会被收录在`pm.hook: _HookRelay`中作为一个子属性而存在.  
比如说 `MySpec` 有一个 `myhook` 方法是`hook规范`.


当执行`pm.register(Plugin_1())`时, 它会去查找`Plugin_1`对象中的所有方法,  
只有当 `Plugin_1` 中有 `myhook` 方法并且属性中包含了`myproject_impl`键值信息.  
满足了这两个条件才会被收录在`pm.hook.myhook._wrappers`或`pm.hook.myhook._nonwrappers`列表中.    


```python3
import inspect
import sys
import warnings


class HookspecMarker:
    """
    Decorator helper class for marking functions as hook specifications.
    You can instantiate it with a project_name to get a decorator.
    
    Calling :py:meth:`.PluginManager.add_hookspecs` later will discover all marked functions
    if the :py:class:`.PluginManager` uses the same project_name.
    """

    def __init__(self, project_name):
        self.project_name = project_name

    def __call__(
        self, function=None, firstresult=False, historic=False, warn_on_impl=None
    ):
        """
        if passed a function, directly sets attributes on the function
        which will make it discoverable to :py:meth:`.PluginManager.add_hookspecs`.
        不带任何参数直接使用装饰器, 例如:  
        class MySpec:
        
            @hookspec                                   # 不带任何参数
            def myhook(self, arg1, arg2):                                  
                pass

        这个装饰器会给函数打上一些属性: function.f"{project_name}_spec" = dict(firstresult=False,
                                                                         historic=False,
                                                                         warn_on_impl=None)
                                                                         
        pm = PluginManager(project_name="myproject")    # 会尝试去查找SpecClass类中的所有方法, 
        pm.add_hookspecs(SpecClass)                     # 那些包含了f"myproject_spec"属性的方法, 都会被找到.
        
        
        If passed no function, returns a decorator which can be applied to a function
        later using the attributes supplied.
        带参数使用装饰器, 例如:
        @hookspec(historic=True)                        # 带参数使用装饰器
        def pytest_addhooks(pluginmanager: "PytestPluginManager") -> None:
            pass
        
        TODO: 这种使用场景待补充.
        

        If ``firstresult`` is ``True`` the 1:N hook call (N being the number of registered
        hook implementation functions) will stop at I<=N when the I'th function
        returns a non-``None`` result.
        当 `firstresult` 是 `True` 时, 任意一个`implement`返回值是非None时, 就停止执行后续的`implement`.   
        验证依据: pluggy/testing/test_invocations.test_firstresult_definition 在这个测试用例中断点调试.  
        

        If ``historic`` is ``True`` calls to a hook will be memorized and replayed
        on later registered plugins.  
        TODO: 待补充.

        """

        def setattr_hookspec_opts(func):
            if historic and firstresult:
                raise ValueError("cannot have a historic firstresult hook")
            setattr(
                func,
                self.project_name + "_spec",
                dict(
                    firstresult=firstresult,
                    historic=historic,
                    warn_on_impl=warn_on_impl,
                ),
            )
            return func

        if function is not None:
            return setattr_hookspec_opts(function)
        else:
            return setattr_hookspec_opts
```