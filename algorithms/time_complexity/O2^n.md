`O(2^n)`被称为指数阶复杂度;
当 n 递增时(不是倍增), 执行次数倍增, 
这种情况通常被当作指数阶时间复杂度.    

典型的指数阶复杂度例子是: `斐波那契数列`; 
详细的分析需看[这里](https://stackoverflow.com/a/360773). 
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

&nbsp;  
&nbsp;   
### 参考
[Understanding time complexity with Python examples](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)   
[Computational complexity of Fibonacci Sequence](https://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence/360773#360773)