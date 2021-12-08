### 生成器
本文试图在 [可迭代对象、迭代器、生成器, 三者的关系](./IterableIteratorGenerator.md#生成器(Generator)) 一文的基础上继续讨论`生成器`话题.  

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


