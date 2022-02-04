### 可用性
[可用性](http://www.uml.org.cn/softwareprocess/rjgc18.htm) 是衡量使用一种产品来执行指定任务的难易程度的尺度.

### 功能性需求
由参与者(人、另一个系统、计时器、传感器等)发起的一个任务, 该任务完成一件事情, 这就是功能性需求.   

### 可用性需求  
系统界面要很友好, 在每个页面上都有操作提示, 这就是可用性需求.  

### 涉众  
参与者是涉众代表, 例如要建立一个办公自动化系统, 这个系统将为所有的办公室员工归档和查找文件带来利益.  
但是并不需要把所有的办公室员工都找来咨询需求, 一个称之为"文员"的参与者可以代表这批涉众来向系统提出  
如何归档和如何查询的要求, 一次来获得涉众利益.  

### 高内聚  
避免边界外的事物频繁的直接访问边界内的元素.   

### 低耦合  
对象与对象之间的依赖关系(双向依赖、交叉依赖)越紧密表示着耦合越高.  
单向依赖、无依赖通常表示为低耦合.  

### 业务对象  
TODO: 待补充   

### 领域模型  
领域模型描述那些对业务有着重要意义的业务对象.  

### 结构化编程(SP)  
结构化编程, 英文简称: SP; 英文全称: [Structured programming](https://en.wikipedia.org/wiki/Structured_programming).  
结构化编程强调在程序入口处充分利用 `if`、`if else`、`for loop`、`while`、`struct` 等特性完成需求代码的开发.  
> 结构化编程, 适用于卡片编程时代(20世纪60年代).  

### 面向过程编程(OPP)  
面向过程编程, 英文简称: OPP; 英文全称: [Procedural Oriented Programming](https://www.geeksforgeeks.org/differences-between-procedural-and-object-oriented-programming/).  
在`结构化编程`的基础上, 将动作最小化封装成函数, 每个函数表示一个操作步骤,     
每个动作都是一个函数调用, 并且函数和函数之间对数据的承接有严格的要求;  
结构化的数据要么是全局共享的, 要么是通过指针形式传递给函数;  
面向过程编程强调由控制函数来统筹调用所有步骤函数来完成需求代码的开发.
> 面向过程编程, 适用于小规模编程时代(20世纪60、70、80年代).  
> 在20世纪90年代以前盛行的过程式编程, 是非常面向机器的.  
> 开发人员需要对计算机如何工作有相当多的了解, 才能写出好代码.  
> 
> 补充: httprunner 这个框架是面向过程编程的.  


### 面向对象编程(OOP)
面向对象编程, 英文简称: OOP; 英文全称: [Object Oriented Programming](https://www.geeksforgeeks.org/differences-between-procedural-and-object-oriented-programming/)  
面向对象编程是继结构化革命之后的又一次软件开发方式革命, 面向对象的主要思想是基于抽象数据类型的(Abstract Data Type, ADT):   
在结构化编程过程中, 人们发现把某种数据结构和用于操纵它的各种操作以某种模块化方式绑定到一起会非常方便, [参考来源](https://blog.csdn.net/Edward_Wong/article/details/39533245).  
面向对象编程还产生了很多的重要概念: `继承`、`接口`、`多态`、`封装`、`方法`、`依赖`、`组合`、`实例化`、`耦合`、`复用` 等.  
> 面向对象编程, 适用于大规模编程时代(20世纪90年代至今).  
> Python于1991年诞生, 这是一门面向对象语言, 在Python中一切都是对象.  
> wxPython这个三方库于1994年诞生, 这是框架的采取面向对象的编程规范来进行封装.  

### 面向过程与面向对象的区别  
参考这里: [Difference between Procedural Programming and Object Oriented Programming](https://www.geeksforgeeks.org/differences-between-procedural-and-object-oriented-programming/)

|差异|面向过程|面向对象|
|---|---|---|
|代码封装|代码封装在函数中|代码封装在类的方法中|
|设计方法|遵循自顶向下方法|遵循自底向上方法|
|访问控制|-|`private`、`public`、`protect`|
|流程或数据变更|改动大|改动小|
|数据安全|数据都是公开的|类数据默认都是私有的, <br />通过显式声明公开来访问, <br />通过方法代理访问, <br />通过方法代理修改. |
|多态机制|-|支持多态机制|
|侧重点-1|认为函数比数据重要|认为类的数据比类的方法重要|
|侧重点-2|面向操作系统的API来设计和开发|面向现实世界的对象和关系来设计、抽象和开发|