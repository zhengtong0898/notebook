### Pluggy解决了什么问题?  
> There are some established mechanisms for modifying the behavior of other programs/libraries in Python like method overriding (e.g. Jinja2) or monkey patching (e.g. gevent or for writing tests). These strategies become problematic though when several parties want to participate in the modification of the same program. Therefore pluggy does not rely on these mechanisms to enable a more structured approach and avoid unnecessary exposure of state and behaviour. This leads to a more loosely coupled relationship between host and plugins.
> 
> The pluggy approach puts the burden on the designer of the host program to think carefully about which objects are really needed in a hook implementation. This gives plugin creators a clear framework for how to extend the host via a well defined set of functions and objects to work with.

在没有`Pluggy`之前, 一个程序如果想要扩展一个接口, 大体上有两种方式.  
第一种: 面向对象的多态允许对象和对象之间采用继承和方法覆盖的方式完成各自行为的实现.  
第二种: 利用编程语言的特性(例如: monkey_patch、mock、hot patch)做一些方法覆盖.  
这两种方式可以解决很多常见的编程问题, 但总体来说这两种编程方式都属于一体化开发模式.  

当一个程序的目标是将自己打造成一个可扩展的框架时, 插件化的编程模式就浮现出来了.  
框架负责根据软件的整体架构设计出一些接口, 然后所有开发者都能围绕这些接口开发特定的插件.  

`Pluggy`的这种插件化编程模式, 将困难留给了框架设计者, 让其必须要想清楚哪些接口适合用来做`hook`.  
这种方式让插件开发者可以清晰的感受到哪些接口可以扩展、哪些接口可以覆盖.  




  
