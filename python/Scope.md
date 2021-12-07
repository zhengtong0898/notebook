### 作用域
我们在编程的时候经常会听到`全局变量`和`局部变量`, 这些词汇在`Python`中统称为作用域.  
`Python`的作用域遵循`LEGB`规则来管理变量的访问顺序和读写权限, 下表列出了`LEGB`的全称.  

|首字母|英文单词|中文含义|
|---|---|---|
|L|Local|本地域|
|E|Enclosing|闭包域|
|G|Global|全局域|
|B|Built-in|内置域|

&nbsp;  
### LEGB规则
一般情况下,   
`Python`创建的变量, 要么是`Local variable`, 要么是 `Global variable`.  
`Python`访问变量时, 按照`Local`、`Enclosing`、`Global`、`Built-in`的顺序来读取.  
```python3
#!/bin/env python3


foo = "foo"                               # 创建变量: Global variable


def main():
    bar = "bar"                           # 创建变量: Local variable to main function
    sss = "sss"                           # 创建变量: Local variable to main function
    
    def show_result():
        toy = "toy"                       # 创建变量: Local variable to show_result function
        sss = "xxx"                       # 创建变量: Local variable to show_result function
        
        print(f"toy: {toy}")              # 访问变量: 从Local作用域中找到toy变量, 将它打印出来.
        
        print(f"sss: {sss}")              # 访问变量: 从Local作用域中找到sss变量, 所以就不会再去Enclosing作用域中去找.
        
        print(f"bar: {bar}")              # 访问变量: 从Local作用域中没找到bar变量, 
                                          #          按照LEGB原则, 下一个寻找点是Enclosing作用域 
                                          #          对于show_result函数来说, bar变量就是Enclosing作用域中的变量.
        
        print(f"foo: {foo}")              # 访问变量: 从Local作用域中没有找到foo变量,
                                          #          从Enclosing作用域中没有找到foo变量,
                                          #          从Global作用域中找到了foo变量, 将它打印出来.
        
        print(f"dir: {dir}")              # 访问变量: 从Local作用域中没有找到dir变量,  
                                          #          从Enclosing作用域中没有找到foo变量,  
                                          #          从Global作用域中没有找到foo变量,  
                                          #          从Built-in作用域中找到了dir变量, 将它打印出来.  

    show_result()
    print(f"bar: {bar}")                  # 访问变量: 从Local作用域中找到bar变量(备注: 对于main函数来说, bar是在Local作用域中).
    print(f"sss: {sss}")                  # 访问变量: 从Local作用域中找到sss变量
    


if __name__ == '__main__':
    main()
```

&nbsp;  
### LEGB拓展
`Python`提供了两个关键字来处理非一般情况. 
1. 无法在函数内直接修改全局变量
   ```python3
   #!/bin/env python3
   foo = "foo"
   
   
   def main(): 
       foo = "bar"                        # 这里其实是在 main 函数的 Local作用域 中创建了一个foo变量.
       print(f"foo: {foo}")               # 输出 foo: bar
   
   
   if __name__ == '__main__':
       main()
       print(f"foo: {foo}")               # 输出 foo: foo
   ```
   解决办法
   ```python3
   #!/bin/env python3
   foo = "foo"
   
   
   def main(): 
       global foo                         # 先将Global作用域中的foo变量, 下层到Local作用域中.
       foo = "good luck"                  # 然后在对foo变量进行改动.
       print(f"foo: {foo}")               # 输出 foo: good luck
   
   
   if __name__ == '__main__':
       main()
       print(f"foo: {foo}")               # 输出 foo: good luck
   ```

&nbsp;  
2. 无法在内嵌函数中修改那些不是全局变量的外部变量.
   ```python3
   #!/bin/env python3

   
   def main(): 
       sss = "sss"       
          
       def show_result():
           sss = "change"                 # 这里其实是在 show_result 函数的 Local作用域 中创建了一个sss变量.
           print(f"sss: {sss}")           # 输出 sss: change
   
       show_result()
       print(f"sss: {sss}")               # 输出 sss: sss
   
   if __name__ == '__main__':
       main()
   ```
   解决办法
   ```python3
   #!/bin/env python3
   
   
   def main(): 
       sss = "sss"       
          
       def show_result():
           nonlocal sss
           sss = "change"                 # 这里其实是在 show_result 函数的 Local作用域 中创建了一个sss变量.
           print(f"sss: {sss}")           # 输出 sss: change
   
       show_result()
       print(f"sss: {sss}")               # 输出 sss: change
   
   if __name__ == '__main__':
       main()
   ```

&nbsp;  
### 可观测的作用域
`Python`还提供了`globals`、`locals`、`vars`、`dir`四个内置方法来窥探作用域中的变量信息.

- **globals**  
  返回值中包含了所有可访问的全局变量、全局对象.  


- **locals**  
  返回值中包含了`Local作用域`中创建的变量和对象.


- **vars**  
  不传参的情况下, 返回值与`locals`内置函数返回值一致.  
  参数可传: `class`、`instance`、`module`、`function`.  
  列出参数对象的所有属性值, 不含方法, 不含内置方法.
  ```python3
  class Hello:

      def __init__(self):
          self.ok = "ok"
          self.hello = "hello"
          self.world = "world"
          self._get = "_get"
          self.__get = "__get"

      def walk(self):                   # 不会被 vars 打印出来
          return "walk"


  def main():
      h = Hello()
      print(vars(h))                    # 输出: {'ok':          'ok', 
                                        #       'hello':       'hello', 
                                        #       'world':       'world', 
                                        #       '_get':        '_get', 
                                        #       '_Hello__get': '__get'}


  if __name__ == '__main__':
      main()
  ```


- **dir**   
  不传参的情况下, 返回值相当于是 `lit(locals().keys())`.  
  传参的情况下, 返回值中包含参数对象的内置方法、隐藏方法、常规方法、属性等信息.  
  ```python3
  class Hello:

      def __init__(self):
          self.ok = "ok"
          self.hello = "hello"
          self.world = "world"
          self._get = "_get"
          self.__get = "__get"

      def walk(self):                   # 不会被 vars 打印出来
          return "walk"


  def main():
      h = Hello()
      print(dir(h))                     
  
  
  # 输出: ['_Hello__get', '__class__', '__delattr__', 
  #       '__dict__', '__dir__', '__doc__', '__eq__', 
  #       '__format__', '__ge__', '__getattribute__', 
  #       '__gt__', '__hash__', '__init__', '__init_subclass__', 
  #       '__le__', '__lt__', '__module__', '__ne__', '__new__', 
  #       '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
  #       '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
  #       '_get', 'hello', 'ok', 'walk', 'world']


  if __name__ == '__main__':
      main()
  ```
