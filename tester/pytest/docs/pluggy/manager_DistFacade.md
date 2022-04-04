### DistFacade 类对象的介绍  

这是一个`插件元数据`代理对象, 利用`__dir__`和`__getattr__`代理访问`self._dist`对象.  
注: `importlib_metadata.Distribution` 对象存储的是单个已安装的`setuptools`包, 可通过`pip list`查询出来的包.  

```python3

class DistFacade:
    """Emulate a pkg_resources Distribution"""

    def __init__(self, dist: importlib_metadata.Distribution) -> None:
        self._dist = dist

    @property
    def project_name(self) -> str:
        name: str = self.metadata["name"]
        return name

    def __getattr__(self, attr: str, default=None):
        return getattr(self._dist, attr, default)

    def __dir__(self) -> List[str]:
        return sorted(dir(self._dist) + ["_dist", "project_name"])

```