```python3
import inspect
import sys
import warnings


class HookspecMarker:
    """
    Decorator helper class for marking functions as hook specifications.
    当前类对象是一个装饰器类, 用于将函数标记为是钩子规范, 所谓的钩子规范指的是公共的接口和其参数约束.  

    You can instantiate it with a project_name to get a decorator.
    要让当前类成为一个装饰器, 需要先实例化当前类, 并且提供一个project_name字符串参数.
    
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