### _wrappers 和 _nonwrappers 谁的优先级高?

结论是: _wrappers 优先级高.

&nbsp;  
拿 pytest_collection 这个 hook 来举例.
```shell


# _nonwrappers
[
<HookImpl plugin_name='main', plugin=<module '_pytest.main' from '_pytest/main.py'>>, 
<HookImpl plugin_name='assertion', plugin=<module '_pytest.assertion' from '_pytest/assertion/__init__.py'>>, 
<HookImpl plugin_name='pytest-hookorder/conftest.py', plugin=<module 'conftest' from 'pytest-hookorder/conftest.py'>>, 
<HookImpl plugin_name='terminalreporter', plugin=<_pytest.terminal.TerminalReporter object at 0x7f6b8249c1f0>>
]


# _wrappers
[
<HookImpl plugin_name='pytestconfig', plugin=<_pytest.config.Config object at 0x7f6b837a2820>>, 
<HookImpl plugin_name='warnings', plugin=<module '_pytest.warnings' from '_pytest/warnings.py'>>, 
<HookImpl plugin_name='logging-plugin', plugin=<_pytest.logging.LoggingPlugin object at 0x7f6b8249c250>>
]


# 最终汇聚成的hook_impls是
[
<HookImpl plugin_name='main', plugin=<module '_pytest.main' from '_pytest/main.py'>>, 
<HookImpl plugin_name='assertion', plugin=<module '_pytest.assertion' from '_pytest/assertion/__init__.py'>>, 
<HookImpl plugin_name='pytest-hookorder/conftest.py', plugin=<module 'conftest' from 'pytest-hookorder/conftest.py'>>, 
<HookImpl plugin_name='terminalreporter', plugin=<_pytest.terminal.TerminalReporter object at 0x7f6b8249c1f0>>, 
<HookImpl plugin_name='pytestconfig', plugin=<_pytest.config.Config object at 0x7f6b837a2820>>, 
<HookImpl plugin_name='warnings', plugin=<module '_pytest.warnings' from '_pytest/warnings.py'>>, 
<HookImpl plugin_name='logging-plugin', plugin=<_pytest.logging.LoggingPlugin object at 0x7f6b8249c250>>
]


# 由于pluggy采取的是LIFO策略, 所以真正的执行顺序是
[
<HookImpl plugin_name='logging-plugin', plugin=<_pytest.logging.LoggingPlugin object at 0x7f6b8249c250>>
<HookImpl plugin_name='warnings', plugin=<module '_pytest.warnings' from '_pytest/warnings.py'>>, 
<HookImpl plugin_name='pytestconfig', plugin=<_pytest.config.Config object at 0x7f6b837a2820>>, 
<HookImpl plugin_name='terminalreporter', plugin=<_pytest.terminal.TerminalReporter object at 0x7f6b8249c1f0>>, 
<HookImpl plugin_name='pytest-hookorder/conftest.py', plugin=<module 'conftest' from 'pytest-hookorder/conftest.py'>>, 
<HookImpl plugin_name='assertion', plugin=<module '_pytest.assertion' from '_pytest/assertion/__init__.py'>>, 
<HookImpl plugin_name='main', plugin=<module '_pytest.main' from '_pytest/main.py'>>, 
]
```