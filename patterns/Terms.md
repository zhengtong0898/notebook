### 可用性
[可用性](http://www.uml.org.cn/softwareprocess/rjgc18.htm) 是衡量使用一种产品来执行指定任务的难易程度的尺度.

### 功能性需求
由参与者(人、另一个系统、计时器、传感器等)发起的一个任务, 该任务完成一件事情, 这就是功能性需求, page-45.   

### 可用性需求  
系统界面要很友好, 在每个页面上都有操作提示, 这就是可用性需求, page-81.  

### 涉众(Stakeholder)  
参与者是涉众代表, 例如要建立一个办公自动化系统, 这个系统将为所有的办公室员工归档和查找文件带来利益.  
但是并不需要把所有的办公室员工都找来咨询需求, 一个称之为"文员"的参与者可以代表这批涉众来向系统提出  
如何归档和如何查询的要求, 一次来获得涉众利益, page-49.  

### 高内聚  
避免边界外的事物频繁的直接访问边界内的元素, page-77.   

### 低耦合  
对象与对象之间的依赖关系(双向依赖、交叉依赖)越紧密表示着耦合越高.  
单向依赖、无依赖通常表示为低耦合, page-77.  

### 对象(Object)
对象对应于编程语言中的类, 而我们都知道类是由多个属性(数据)和多个方法构成的, [参考资料](https://www.techtarget.com/searchapparchitecture/definition/object).  

### 对象实例
场景中的对象只是该对象的一个侧面, 我们称之为对象实例, page-37.  
通过一个场景, 我们仅能得到该对象的一个侧面信息.  
要深入了解对象, 我们经常需要分析很多个与该对象强相关的场景.

### 业务对象(Business Object)  
业务对象对应于现实世界中的人、地点或事物.  
业务对象的定义侧重点在对象的属性、方法以及业务对象间的关系, page-16、[参考资料](https://flylib.com/books/en/2.699.1.19/1/).  

### 业务实体
**现实:** 各个环节的需要前置和填写信息的工单: 申请单、勘察单、收费清单、同意签字单等等.  
**系统:** 系统用户、收费账号、结算账号、抄表台账、监察档案.  
这些都是各业务环节可以看得到或摸得着的实体.  

### 用例(Use Case)
用例对应于日常工作的测试用例, page-52.
> **用例**  
> 你想做一顿饭吃, 你需要完成煮饭和炒菜两件事情, 这两件事情就是两个用例.  
> 
> **用例的实例**  
> 煮饭这件事情是可以有不同做法的, 你可以用电饭煲煮饭,   
> 也可以用蒸笼蒸饭, 这是两个不同的场景, 也就是两个用例的实例.    
> 
> **用例在不同条件下的不同处理场景**  
> 同样是用电饭煲煮饭, 如果是粗米, 你需要先淘米, 然后再下锅.  
> 如果是精米, 则可以省略淘米步骤直接下锅.  
> 这是用例在不同条件下的不同处理场景.  
> 
> **结论**  
> 根据上面三个描述片段, 有效的用例时2个(就是那两个用例的实例).   
> 然而在实际工作中, 通常会产出4个有效的用例:   
> 1). 用电饭煲煮饭, 粗米, 算一个用例.  
> 2). 用电饭煲煮饭, 精米, 算一个用例.  
> 3). 用蒸笼煮饭, 算一个用例.  
> 4). 炒菜, 算一个用例.
 
