### 概述
本文试图在 [可迭代对象、迭代器、生成器, 三者的关系](./IterableIteratorGenerator.md#生成器(Generator)) 一文的基础上继续讨论`生成器`话题.  
在`Python2`的时代, 高性能网络异步框架`tornado`于2008年诞生, 它试图使用生成器结合非堵塞socket特性解决`C10K`的问题.  
随着时间的推移, 生成器被越来越多的运用和总结, `Python3`在生成器的概念基础上提炼出了`async/await`的编程模式, 像著名的 [aio-libs](https://github.com/aio-libs) 项目汇聚了所有异步的网络编程库, 这已经成为了目前`Python3`主流的异步编程流派.  


&nbsp;  
### 生成器的接口
生成器时异步编程的基石, 想要很好的探索生成器的编程模型, 需要先掌握生成器的每个接口的作用,  
这里将生成器的所有接口逐一罗列出来并阐述它们的作用和表现.  


&nbsp;  
**普通函数**  
当我们执行一个函数时, Python会从头到尾的执行该函数体内的代码.   
```python3

def simple():
    return "10"

    
ss = simple()
print(ss)                           # output: 10
``` 

&nbsp;  
**yield关键字**  
当我们在函数中使用`yield`关键字时, 执行该函数并不会执行任何代码, 而是返回一个`generator`对象.  
也就是说, 当我们执行一个含有`yield`关键字的函数时, Python会将函数转换成`<class 'generator'>`类对象, 并实例化这个类对象.  
```python3

def example():
    yield "10"

ss = example()
print(ss)                           # output: <generator object example at 0x7fc04b0db9d0>
```
&nbsp;  
**next内置函数**  
此时, `ss`这个变量是一个`<generator object example at 0x7fc04b0db9d0>`对象, 这个对象就是一个生成器.  
从`Python2.2`开始, 生成器只有一个对外开放的接口: `__next__`, 可以使用内置函数`next`来触发这个接口.  
只有触发了生成器的`__next__`接口, 将会触发执行`exmaple`体内的代码.
```python3

def example():
    yield "10"                      # 函数中使用了 yield 关键字.

print(type(example))                # 未调用example之前, Python 认为它是一个普通函数.

ss = example()                      # 调用 example 时, 
                                    # Python 发现函数体内有 yield 关键字, 
                                    # Python 将 example 函数转换成 <class 'generator'>, 
                                    # Python 然后实例化这个生成器类.
                                    
print(ss)                           # output: <generator object example at 0x7fc04b0db9d0>
xx = next(ss)                       # 执行 example 体内的代码.
print(xx)                           # output: 10
```

&nbsp;  
**StopIteration异常**  
上面`example`的案例只能生产一个值`"10"`, 当我们再次使用`next`触发生成器的`__next__`接口, 会抛出`StopIteration`异常.  
之所以会抛异常是因为`__next__`接口有一个特殊的使命, 开始执行代码, 要么遇到下一个`yield`(返回一个值, 然后挂起生成器), 要么抵达函数底部并抛出一个异常.  
```python3

def example():
    yield "10"
    print("hello world!")


ss = example()
xx = next(ss)                       # next(ss)会触发ss的__next__接口, 从example体内的第一行代码开始执行, 
                                    # 当遇到 yield "10" 后, 将 "10" 返回给外部.
                                    # example体内的代码会停留在 yield "10" 的位置, 
                                    # 当下一次再执行 next(ss) 时, 会从 yield "10" 的下一行开始执行.
                                    
print(f"xx: {xx}")                  # output: "10"

zz = next(ss)                       # next(ss)会触发ss的__next__接口, 从 print("hello world!") 这一行开始执行代码.
                                    # 所以这里会打印 "hello world!" 这个字符串,
                                    # 然后是抵达函数尾部, 但是__next__接口并没有如期遇到yield关键字, 所以此时它会抛出异常.
                                    # Traceback (most recent call last):
                                    #   File "python/ss.py", line 9, in <module>
                                    #     zz = next(ss)
                                    # StopIteration
```
小结: 
1. `next()` 会触发 `generator.__next__` 接口.
2. `generator.__next__` 要么返回 `yield` 右侧的值, 要么抛 StopIteration 异常.


&nbsp;  
**generator.send方法**  
从`python2.5`开始, `generator`对象新增了一个`send`方法, 这个方法的作用是:  
允许外部程序传递一个值进入到生成器中来, 然后唤醒生成器的执行, 它的行为由两个动作组成:
1. 传递一个值给`yield`左侧的变量.
2. 唤醒`generator`对象, 执行后续代码, 要么遇到下一个yield, 要么抵达函数底部并抛出一个异常.    
```python3

def example():
    recv = yield "10"
    print(f"recv: {recv}")

ss = example()
xx = next(ss)                       # 代码将"10"返回给外部, ss这个`generator`对象就会被挂起, 不会执行左侧的'recv = '这部分代码.
ss.send("good")                     # 将"good"传递给'recv = '的右侧, 即: 'recv = "good"';
                                    # 触发ss.__next__接口, 从 'recv = "good"' 开始执行赋值, 
                                    # 然后继续往下执行代码, 要么再次遇到yield返回值和挂起, 要么抵达函数底部抛StopIteration异常.
```

&nbsp;  
**generator.throw方法**  
从`python2.5`开始, `generator`对象新增了一个`throw`方法, 这个方法的的作用是:  
允许外部程序传递一个异常对象进入到生成器中来, 这样做的目的是唤醒生成器并告诉它出现异常了,  
此时生成器内部可以根据异常信息和当前作用域的变量值的情况来决定该如何处理异常.
```python3
def example():
    yield "10"                             
    yield "20"
    yield "30"


ss = example()
resp = next(ss)
ss.throw(RuntimeError, "bad value")                         # 将抛异常的动作在`generator`的对象内触发, 它会发生在挂起点.

# Traceback (most recent call last):
#   File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py", line 1483, in _exec
#     pydev_imports.execfile(file, globals, locals)  # execute the script
#   File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
#     exec(compile(contents+"\n", file, 'exec'), glob, loc)
#   File "python/ss.py", line 9, in <module>
#     ss.throw(RuntimeError, "bad value")
#   File "python/ss.py", line 2, in example
#     yield "10"                                            # 重点在这里, 它会告诉你是在哪里报错的, 你会知道挂起点在哪里.
# RuntimeError: bad value
```

&nbsp;  
**generator.close方法**  
从`python2.5`开始, `generator`对象新增了一个`close`方法,   
允许外部程序将生成器设定为结束状态, 此时如果生成器的`__next__`接口再次被触发, 它就会抛StopIteration异常.
```python3
def example():
    yield "10"
    yield "20"
    yield "30"

ss = example()
xx = next(ss)
ss.close()                                                  # 关闭生成器
print(f"xx: {xx}")
xx = next(ss)                                               # 已关闭的生成器, 不能在继续执行代码, 此时会抛出StopIteration异常.

# Traceback (most recent call last):
#   File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py", line 1483, in _exec
#     pydev_imports.execfile(file, globals, locals)  # execute the script
#   File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
#     exec(compile(contents+"\n", file, 'exec'), glob, loc)
#   File "python/ss.py", line 10, in <module>
#     xx = next(ss)
# StopIteration
```

&nbsp;  
**StopIteration 异常处理**   
`tornado`利用生成器的异常处理机制, 可以将[结果即时的返回](https://www.tornadoweb.org/en/stable/gen.html#tornado.gen.Return) 给外部程序.  
这是一个比较抽象的情况, 不理解不要紧, 以后阅读框架性源码遇到的时候在过来看就好.  
```python3

def example():
    count = 0
    while True:
        recv = yield count
        count += 10
        if recv == "close generator":       
            return "closed"                 # return "closed", 其实是告诉生成器, 抵达函数底部了, 抛 StopIteration 异常把.


ss = example()

xx1 = next(ss)                              # next 返回的是 yield 右侧的值
assert xx1 == 0                             

xx2 = next(ss)
assert xx2 == 10

xx3 = next(ss)
assert xx3 == 20

try:
    ss.send("close generator")              # send 完成的是 yield 左侧的赋值
except StopIteration as ex:                 # 
    xx4 = ex.value                          # 重点在这里: 利用异常机制的 value 接口获取正确的值.
    assert xx4 == "closed"

```


&nbsp;  
**yield from 关键字**  
从`python3.3`开始提供了`yield from`关键字, 这个关键字为生成器提供了两个能力:
1. 让代码扁平化, 简化代码的编写(用处不大).
```python3

# yield的编码方式
def example_1():
    for i in [5, 4, 3, 2, 1]:
        yield i

    for i in [0, 1, 2, 3, 4]:
        yield i

# yield from的编码方式
def example_2():
    yield from [5, 4, 3, 2, 1]
    yield from [0, 1, 2, 3, 4]


list(example_1()) == list(example_2()) == True

```
2. 使`generator.send`具备将`值`和`异常`持续(多级的)透传给`子生成器`的能力.  
3. `yield from`使代码抽象到子生成器中变得更容易一些, 对父生成器起到扁平化、逻辑简化的效果.
```python3

# 子生成器
def accumulate():
    tally = 0                                   # 计数器
    while True:
        recv = yield                            # yield 右侧的值, 会透传回给非生成器(外部)对象
                                                # 由于这里的 yield 右侧没有值, 所以透传回给非生成器对象是一个None
                                                # yield 左侧的值, 是由外部通过 generator.send 传递进来的.
        
        if recv is None:                        # 当外部 generator.send(None) 进来时,                                                 
            return tally                        # 会结束掉当前生成器.
        
        tally += recv


# 父生成器
def gather_tallies(tallies):
    while True:
        tally = yield from accumulate()         # generator.send 的值会透传到 accumulate 子生成器中,
                                                # next() 触发的也是accumulate子生成器,
                                                # yield from 还有一个隐藏能力, 就是不需要处理StopIteration.
                                                # 当 accumulate 子生成器 return 值时, 
                                                # yield from自动捕获StopIteration并将值, 赋值给tally.
        tallies.append(tally)


tallies = []
acc = gather_tallies(tallies)                   # 将函数转换和实例化成为生成器对象.
next(acc)                                       # 开始执行生成器对象, 要么遇到yield挂起生成器, 要么抵达底部抛StopIteration.
                                                # next(acc) 这个动作会透传到 accumulate 子生成器中.
                                                
for i in range(4):
    acc.send(i)                                 # 透传四个值进入accumulate子生成器: 0, 1, 2, 3 = 6

acc.send(None)                                  # 透传一个None进入accumulate子生成器, 
                                                # 此时 accumulate 子生成器, 抛一个StopIteration异常.
                                                # 但被 yield from 捕获, 并将异常返回的值, 赋值给 tally 并添加到 tallies 中.
                                                
assert tallies == [6, ]                         # 所以此时, tallies 预期时等于 [6, ]                       

for i in range(5):                              
    acc.send(i)

acc.send(None)

assert tallies == [6, 10]
print(tallies)                                  # 输出: [6, 10]

```