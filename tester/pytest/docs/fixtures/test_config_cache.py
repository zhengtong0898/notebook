import pytest

"""
The config.cache object allows other plugins and fixtures to store and retrieve values across test runs.   
config.cache 可以跨 测试用例、跨运行会话(Session) 存储和访问自定义的缓存数据.  

除非显式的生命--cache-clear, 否则缓存将会持久化留存在当前目录的 ./pytest_cache/v/cache 路径.

./.pytest_cache/
├── CACHEDIR.TAG
├── README.md
└── v
    ├── cache
    │    ├── lastfailed                     # pytest内置缓存文件(数据)
    │    ├── nodeids                        # pytest内置缓存文件(数据)
    │    └── stepwise                       # pytest内置缓存文件(数据)
    ├── test_config_cache_a::actual         # 自定义的缓存文件
    └── test_config_cache_a::expect         # 自定义的缓存文件


参考:
https://docs.pytest.org/en/6.2.x/reference.html#config-cache
https://docs.pytest.org/en/6.2.x/cache.html
"""


def test_config_cache_a(request):                                            # 失败用例
    request.config.cache.set("test_config_cache_a::actual", 120)
    request.config.cache.set("test_config_cache_a::expect", 120)
    assert 1 == 2


def test_config_cache_b(request):                                            # 成功用例
    expect = request.config.cache.get("test_config_cache_a::expect", None)
    assert expect == 120
    assert 1 == 1


"""
执行结果

============================================ test session starts ============================================
platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-1.0.0
------------------------------------------- cache values for '*' --------------------------------------------
cache/lastfailed contains:
  {'test_config_cache.py::test_config_cache_a': True}                        # 失败用例被缓存了
cache/nodeids contains:
  ['test_config_cache.py::test_config_cache_a',
   'test_config_cache.py::test_config_cache_b']
cache/stepwise contains:
  []
test_config_cache_a::actual contains:
  120
test_config_cache_a::expect contains:
  120

=========================================== no tests ran in 0.01s ===========================================
"""