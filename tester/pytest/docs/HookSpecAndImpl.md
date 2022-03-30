### Pluggy的函数签名和实现


`hookspec = pluggy.HookspecMarker(project_name="myproject")` 的源码分析, [请参考这里](./pluggy/hooks_HookspecMarker.md).    
`hookimpl = pluggy.HookimplMarker(project_name="myproject")` 的源码分析, [请参考这里](./pluggy/hooks_HookimplMarker.md).    
`pm = pluggy.PluginManager(project_name="myproject")` 的源码分析, [请参考这里](./pluggy/manager_PluginManager.md)   


```python3
import pluggy


hookspec = pluggy.HookspecMarker(project_name="myproject")  # hookspec是一个“myproject”装饰器,用于将函数标记为钩子接口规范.
hookimpl = pluggy.HookimplMarker(project_name="myproject")  # hookimpl是一个“myproject”装饰器,为钩子做具体实现的函数/方法.


class MySpec:

    @hookspec
    def myhook(self, arg1, arg2):                           # 定义一个接口(规范)签名,
        pass                                                # 即: 这个接口必须是 myhook 方法名, 参数必须叫 arg1 和 arg2.


class Plugin_1:

    @hookimpl
    def myhook(self, arg1, arg2):                           # 定义一个接口实现, 参数必须与接口(规范)签名一致.
        print("inside Plugin_1.myhook()")
        return arg1 + arg2


class Plugin_2:

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return arg1 - arg2


pm = pluggy.PluginManager(project_name="myproject")         # 创建一个名为"myproject"的插件管理器实例对象: pm.
pm.add_hookspecs(MySpec)                                    # 读取 MySpec 类中的所有方法,
                                                            # 找到那些属性是"myproject_spec"的方法,
                                                            # 将这些方法绑定到 pm.hook.方法名中.
                                                            # 补充: pm.hook.方法名: _HookCaller 类型

pm.register(Plugin_1())                                     # 读取 Plugin_1 实例对象中的所有方法,
                                                            # 找到那些属性是"myproject_impl"的方法,
                                                            # 将这些方法绑定到
                                                            #     pm.hook.方法名._wrappers 或
                                                            #     pm.hook.方法名._nonwrappers 中.
pm.register(Plugin_2())


results = pm.hook.myhook(arg1=1, arg2=2)                    # pm.hook.myhook: _HookCaller 类型
                                                            # 这里触发的是 _HookCaller.__call__ 方法.
                                                            # 先获取所有的实现(get_hookimpls),
                                                            # 然后丢给 _callers._multicall 去执行.
                                                            # 执行策略是: LIFO.
                                                            # 写入采取: append.
                                                            # 执行采取: pop.

print(results)                                              # [-1, 3]
```
