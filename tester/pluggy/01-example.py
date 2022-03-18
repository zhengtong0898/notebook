"""
这是官方提供的一个 toy example 的样例代码.

代码关系:
1. 定义 MySpec 类对象, 用于描述当前 "myproject" 这个 plugin 的标准接口函数 和 函数的参数签名(指纹).
2. 定义 Plugin_1 和 Plugin_2 类对象, 通常需要严格按照 MySpec 类对象定义的公共接口和参数签名做对应的实现.

代码行为:
hookspec = pluggy.HookspecMarker("myproject")       # hookspec 是一个装饰器, 被装饰对象表示是 "myproject" 的标准接口函数.
hookimpl = pluggy.HookimplMarker("myproject")       # hookimpl 是一个装饰器, 被装饰对象表示是 "myproject" 的具体实现函数.

pm = pluggy.PluginManager("myproject")              # 创建一个名为 "myproject" 的 plugin.
pm.add_hookspecs(MySpec)                            # 将 MySpec 对象作为检查标准, 只要 MySpec 内的方法声明了 @hookspec 装饰器,
                                                    # 都将会作为检查标准, 检查标准: 方法名 + 参数名, 做一致性检查.

pm.register(Plugin_1())                             # 具体的实现, 注册到 pm 对象中.
pm.register(Plugin_2())                             # 这两个实现, 只有符合: 方法名 + 参数名, 才会做检查, 当不一致时, 就会报错.

results = pm.hook.myhook(arg1=1, arg2=2)            # 按照 LIFO 的方式在执行所有 register 的 myhook 方法.
"""
import pluggy


hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")


class MySpec:
    """A hook specification namespace.
    """

    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize.
        """


class Plugin_1:
    """A hook implementation namespace.
    """

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return arg1 + arg2


class Plugin_2:
    """A 2nd hook implementation namespace.
    """

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return arg1 - arg2


# create a manager and add the spec
pm = pluggy.PluginManager("myproject")
pm.add_hookspecs(MySpec)

# register plugins
pm.register(Plugin_1())
pm.register(Plugin_2())

# call our ``myhook`` hook
results = pm.hook.myhook(arg1=1, arg2=2)
print(results)