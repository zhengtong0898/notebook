`O(n)`被称为线性复杂度,
线性复杂度指的是随着循环次数的增加, 执行时间也会随之线性增长.  

`O(n)`在代码中通常对应的是单个层级`for`或`while`循环.   

下面的代码时间复杂度是: `O(1+1+100+100+100+1+1)`;
这里只关注最大阶的量级: 单个层级`for`循环; 
所以这里忽略掉常量, 只记`O(n)`.
```python
def main(n=100):
    sum = 0                      # 1 unit_time
    count = 1                    # 1 unit_time

    for i in range(n):           # 100 unit_time: 100次赋值给 i 
        sum += i                 # 100 unit_time: 100次追加赋值给 sum
        count += 1               # 100 unit_time: 100次追加赋值给 count
    
    print("sum: ", sum)          # 1 unit_time
    print("count: ", count)      # 1 unit_time
```

&nbsp;  

> 备注:
> 线性增长, 假设举例:
> 
> 当 times = 100 时, 执行耗时 1 毫秒(ms),   
> 当 times = 1000 时, 执行耗时 10 毫秒(ms),   
> 当 times = 10000 时, 执行耗时 100 毫秒(ms),   
> 当 times = 100000 时, 执行耗时 1000 毫秒(ms; 1000ms == 1s)   
> 
> 如果 times 倍增的规律 与 执行时间倍增的规律 一致, 那么就可以称之为线性增长.

&nbsp;  
&nbsp;  

> 补充:  
> 容易发生混淆的情况,  
> 下面这段代码, 由于 n 变量是固定的100,   
> `for` 循环就是一个已知大小的执行次数100,  
> 因此这段代码也是一个常量复杂度O(1).
 
```python

def main():
    n = 100
    sum = 0
    for i in range(n):
        sum += i
```