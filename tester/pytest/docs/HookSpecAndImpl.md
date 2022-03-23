### Pluggy的函数签名和实现

```python3
import pluggy

hookspec = pluggy.HookspecMarker(project_name="myproject")  # 定义一个接口(规范)集合
hookimpl = pluggy.HookimplMarker(project_name="myproject")  # 定义一个实现集合


class MySpec:

    @hookspec
    def myhook(self, arg1, arg2):                           # 定义一个接口(规范)签名                   
        pass


class Plugin_1:

    @hookimpl
    def myhook(self, arg1, arg2):                           # 定义一个接口实现, 参数必须与接口(规范)签名一致.
        print("inside Plugin_1.myhook()")
        return arg1 + arg2


class Plugin_2:

    @hookimpl
    def myhook(self, arg1, arg2):                           # 定义一个接口实现, 参数必须与接口(规范)签名一致.
        print("inside Plugin_2.myhook()")
        return arg1 - arg2


pm = pluggy.PluginManager(project_name="myproject")         # 创建一个插件管理器, 通过project_name来绑定和匹配.
pm.add_hookspecs(MySpec)                                    # 将一个类中的多个 @hookspec 接口规范签名添加到插件管理器实例pm中. 
pm.register(Plugin_1())                                     # 将一个类中的多个 @hookimpl 接口实现注册到插件管理器实例pm中.
pm.register(Plugin_2())                                     
results = pm.hook.myhook(arg1=1, arg2=2)                    # 根据 @hookspec 的接口(规范)签名来触发调用对应的实现.
                                                            # pm从实现清单中找到了两个对应的实现, 因此会按照LIFO逐一的执行这两个实现.
print(results)                                              # [-1, 3]
```
