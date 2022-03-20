
### Pluggy是什么?

> pluggy is the crystallized core of plugin management and hook calling for pytest. It enables 500+ plugins to extend and customize pytest’s default behaviour. Even pytest itself is composed as a set of pluggy plugins which are invoked in sequence according to a well defined set of protocols.
> 
> It gives users the ability to extend or modify the behaviour of a host program by installing a plugin for that program. The plugin code will run as part of normal program execution, changing or enhancing certain aspects of it.
> 
> In essence, pluggy enables function hooking so you can build “pluggable” systems.

`Pluggy`是一个插件管理系统, 它提供了插件注册、插件运行、钩子定义、钩子实现等等的一系列接口规范和准则.    
`Pytest`本身也是由一系列`内部插件`组成, `Pytest`的这些`内部插件`根据一组明确定义的协议按顺序调用.  
`Pluggy`提供的这一套机制, 让用户可以根据主库(例如: `pytest`)的钩子定义, 来开发一个特定场景的插件.  

**pytest**、**tox**、**devpi** 这些框架或工具, 都是围绕`Pluggy`的运作方式开发出来的.  

### 参考
[官方文档](https://pluggy.readthedocs.io/en/latest/)