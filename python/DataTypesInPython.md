### Python中的数据类型有哪些?
在 Python 中有两类数据类型.
#### 内置类型

|关键字|名称|
|---|---|  
| int  |  数字类型 |
|float| 浮点类型 | 
|str|字符串类型|
|list|列表类型|
|tuple|元祖类型|
|dict|字典类型(无序)|
|set|集合类型|

#### 标准库提供的类型

|关键字|名称|场景| 
|---|---|---:|
|queue.Queue|[队列类型](https://www.jianshu.com/p/a1a407ef5945)|[线程池]() 、[连接池]() |
|queue.LifoQueue|[栈类型](https://blog.csdn.net/kuangsonghan/article/details/79499380)|[反向排序](./stack-reverse.py)、[计算器](./interview1626-calculator-lcci.py) 、[有效括号](./0020-valid-parentheses.py)|
|queue.PriorityQueue|优先级队列类型|-|
|collections.deque|双向队列类型|-|
|collections.defaultdict|默认值字典|-|
|collections.ordereddict|有序字典|-|
