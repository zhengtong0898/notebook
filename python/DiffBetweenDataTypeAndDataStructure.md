### 数据类型和数据结构的区别?  
严格意义上来说，在 Python 中的数据类型其实只有 3 个, 其他全部都是数据结构.

#### 数据类型

|关键字|名称|
|---|---|  
| int  |  数字类型 |
|float| 浮点类型 | 
|str|字符串类型|


#### 数据结构
|关键字|名称|使用场景|
|---|---|---:|
|list|列表类型|-|
|tuple|元祖类型|-|
|dict|字典类型(无序)|-|
|set|集合类型|-|
|queue.Queue|[队列类型](https://www.jianshu.com/p/a1a407ef5945)|[线程池]() 、[连接池]() |
|queue.LifoQueue|[栈类型](https://blog.csdn.net/kuangsonghan/article/details/79499380)|[反向排序](./stack-reverse.py)、[计算器](./interview1626-calculator-lcci.py) 、[有效括号](./0020-valid-parentheses.py)|
|queue.PriorityQueue|优先级队列类型|-|
|collections.deque|双向队列类型|-|
|collections.defaultdict|默认值字典|-|
|collections.ordereddict|有序字典|-|
