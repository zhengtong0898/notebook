### pytest的缓存机制
`Pytest`为了能记录上一次全量测试用例的执行情况, 创建了一套缓存机制. 当执行完一次全量用例后,   
`Pytest`会在项目目录下创建一个`.pytest_cache`文件夹, 并以文件形式存放着最后一次用例执行结果数据.  

`.pytest_cache`目录结构  
```shell
.pytest_cache/
├── CACHEDIR.TAG                # 这是一个固定的模板文件
├── README.md                   # 这是一个固定的模板文件
└── v                           # 这是一个一级目录
    └── cache                   # 这是一个二级目录
    │   ├── lastfailed          # 这是一个文件: 以字典格式存放最后一次执行失败的用例集合 
    │   ├── nodeids             # 这是一个文件: 以列表格式存放最后一次执行的所有用例集合
    │   └── stepwise            # 这是一个文件: 以字符串格式存放最后一次执行失败的用例
    └── userid                  # 这是一个文件: 自定义的缓存数据: 文件名为key, 文件内容为value
    └── content                 # 这是一个文件: 自定义的缓存数据: 文件名为key, 文件内容为value
```

我可以通过参数`--cache-show`的方式快速列出缓存数据.  [测试用例](./cmdlines/cache-show/main.py)
```shell
$ pytest --cache-show
===================================================== test session starts ==========================================
platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-0.13.1
rootdir: notebook/tester/pytest/docs/fixtures
plugins: xdist-2.5.0, allure-pytest-2.9.45, loadinitialconftests-0.0.0, cmdlineparse-0.0.0, forked-1.4.0
cachedir: notebook/tester/pytest/docs/fixtures/.pytest_cache
---------------------------------------------------- cache values for '*' ------------------------------------------
cache/lastfailed contains:
  {'test_config_cache.py::test_config_cache_a': True,
   'test_fixture_monkey_patch.py::test_env_reading_2': True,
   'test_monkey_patch.py::test_env_reading_2': True}
cache/nodeids contains:
  ['test_config_cache.py::test_config_cache_a',
   'test_config_cache.py::test_config_cache_b',
   'test_fixture_caplog.py::test_caplog',
   'test_fixture_caplog.py::test_foo',
   'test_fixture_capsys.py::test_capsys',
   'test_fixture_capsys.py::test_capsys_rewrite',
   'test_fixture_capsys.py::test_capsys_stderr',
   'test_fixture_monkey_patch.py::test_env_reading_1',
   'test_fixture_monkey_patch.py::test_env_reading_2',
   'test_fixture_order_with_nest.py::test_order',
   'test_fixture_request.py::test_request',
   'test_fixture_tmp_path.py::test_create_file',
   'test_monkey_patch.py::test_env_reading_1',
   'test_monkey_patch.py::test_env_reading_2',
   'test_monkey_patch.py::test_envreading']
cache/stepwise contains:
  []
userid:
  120
content:
  "口头禅是无聊"

==================================================== no tests ran in 0.01s =========================================
```

也可以通过`linux`命令行`cat`逐一查看文件内容来了解最后一次全量测试用例的执行情况.
```shell
// 最后一次执行失败的用例集合 
$ cat .pytest_cache/v/cache/lastfailed
{
  "test_config_cache.py::test_config_cache_a": true,
  "test_monkey_patch.py::test_env_reading_2": true,
  "test_fixture_monkey_patch.py::test_env_reading_2": true
}


// 最后一次执行的全量用例集合 
$ cat .pytest_cache/v/cache/nodeids
[
  "test_config_cache.py::test_config_cache_a",
  "test_config_cache.py::test_config_cache_b",
  "test_fixture_caplog.py::test_caplog",
  "test_fixture_caplog.py::test_foo",
  "test_fixture_capsys.py::test_capsys",
  "test_fixture_capsys.py::test_capsys_rewrite",
  "test_fixture_capsys.py::test_capsys_stderr",
  "test_fixture_monkey_patch.py::test_env_reading_1",
  "test_fixture_monkey_patch.py::test_env_reading_2",
  "test_fixture_order_with_nest.py::test_order",
  "test_fixture_request.py::test_request",
  "test_fixture_tmp_path.py::test_create_file",
  "test_monkey_patch.py::test_env_reading_1",
  "test_monkey_patch.py::test_env_reading_2",
  "test_monkey_patch.py::test_envreading"
]

```


&nbsp;  
### 缓存机制有什么用?
缓存机制能让我不费任何力气就可以在全局层面具备仅重跑所有的失败用例.  
缓存机制甚至能让按增量策略的方式来修复测试用例和重跑测试用例.  
缓存机制提供了非常丰富的重跑策略, 完整的策略清单[点击这里](./re-run_failed_tests.md).