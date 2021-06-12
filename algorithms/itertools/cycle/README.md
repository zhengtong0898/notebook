### cycle
`['a', 'b', 'c', 'd', 'e', 'f']` 无限循环迭代.  


&nbsp;  
思路
```
def pseudocode():
    iterable_l = ['a', 'b', 'c', 'd', 'e', 'f']
    while True:
        for i in iterable_l:
            yield i
```
