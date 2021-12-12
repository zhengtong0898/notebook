### 概述  
参数是函数的重要组成部分, 参数使函数具备复用的可能.   
参数有两个称呼: 形式参数(**Parameter**)和实际参数(**Argument**),  
当我们处在函数体内时, 函数头定义的参数要求, 就是形式参数,  
当我们处在函数外部, 要将参数传递给函数时, 这些参数就是实际参数.  


&nbsp;   
### 必填参数
在定义函数的形式参数(**Parameters**)时, 变量不指定默认值, 就代表该参数是必填参数.  
```python3

def example(a, b, c):                           # 定义形式参数: 三个参数都是必填参数, 缺一不可, 提供多了也不行.  
    print(f"a: {a}; b: {b}; c: {c}")


# 传参(实际参数), 支持的写法
example("apple", "banana", "orange")            # 直接传值
example(a="apple", b="banana", c="orange")      # 指定变量名传值(顺序)
example(c="orange", b="banana", a="apple")      # 指定变量名传值(乱序)
example("apple", "banana", c="orange")          # 混合形式: 前面部分采用直接传值, 后面部分采用指定变量名传值.
example("apple", b="banana", c="orange")        # 混合形式: 前面部分采用直接传值, 后面部分采用指定变量名传值(顺序).
example("apple", c="orange", b="banana")        # 混合形式: 前面部分采用直接传值, 后面部分采用指定变量名传值(乱序).
kws = {"a": "apple",
       "b": "banana",
       "c": "orange"}
example(**kws)                                  # 合法的写法: **会以键值的形式把一个字典解构为独立的关键字参数.


# 传参(实际参数), 不支持的写法
example(a="apple", "orange", "banana")          # 键值传递, 后续的参数必须也要键值传递, 不允许直接传值.
```

&nbsp;  
### 可选参数
在定义函数的形式参数(**Parameters**)时, 变量指定默认值, 就代表该参数是可选参数.  
```python3

def example(a="apple", b="banana", c="orange"): # 定义形式参数: 三个参数都是可选参数, 可不填写参数.
    print(f"a: {a}; b: {b}; c: {c}")


# 传参(实际参数), 支持的写法
example()                                       # 不传值, 此时函数使用默认值
example("aaa")                                  # 仅传一个值, 此时函数按顺序赋值给a变量, 剩余的b和c变量采用默认值.
example(c="aaa")                                # 仅传一个值, 指定变量传值给c变量, 剩余的a和b变量采用默认值.  
example("aaa", "bbb", "ccc")                    # 传三个值, 此时函数按顺序赋值给a,b,c变量, 覆盖掉默认值.  
example(c="aaa", a="bbb", b="ccc")              # 传三个值, 此时桉树按照指定的变量赋值, 覆盖掉默认值.  

# 传参(实际参数), 不支持的写法
example(a="apple", "orange", "banana")          # 键值传递, 后续的参数必须也要键值传递, 不允许直接传值.
```