### 业务用例(Business Use Case)
业务用例(Business Use Case) == 用例(Use Case),  
所以后续业务用力统统会被成为用例.  
[参考资料-1](https://stackoverflow.com/a/3294069) 、
[参考资料-2](https://sceweb.uhcl.edu/helm/RationalUnifiedProcess/process/modguide/md_buc.htm) 、
[参考资料-3](https://sceweb.uhcl.edu/helm/RationalUnifiedProcess/process/modguide/md_uc.htm)    

> 获取业务用例是什么意思?  
> 当我们手握需求文档或与客户沟通完需求后, 需要从这些信息中提炼出业务用例的这个过程, 叫做获取业务用例.  
> 业务用例通常包含了: 业务主角 和 业务目标;   
> 说人话就是系统需要提供具体服务来满足客户的具体需求.  

### 用例实例(Use Case Instance)  
用例实例 == 业务用例实现(Business use case realization),  
就像对象实例与之对象, 一个用例实例也只是用例的一个侧面.  
`Pytest`的参数化就是一组用例实例, 用于验证用例的完整性.    
page-68, [参考资料-1](https://sceweb.uhcl.edu/helm/RationalUnifiedProcess/process/modguide/md_uc.htm)

### 概念用例
TODO: 资料不充分, 表达不清楚, 后续需要精简或重写这里.  
概念用例用来表示核心业务逻辑, 这些核心业务逻辑揭示了业务模式, 成为业务框架的重要知道, page-69.

### 系统用例  
业务用例: 以参与者的目标来描述所有操作步骤, 侧重点是参与者输入什么, 系统输出什么.   
系统用例: 以参与者和系统的角色来描述所有操作步骤, 侧重点是参与者在不同的角色下能做什么, 系统分别输出什么.  

### 用例实现
一个用例实现代表了用例的一种实现方式, page-70.  
用例实现描述的是用例实现的过程, 先干嘛, 再干嘛, 最后干嘛.  

### 业务用例与业务用例实现的区别  
业务用例: 表达了客户的单个(路径的)实际业务, 每一个场景只针对一种业务执行方式, 应当清晰而明了.    
业务用例实现: 一个业务用例的一个或多个实现方式, 如果某个场景又多个实现, 则可以用业务用例实现来画图, page-254.    
> 建立计算机的目的就是让用户通过人与计算机交互来完成业务,   
> 因此, 在 '业务用例实现' 时, 应当着重描述如何通过人机交互来完成业务.  
> 
> 如果说业务用例场景是跟客户就业务打成共识,   
> 那么业务用例实现场景就是跟客户就如何操作打成共识.  
> 
> 业务用例实现场景也是制作系统原型的依据,  
> 业务用例实现场景通常都要比业务用例场景细致很多, 因为它包含了实现的细节.  
> 业务用例实现场景的建模通常使用活动图来完成、也可以使用时序图来完成.  
> 
> 业务用例、业务用例场景、业务用例实现场景它们之间的关系是:  
> 一个业务用例可以有多个业务用例场景. 
> 一个业务用例场景由多个步骤(活动)构成, 这些步骤(活动)可能会存在条件分支.  
> 一个活动分支对应一个完整的流程图来描述业务模型, 这个流程图可以是: 活动图、时序图来完成.  


### 领域模型  
领域模型描述那些对业务有着重要意义的业务对象, page-112.  

### 结构化编程(SP)  
结构化编程, 英文简称: SP; 英文全称: [Structured programming](https://en.wikipedia.org/wiki/Structured_programming).  
结构化编程强调在程序入口处充分利用 `if`、`if else`、`for loop`、`while`、`struct` 等特性完成需求代码的开发, page-1.  
> 结构化编程, 适用于卡片编程时代(20世纪60年代).  

### 面向过程编程(OPP)  
面向过程编程, 英文简称: OPP; 英文全称: [Procedural Oriented Programming](https://www.geeksforgeeks.org/differences-between-procedural-and-object-oriented-programming/).  
在`结构化编程`的基础上, 将动作最小化封装成函数, 每个函数表示一个操作步骤,     
每个动作都是一个函数调用, 并且函数和函数之间对数据的承接有严格的要求;  
结构化的数据要么是全局共享的, 要么是通过指针形式传递给函数;  
面向过程编程强调由控制函数来统筹调用所有步骤函数来完成需求代码的开发, page-3.  
> 面向过程编程, 适用于小规模编程时代(20世纪60、70、80年代).  
> 在20世纪90年代以前盛行的过程式编程, 是非常面向机器的.  
> 开发人员需要对计算机如何工作有相当多的了解, 才能写出好代码.  
> 
> 补充: httprunner 这个框架是面向过程编程的.  


### 面向对象编程(OOP)
面向对象编程, 英文简称: OOP; 英文全称: [Object Oriented Programming](https://www.geeksforgeeks.org/differences-between-procedural-and-object-oriented-programming/)  
面向对象编程是继结构化革命之后的又一次软件开发方式革命, 面向对象的主要思想是基于抽象数据类型的(Abstract Data Type, ADT):   
在结构化编程过程中, 人们发现把某种数据结构和用于操纵它的各种操作以某种模块化方式绑定到一起会非常方便, [参考来源](https://blog.csdn.net/Edward_Wong/article/details/39533245).  
面向对象编程还产生了很多的重要概念: `继承`、`接口`、`多态`、`封装`、`方法`、`依赖`、`组合`、`实例化`、`耦合`、`复用` 等, page-7.    
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

### 统一过程(RUP)
统一过程, 英文简称: RUP; 英文全称: Rational Unified Process.  
RUP集成了面向对象方法、UML语言、核心工作流、工作模板和过程指导等许多知识.  
RUP要求在写代码之前, 需要先将需求分析清楚并转换成设计文档(含: 流程图、时序图、状态图、类图等).    
RUP适用于开发稳定的架构, 它通过不断的演进来逐步推进软件产品, 这一特点使得它特别适合长期战略的软件产品.  
RUP适合那些想长期立足于做某个行业, 希望做精做深, 做行业整体解决方案的企业(组织), page-22.  

### 极限编程(XP)  
极限编程, 英文简称: XP; 英文全称: Extreme Programming.
XP的核心思想是利用单元测试、系统测试体系来做每日构建, 尽早的暴露问题、发现错误,   
降低问题随着时间的推移而不断增加的复杂度, 从而达到节约成本的效果.  
XP强调将一个大的任务拆解成可以在较短周期解决的一个个子任务,   
通过一个个短小的迭代周期, 可以获得一个个阶段性的进展, page-26.  

### 统一过程与极限编程的区别  
如果用XP方法来开发F-35战斗机将会是一个什么情形, 没有人清楚地知道将来飞机的整体是什么样,   
好不容易设计出机翼来, 另一个小组说我们决定改变一下气动外形, 你们再重构一下把;   
没有人知道最后飞机的性能怎么样, 反正先造一架出来, 要是摔了找找原因, 改进改进,   
重构一下, 在造一架, 再摔了, 没关系, 咱们拥抱变化, 再造就是了...   
显然对这种大型产品来说XP方法是不可接受的, 而RUP的稳步推进的方法正好适合这种场景.  

如果你是一个杂货店的老板, 刚开业不知道什么样的商品受欢迎, 没关系, 先各进一小批货,   
卖上一段时间, 受欢迎的货品多进, 不受欢迎的不进, 随时向顾客做一些调查,  
顾客喜欢什么就进什么, 不断改进, 最后一定会顾客盈门的, XP方法就比较适合这种场景.

如果杂货店场景采用RUP方法, 先做商业分析、客户关系分析、消费曲线分析,   
还没开业呢, 估计就破产了, 或者好不容易做出了一个商业策略, 客户兴趣已经改变了.    

上面介绍了它们的差异, 但是实际工作中我发现它们是紧密融合的,   
在做底层框架开发的时候采用RUP方法, 而在做一些具体功能的时候可以采用XP方法.   

> **最佳实践**  
> 对于软件产品来说, 最佳实践来自两个方面: 一方面是技术类的, 如设计模式;   
> 另一方面是过程类的, 如需求方法、分析方法、设计方法等.  
> RUP继承了很多过程类的最佳实践, 这些最佳实践中包括用例驱动、架构导向、构件化等.  
> 学习RUP将了解到软件的本质, 对提升软件"智商"是非常有好处的.  


### 抽象(abstract)  
从众多具体事物中, 抽取共同的属性, 舍弃个别的属性, 这个动作被称为抽象.  
从编程的角度来看, 抽象对应的就是公共接口(`Interface`).  

**抽象角度**  
请在30秒内尽可能多的说出筷子、勺子和盘子的相同点和不同点.  

- 从用途的角度去抽象   
  它们的相同点是三者都是餐具, 不同点是筷子是用来夹的, 勺子是用来舀的, 盘子是用来盛的.   
  > 举例:  
  > 当从用途的角度去抽象时, 在脑子里为这三个事物建立起了一个人用餐的业务逻辑模型,   
  > 并且这三者在这个业务逻辑模型中表现出了各自的职责和特别的属性.  


- 从使用的角度去抽象  
  它们的相同点是都需要用手去拿, 不同的是手的动作不同.


- 从字面的角度去抽象  
  它们的相同点是都带了一个"子"字.  



所以从不同的角度抽象可以得出不同的结果, 当我们试图为现实世界建模的时候, 首先要决定的是抽象角度,   
即: 建立这个模型的目的是什么, 一旦抽象角度确定, 剩下的事情就变得顺利成章, 而不再是杂乱无章.    

当我们试图去分析需求、面对大量需求资料时, 是否有时候感觉到无从下手?   
当我们试图去做一个设计时, 是否有时候感觉到力不从心?  
这个时候与其说是分析经验不足或是设计能力不够, 不如说是你还没有找到明确的抽象角度.  
面向对象与面向过程不同的地方是, 面向过程希望你通盘考虑, 这时问题变得复杂化;  
而面对象希望你把事务通过抽象角度分解成小块, 问题就变得简单化.  
正如上面的小测试, 在没有明确抽象角度之前, 大部分面试者都会很慌张,   
不明白面试官为什么要问这样一个问题, 不知道从哪里回答, 也不知道回答得是否准确.    
如果加一个条件, 编程请在30秒内说出在使用上: 筷子、勺子、盘子有什么相同点和不同点,  
这个问题就会变得很容易回答了.  

**抽象方法**  
抽象有两种方法, 一种是自顶向下, 另一种是自底向上.   

- 自顶向下  
  自顶向下的方法适用于人们从头开始认识一个事物,   
  例如介绍汽车的工作原理时, 从发动机、传动装置、变速器等较高层次的抽象概念来讲就比较容易明白.  
  如果降一个层次, 从发动机原理讲起, 一大部分听众就会开始迷惑.  
  再降一个层次, 从热力学原理和力学原理讲起, 那就更没人能搞懂汽车是怎么工作的了.   


- 自底向上  
  自顶向下的方法适用于在实践中改进和提高认识,   
  例如在实践中发现了发动机的问题, 因而改进发动机结构, 甚至采用新的发动机原理, 最终能够提升汽车的质量.  

在软件开发过程中, 主题上应当采用**自顶向下**的方法, 用少量的概念覆盖系统需求, 再逐步降低抽象层次, 直到代码编写.  
同时应当辅以自底向上的方法, 通过总结在较低抽象层次的实践经验来改进较高层次的概念以提升软件质量.  



### 建模

建立模型的关键就是弄明白有什么人, 什么人做什么事, 什么事产生什么物, 中间有什么规则,  
再把人、事、物之间的关系定义出来, 一个模型也就基本成型了.  

> **方法论:**  
> 1. 将`文字描述`转换成`业务模型`: 抽象出人、事、物、规则.
> 2. 将`业务模型`转换成`概念模型`: 抽象出(对象的)边界、(对象的)实体、(业务的流向)控制.
> 3. 将`概念模型`转换成`设计模型`: 抽象出(边界)接口、(实体)数据对象、(控制)算法.    

**业务模型**  
TODO: 没有在讲人话.  
需求方(`actor`)是业务信息的第一驱动者(**人**), 即: 整个需求场景开始的地方.  
用例(`use case`)是描述驱动者的目标(**事**), 即: 想要做什么并且获得什么效果.  
场景(`scenario`)是描述场景的过程(**规则**), 即: 这件事是怎么做的, 依据什么规则.  
对象(`object`)是描述场景流转过程需要哪些对象(**物**), 即: 达成这些业务目标的过程中涉及到的事务.

**概念模型**  
TODO: 没有在讲人话.  
计算机的代码可以通过概念模型追溯到原始需求, 概念模型规定了一种高层次的抽象,   
这种抽象是一种指导, 也是一种约束, 实际编码过程中非常容易遵循这种指导和约束来完成代码的设计和落地工作.  
边界类(`boundary`): 对应于现实世界中的"事"(决定了外面能对里面做什么).    
实体类(`entity`): 对应于现实世界中的"物"(描述了物的属性、维度、状态、上下文等).  
控制类(`contrl`): 对应于现实世界中的"规则"(控制边界类和实体类的交互).  
只要有人、事、物和规则(定于), 就能构成一个有意义的结果, 无非是是否合理而已.  

**设计模型**  
TODO: 没有在讲人话.  
概念模型使我们获得了软件的蓝图, 获得了建设软件所需要的所有组成内容以及所有必要细节.  
这就类似于我们已经在图纸上绘制出了一辆汽车所有的零部件, 并且绘制出如何组装这些零部件的步骤.  
设计模型的工作就是建造零部件, 组装汽车的过程.  
设计模型可以将边界类转化为`接口`类.  
设计模型可以将实体类转化为`pydantic`数据对象类.  
设计模型可以将控制类转化为`算法`函数, 业务流程的逻辑和算法都在这里完成.  

### 视图
[参考资料-1](https://plantuml.com/zh/) 、
[参考资料-2](https://zhuanlan.zhihu.com/p/375129998)  
静态视图: 用例图、类图、对象图、包图(组件图)、部署图  
动态视图: 时序图(顺序图)、活动图、状态图  
面向过程的视图: [数据流(DFD)图](https://zhuanlan.zhihu.com/p/231863024)

- [用例图](https://www.zhihu.com/question/407047121/answer/1432849782)  
  用例图是编写需求说明时经常用到的需求表达方式,  
  用于向开发、测试同事说明需求中用户与系统功能单元之间的关系.  
  > **基础元素:** 参与者、用例.  
  > **基础关系:** 关联、继承(基础用例/父用例).  

- [类图](https://zhuanlan.zhihu.com/p/267298708)  
  类图中表达的类与现实世界有着明显的对应关系,   
  类和类之间的关系也与现实世界中事物的关系有着明显的对应关系, page-102, [参考资料-1](https://plantuml.com/zh/class-diagram) .      
  > **类是离散的:** 类和场景之间的关系是独立的, 因为一个类可以对应处理多个场景.  
  > **类的关系:** 类与类之间的关系是多样的: 关联、依赖、继承、聚合、组合 等.  

- [对象图](https://zhuanlan.zhihu.com/p/372860982)  
  对象图展示的是类的实例, 一个对象图是类图的一个实例.  
  > **基本元素:** object、relationship   
  > **对象关系:** Extension、Aggregation、Composition  
  > [参考这里](https://plantuml.com/zh/object-diagram)  

- [包图](https://zhuanlan.zhihu.com/p/381028072)  
  包图通常用于描述系统的逻辑架构: 层、子系统、包;  
  > **基本元素:** 类、接口、组件、节点、协作、用例、图以及其他包. 
  > **包的关系:** 依赖、继承、实现.  
  > [参考这里](https://plantuml.com/zh/component-diagram)  

- [部署图](https://zhuanlan.zhihu.com/p/381027189)  
  部署图描述的是系统运行时的结构, 展示了系统的硬件配置、硬件部署, 以及其软件如何部署到网络结构中.  


- [时序图](https://zhuanlan.zhihu.com/p/360656613)  
  时序图描述对象之间的传递消息的时间顺序(包括发送消息、接收消息、处理消息、返回消息等).  
  > **基本元素:** 对象、生命线、消息(同步消息、异步消息、返回消息、自关联消息).  

- [活动图](https://zhuanlan.zhihu.com/p/375129998)
  活动图描述活动的顺序, 展现从一个活动到另一个活动的控制流, 它本质上是一种流程图.  
  > **基本元素:** 起点、终点、活动名称、判断条件、分支与合并、接收信号、发送信号、泳道(其实和流程图很相像).  

- [状态图](https://zhuanlan.zhihu.com/p/408303320)  
  状态机图描述一个对象在其生命周期中的各种状态以及状态的转换.  
  > **状态机:** 状态、转换、事件、动作、活动.  

### 视角  
指的是不同工作职责的人会从不同的角度来理解某个需求或者某个功能,   
**例如:** 同一个业务模块, 经理更关系整体业务流程, 业务员更关心表单填写;    
**作用:** 为不同工作职责的人展示他们所关心的那部分视角.  
从信息的展示角度来说, 恰当的视角可以让观察者更容易抓住信息的本质.  
从观察者的角度来说, 观察者只会关心信息中他感兴趣的那一部分视角, 其他视角的信息对他是没有多少用处的.  
因此在展示信息时选择适当的视角并展示给适当的观察者是十分重要的.

### 描述事物的方法
在描述一个事物的时候, 我们可以从以下三个观点出发(page-61):  
1. 这个事物是什么?
2. 这个事物能做什么?
3. 人们能够用这个事物做什么?  

描述一辆自行车的时候, 我们通常这样说明:  

第一, 自行车是一种交通工具, 它由传动系统、刹车系统等部分组成.  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;描述结构性观点, 即事物的客观存在.  

第二, 自行车可以骑行, 可以载物.   
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;描述功能性观点, 说明事物可利用的价值.  

第三, 人们可以用双脚蹬动踏板而向前行进, 可以用手捏合刹车使自行车停下来.  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;描述使用者观点, 说明事物对于使用者的意义, 以及使用者怎么使用它, 得到什么样的利益.  

对于我们早已熟知的事物来说, 我们可以上述三个方面的观点来描述, 例如自行车这种天天可以看到的东西.  
如果我们要描述的事物是我们并不熟悉的呢?   
对于一个陌生的事物, 我们不大可能先从结构的角度去解释它, 顶多可以通过观察假定出这个事物能做什么.  
如果这个事物是现在还不存在的呢?  
例如正在研制一种全新药品(不存在的事物), 我们既不能从结构上去解释它, 也不能确定它到底能做什么,   
最好的方式是从使用者的观点出发, 描述使用者能用它做什么, 能获得什么.  

> 补充例子:  
> Viagra本来是辉瑞公司研制生产的一种治疗心绞痛的药物, 可现在Viagra变成了人尽皆知的威哥,  
> 人们都用它来治疗ED(勃起功能障碍症), 大大出乎研究人员的初衷.  
> 
> 所以对于创造一种还不存在的事物, 最好的方式是从使用者的观点出发,   
> 描述使用者能用它做什么, 能获得什么.  

软件恰恰就是一种还不存在的事物.   
对于正准备开发的软件, 我们不能从结构观点去描述它, 也不能从功能观点去描述它.  
最好的方法就是从使用者的观点去描述它,   
至于功能性观点和结构性观点, 可以通过使用者观点推导出来.  

### 边界  
面向对象里, 任何一个对象都有一个边界, 外界只能通过这个边界来认识对象, 与对象打交道, 而对象内部则是一个进去.  
我们把边界放大了看, 这个世界上任何一种东西我们都不可能知道它本质上是什么, 而只能通过它的行为、外观、性质来  
描述它是一个什么东西, 行为也好, 外观也罢, 这就是这个东西的一个边界, 我们就是通过边界来认识事物的.  

> 比如说我们观察并描述一幢建筑物, 如果我们的位置在楼的正前方, 能够观察到的东西是大门、招牌、楼层数这些东西;  
> 如果我们的位置是在大厅里, 能够观察到的东西是吊灯、沙发、柱子这些东西;   
> 如果我们的位置是在楼顶上, 能观察到的东西是围栏、烟道、中央空调水冷器这些东西了.  
> 
> 虽然这些东西完全不一样, 但是我们一直都在描述同一幢建筑. 为了更接近真相,   
> 我们能够做的就是不断变换边界, 从更多的侧面去描述同一个信息, 以求最大程度地符合真实的需求.  

在实际工作中应当学会灵活地使用边界, 用边界来决定抽象层次和视角, 进而排除边界外大量的杂音来降低复杂度.  


### 发现参与者

场景1:  
小王到银行去开户, 向大厅经理询问了办理手续, 填写了表单并交给柜台职员, 最终拿到了银行存折.

系统之外: 小王(参与者);  
系统之内: 银行场所、大厅经理、柜台职员、保安、电脑、桌子、椅子等等,  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
由于大厅经理和柜台职员"参与"了场景中的业务, 它们被称为业务工人(**business worker**).  

&nbsp;  
场景2:  
每天自动统计网页访问量, 生成统计报表, 并发送至管理员信箱.  

系统之外: 定时任务(参与者);  
系统之内: 自动统计网页访问量的程序、自动生成统计报表的程序、自动发送邮件给管理员的程序.  

> 这两个案例表明, 参与者可以是人, 也可以是物,   
> 其中物可以是另外一个系统、一个定时器(定时任务)或一个传感器等等.  

场景3:  
机票购买者通过登录到网站购买机票.  

系统之外: 机票购买者(参与者).  
系统之内: 订票网站.  

&nbsp;  
场景4:  
机票购买者通过呼叫中心, 由人工坐席操作订票系统来购买机票.  

系统之外: 机票购买者(不是参与者)、人工坐席(参与者).  
系统之内: 订票系统.   

&nbsp;  
场景5:  
机票购买者通过呼叫中心的自动语音来预定机票.   

系统之外: 机票购买者(不是参与者)、语音呼叫系统(参与者).  
系统之内: 订票系统.   

&nbsp;  
场景6:  
如果电话自动语音是机票预定系统的一个子系统、电话人工坐席也是机票预定系统的一个子系统.  
机票购买者通过呼叫中心的自动语音来预定机票.   
机票购买者通过呼叫中心的人工坐席来预定机票.  

系统之外: 机票购买者(参与者).   
系统之内: 订票系统、电话自动语音子系统、电话人工坐席子系统.  


### 关联关系(Association)
关联关系是一种静态关系, 通常与运行时无关.  
关联关系一般不强调关联的方向, 我们默认A和B都是相互"知道"对方的存在, page-86, [箭头参考](./UMLIcons.md#关联关系(Association)) .     
关联关系分为下面三种:    
**一对一:** 乘车人和车票之间的一对一是符合"规则"的关系; 公民和身份证之间的一对一是符合"法律"的关系.    
**一对多:** 一个班级和多个学生之间是一对多的关系;  
**多对多:** 班级和老师之间的关系, 一个班级有多个老师, 一个老师也可以带多个班级.  
> **Django ORM**     
> [一对一](https://docs.djangoproject.com/en/4.0/topics/db/examples/one_to_one/) 采取成员变量(`models.OneToOneField`)来获得, 成员变量对象的生命周期随主对象结束而结束.  
> [一对多、多对多](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/) 采取中间对象(`TableName_set`)来获得, 成员变量对象的生命周期随主对象结束而结束.  


### 依赖关系(Dependency)
依赖关系描述一个对象在运行时会使用另一个对象的关系.  
依赖关系是一种临时关系, 通常是在运行时产生, 等价于函数定义了一个参数表示函数以来这个参数, page-86, [箭头参考](./UMLIcons.md#依赖关系(Dependency)) .  

### 聚合关系(Aggregation)  
聚合关系表达整体由部分构成, 整体和部分不是强依赖的,   
即使整体不存在了, 部分仍然存在(因为这个部分是由外部实例化的), page-90, [参考资料-1](https://faun.pub/association-aggregation-composition-python-ec9947832cbd) , [参考资料-2](https://gist.githubusercontent.com/sohaib-dev/d65a8d61be4cf5b529cba826703a5d96/raw/fee8cd8c804af63e3cc581e33e2c3c7cb98553c3/aggregation.py) .
```python3
# 来源
# https://faun.pub/association-aggregation-composition-python-ec9947832cbd
# https://gist.githubusercontent.com/sohaib-dev/d65a8d61be4cf5b529cba826703a5d96/raw/fee8cd8c804af63e3cc581e33e2c3c7cb98553c3/aggregation.py
class Student:

    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id) -> str:
        return str(self._id) + '-' + department_id


class Department:                                           # Department 就是整体

    def __init__(self, id, student: Student):
        self._id = id
        self._student = student                             # Student 就是部分

    def student_registration(self):
        return self._student.registration_number(self._id)


if __name__ == '__main__':
    student = Student(10)
    department = Department('ENG', student)                 # 聚合关系想表达: 即便 Department 被销毁了, student 仍然存在.  
    print(department.student_registration())

```

### 组合关系(Composition)  
组合关系表达整是拥有部分的, 是强依赖的关系,   
如果整体不存在了, 部分也将消亡(因为这个部分是有整体内部实例化的), page-90, [参考资料-1](https://faun.pub/association-aggregation-composition-python-ec9947832cbd) , [参考资料-2](https://gist.githubusercontent.com/sohaib-dev/04c670df1733e80764c217feb69761d6/raw/d96e720244739cd09898ea329da287ea4932a794/composition.py) .  

```python3
# 来源
# https://faun.pub/association-aggregation-composition-python-ec9947832cbd
# https://gist.githubusercontent.com/sohaib-dev/04c670df1733e80764c217feb69761d6/raw/d96e720244739cd09898ea329da287ea4932a794/composition.py
class Student:

    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id) -> str:
        return str(self._id) + '-' + department_id


class Department:

    def __init__(self, department_id, student_id):
        self._id = department_id
        self._student = Student(student_id)                 # Student这个部分, 由Department这个整体来实例化.

    def student_registration(self):
        return self._student.registration_number(self._id)


if __name__ == '__main__':
    department = Department('ENG', 10)                      # 组合关系想表达: 如果Department被销毁了, student也就不存在了.  
    print(department.student_registration())
```
