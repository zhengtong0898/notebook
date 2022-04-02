import pluggy


def test_register_order_with_hookwrapper():
    """
    测试场景:
    所有 hookimpl 的 hookwrapper 都是 True.

    期望根据register顺序, 依次向尾部插入hookimpl, 效果与append一致.
    """

    hookspec = pluggy._hooks.HookspecMarker("example")
    hookimpl = pluggy._hooks.HookimplMarker("example")

    class Api:
        @hookspec
        def hello(self, arg):
            """api hook 1"""

    class Plugin1:
        @hookimpl(hookwrapper=True)
        def hello(self, arg):
            yield 1

    class Plugin2:
        @hookimpl(hookwrapper=True)
        def hello(self, arg):
            yield 2

    class Plugin3:
        @hookimpl(hookwrapper=True)
        def hello(self, arg):
            yield 3

    class Plugin4:
        @hookimpl(hookwrapper=True)
        def hello(self, arg):
            assert arg == 0
            outcome = yield
            assert outcome.get_result() == [3, 2, 1]

    pm = pluggy.PluginManager("example")

    pm.add_hookspecs(Api)

    pm.register(Plugin1())
    pm.register(Plugin2())
    pm.register(Plugin3())
    pm.register(Plugin4())

    expect_plugin_order = [Plugin1, Plugin2, Plugin3, Plugin4]  # 重点在这里
    actual_plugin_order = [hookimpl.plugin for hookimpl in pm.hook.hello._hookimpls]
    for actual_plugin, expect_plugin in zip(actual_plugin_order, expect_plugin_order):
        assert isinstance(actual_plugin, expect_plugin)


def test_register_order_mix():
    """
    测试场景:

    数据准备
        三个常规实现:              hookimpl
        三个trylast实现:          hookimpl_trylast
        三个tryfirst实现:         hookimpl_tryfirst
        三个hookwrapper=True实现: hookimpl_hookrapper

    注册顺序
        hookimpl_1
        hookimpl_1_trylast
        hookimpl_1_tryfirst
        hookimpl_1_hookwrapper

        hookimpl_2
        hookimpl_2_trylast
        hookimpl_2_tryfirst
        hookimpl_2_hookwrapper

        hookimpl_3
        hookimpl_3_trylast
        hookimpl_3_tryfirst
        hookimpl_3_hookwrapper

    期望排序
        [Hookimpl_3_trylast,
         Hookimpl_2_trylast,
         Hookimpl_1_trylast,
         Hookimpl_1,
         Hookimpl_2,
         Hookimpl_3,
         Hookimpl_1_tryfirst,
         Hookimpl_2_tryfirst,
         Hookimpl_3_tryfirst,
         Hookimpl_1_hookwrapper,
         Hookimpl_2_hookwrapper,
         Hookimpl_3_hookwrapper]
    """

    hookspec = pluggy._hooks.HookspecMarker("example")
    hookimpl = pluggy._hooks.HookimplMarker("example")

    class Api:
        @hookspec
        def hello(self, arg):
            """api hook 1"""

    class Hookimpl_1:
        @hookimpl
        def hello(self, arg):
            return 1

    class Hookimpl_1_trylast:
        @hookimpl(trylast=True)
        def hello(self, arg):
            return 1

    class Hookimpl_1_tryfirst:
        @hookimpl(tryfirst=True)
        def hello(self, arg):
            return 1

    class Hookimpl_1_hookwrapper:
        @hookimpl(hookwrapper=True)
        def hello(self, arg):
            yield 1

    class Hookimpl_2:
        @hookimpl
        def hello(self, arg):
            return 1

    class Hookimpl_2_trylast:
        @hookimpl(trylast=True)
        def hello(self, arg):
            return 1

    class Hookimpl_2_tryfirst:
        @hookimpl(tryfirst=True)
        def hello(self, arg):
            return 1

    class Hookimpl_2_hookwrapper:
        @hookimpl(hookwrapper=True)
        def hello(self, arg):
            yield 1

    class Hookimpl_3:
        @hookimpl
        def hello(self, arg):
            return 1

    class Hookimpl_3_trylast:
        @hookimpl(trylast=True)
        def hello(self, arg):
            return 1

    class Hookimpl_3_tryfirst:
        @hookimpl(tryfirst=True)
        def hello(self, arg):
            return 1

    class Hookimpl_3_hookwrapper:
        @hookimpl(hookwrapper=True)
        def hello(self, arg):
            yield 1

    pm = pluggy.PluginManager("example")
    pm.add_hookspecs(Api)

    pm.register(Hookimpl_1())
    pm.register(Hookimpl_1_trylast())
    pm.register(Hookimpl_1_tryfirst())
    pm.register(Hookimpl_1_hookwrapper())

    pm.register(Hookimpl_2())
    pm.register(Hookimpl_2_trylast())
    pm.register(Hookimpl_2_tryfirst())
    pm.register(Hookimpl_2_hookwrapper())

    pm.register(Hookimpl_3())
    pm.register(Hookimpl_3_trylast())
    pm.register(Hookimpl_3_tryfirst())
    pm.register(Hookimpl_3_hookwrapper())

    expect_plugin_order = [Hookimpl_3_trylast,
                           Hookimpl_2_trylast,
                           Hookimpl_1_trylast,
                           Hookimpl_1,
                           Hookimpl_2,
                           Hookimpl_3,
                           Hookimpl_1_tryfirst,
                           Hookimpl_2_tryfirst,
                           Hookimpl_3_tryfirst,
                           Hookimpl_1_hookwrapper,
                           Hookimpl_2_hookwrapper,
                           Hookimpl_3_hookwrapper]
    actual_plugin_order = [hookimpl.plugin for hookimpl in pm.hook.hello._hookimpls]
    for actual_plugin, expect_plugin in zip(actual_plugin_order, expect_plugin_order):
        assert isinstance(actual_plugin, expect_plugin)


def test_verify_all_args_are_provided():
    hookspec = pluggy._hooks.HookspecMarker("example")
    hookimpl = pluggy._hooks.HookimplMarker("example")

    class Api:
        @hookspec
        def hello(self, arg):
            """api hook 1"""

    class Plugin:
        @hookimpl
        def hello(self, arg):
            return 1

    pm = pluggy.PluginManager("example")
    pm.add_hookspecs(Api)
    pm.register(Plugin())
    pm.hook.hello(a="b", b="c")                         # 打印警告信息


def main():
    test_register_order_with_hookwrapper()
    test_register_order_mix()
    test_verify_all_args_are_provided()


if __name__ == '__main__':
    main()
