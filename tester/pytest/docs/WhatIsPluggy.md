
### Pluggy是什么?
`Pluggy`是一个插件注册、钩子定义、钩子实现、插件运行的底座, 统称为插件管理系统.  
`Pytest`本身也是由一系列`内部插件`组成, `Pytest`的这些`内部插件`根据一组明确定义的协议按顺序调用.  

**pytest**、**tox**、**devpi** 这些框架或工具, 都是围绕`Pluggy`的运作方式开发出来的.  

### 参考
[官方文档](https://pluggy.readthedocs.io/en/latest/)