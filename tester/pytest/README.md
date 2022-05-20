### Pytest入门
1. [Pytest是如何识别一个测试用例的?](./docs/HowToFindTestCase.md)  
2. [如何写一个测试用例?](./docs/CreateTestCase.md)  
3. [如何实时打印logging日志信息?](./examples/live_logs/README.md)  
4. [如何展示错误堆栈中的变量?](./examples/showlocals/README.md)  
5. [如何动态生成allure报告?](./examples/dynamic_generate_allure_report/README.md)  
6. [Pytest由那些组件构成?](./docs/Components.md)  
7. [当用例失败时是用skip还是xfail?](./docs/skip_or_xfail.md)
8. [Fixture执行策略](./docs/fixture_call_order.md)  
9. [Fixture内置对象](./docs/fixture_built_in.md)
10. [Pytest对外暴露的Hooks清单](./docs/Hooks.md)  
11. [Hooks的执行顺序](./docs/Hooks.md#Hooks执行顺序)
12. [HookCaller对象的_wrappers和_nonwrappers属性谁的优先级高?](./docs/_wrappers_nonwrappers_priority.md)
13. [Debug打印pluginmanager的_wrappers和_nonwrappers代码](./docs/debug_print_wrappers_nonwrappers.md)


&nbsp;  
### Pytest源码  
1. [hookspec加载链路图](./docs/pytest_load_hookspec.png)
2. [hooks的注册过程顺序图(强调顺序、动机)](./docs/pytest_register_hooks.png)
3. [hooks的调用链路图](./docs/hooks/pytest_hooks_invocation_chain.png)
4. [fixture的工作流程图](./docs/fixture_workflow.png)


&nbsp;  
### Pluggy
1. [Pluggy是什么?](./docs/WhatIsPluggy.md)  
2. [Pluggy解决了什么问题?](./docs/WhyIsPluggyUseful.md)  
3. [Pluggy由哪些关键组件构成?](./docs/HowDoesItWork.md)  
4. [Pluggy的函数签名和实现](./docs/HookSpecAndImpl.md)  
5. [Pluggy编写一个插件](./docs/pluggy/eggsample/eggsample/host.py#L39)
6. [pluggy._hooks.HookspecMarker](./docs/pluggy/hooks_HookspecMarker.md)  
7. [pluggy._hooks.HookimplMarker](./docs/pluggy/hooks_HookimplMarker.md)  
8. [pluggy._hooks.varnames](./docs/pluggy/hooks_varnames.md)
9. [pluggy._hooks.HookSpec](./docs/pluggy/hooks_HookSpec.md)  
10. [pluggy._hooks.HookImpl](./docs/pluggy/hooks_HookImpl.md)  
11. [pluggy._hooks._HookCaller](./docs/pluggy/hooks_HookCaller.md)  
12. [pluggy._hooks._SubsetHookCaller](./docs/pluggy/hooks_SubsetHookCaller.md)  
13. [pluggy._manager.DistFacade](./docs/pluggy/manager_DistFacade.md)
14. [pluggy._manager.PluginManager](./docs/pluggy/manager_PluginManager.md)  
15. [pluggy._result._Result](./docs/pluggy/result_Result.md)  
16. [pluggy._caller._multicall](./docs/pluggy/caller_multicall.md)  


&nbsp;  
### allure插件源码


&nbsp;  
### xdist插件源码  


&nbsp;  
### 思考和跟进的内容  
1. 如何编写一个像pytest-bdd这样的插件来改变测试行为?  
是否可以将 httprunner 这种模式变成一个插件.  