&nbsp;  
### 可变长参数
在定义函数的形式参数(**Parameters**)时, 变量前面指定一个星号`*`或者两个星号`**`, 就代表该参数是可变长参数.    
变量前面指定一个星号`*`, 表示这个变量是一个列表类型的变量.  
变量前面指定两个星号`**`, 表示这个变量是一个字典类型的变量.  
```python3

def example(a, *b, **c):                        # 定义形式参数: 三个参数都是必填参数, 第一个是必填参数可以是任何类型的值, 
    print(f"a: {a}; b: {b}; c: {c}")            #             第二个参数必须传递一个列表, 第三个参数必须传递一个字典.  


# 传参(实际参数), 支持的写法
items = [1, 2, 3, 4, 5]
kws = {"k1": "ss", "kw": "xx"}
example("apple", *items, **kws)                 # 标准写法


# 除了标准写法, 剩下的写法都存在一些坑
example(*items, **kws)                          # a: 1; b: (2, 3, 4, 5); c: {'k1': 'ss', 'kw': 'xx'}
                                                # 由于第一个必填参数没有提供, 函数会将 *items 的第一个成员赋值给a变量.

                                                
example("apple", items, kws)                    # a: apple; b: ([1, 2, 3, 4, 5], {'k1': 'ss', 'kw': 'xx'}); c: {}
                                                # 由于传参时没有按照标准写法, 函数将items和kws当做一个列表赋值给b变量.


example(items, kws)                             # a: [1, 2, 3, 4, 5]; b: ({'k1': 'ss', 'kw': 'xx'},); c: {}
                                                # 由于未使用*和**, 函数将items当做赋值给a变量, 将kws当做一个成员纳入到列表中赋值给b变量.


kws2 = {"a": "apple", 
        "b": [1, 2, 3, 4, 5],
        "c": {"k1": "ss", "k2": "xx"}}
example(**kws)                                  # a: apple; b: (); c: {'b': [1, 2, 3, 4, 5], 'c': {'k1': 'ss', 'k2': 'xx'}}
                                                # **会以键值的形式把一个字典解构为独立的关键字参数,
                                                # kws2的{"a": "apple"}被正确解构并赋值给a变量, 
                                                # kws2的{"b": [1,2,3,4,5]}没有被解构赋值给b变量, 
                                                # 而是将 "b" 和 "c" 结构为一个字典, 赋值给c变量.
```

&nbsp;  
### 关键字参数
关键字参数(**Keyword-Only Parameters**)要求传参时, 必须指定变量名.  
备注: 从`Python3`开始支持这个特性.  
```python3

def example(a, *, b, c):                        # 定义形式参数: 第一个a是必填参数
    print(f"a: {a}; b: {b}; c: {c}")            #             第二个*是占位符
                                                #             第三个b是关键字参数, 要求传参时必须指定变量名.
                                                #             第四个c是关键字参数, 要求传参是必须指定变量名.  
    
# 传参(实际参数), 支持的写法
example("apple", b="banana", c="orange")        # 标准写法
example(a="apple", b="banana", c="orange")      # 标准写法
kws = {"a": "apple", 
       "b": "banana", 
       "c": "orange"}
example(**kws)                                  # **会以键值的形式把一个字典解构为独立的关键字参数,


# 传参(实际参数), 不支持的写法
example("apple", "banana", "orange")
```


&nbsp;  
### 固定参数
固定参数(**Positional-Only Parameters**)要求传参时, 必须按照固定的位置填写值.  
备注: 从`Python3.8`开支支持这个特性.
```python3

def example(a, b, /, c, d):                     # 定义形式参数: 第一个a是必填参数, 不允许指定变量名赋值
    print(f"a: {a}; b: {b}; c: {c}; d: {d}")    #             第二个b是必填参数, 不允许指定变量名赋值
                                                #             第三个/是占位符
                                                #             第四个c是关键字参数, 要求传参时必须指定变量名
                                                #             第五个d是关键字参数, 要求传参时必须指定变量名

# 传参(实际参数), 支持的写法
example("apple", "banana",                      # 标准写法
        c="orange", d="lemon")                  

items = ["apple", "banana"]
kws = {"c": "orange", "d": "lemon"}
example(*items, **kws)                          # 占位符(/)是一个非常典型的分水岭，将 *items 和 **kws 传参完美融合.  


# 传参(实际参数), 不支持的写法
example(a="apple", b="banana", 
        c="orange", d="lemon")                  # 占位符(/)要求左侧的形参不允许以指定变量名的方式来传参, 

kws = {"a": "apple", "b": "banana", 
       "c": "orange", "d": "lemon"}
example(**kws)                                  # 占位符(/)要求左侧的形参不允许以指定变量名的方式来传参, 
                                                # 然而**采取的就是解构字典后, 采取指定变量名的方式入参, 因此报错.  
```