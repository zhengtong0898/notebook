### 条件语句
```python3
# 一般形式
# 这个条件句会触发 print("bingo") 指令.
ss = "hello"
if ss == "hello":
    print("bingo")

    
# 两路分支
# 这个条件句会触发 print("warning") 指令.
ss = "world"
if ss != "world":
    print("bingo")
else:
    print("warning")


# 多路分支
ss = "python"
if ss == "hello":
    print("hello")
elif ss == "world":
    print("world")
else:
    print("bingo")


# 三元表达式
ss = "cpython"
rst = "pypy" if ss == "pypy" else ss
print(rst)
```

&nbsp;  
### 循环语句

&nbsp;  
**while循环**   
当条件为True时, 执行循环体内的语句.   
当条件为False时, 跳出循环.
```python3

# 一般形式: 循环去执行一些指令
count = 1
while count < 10:
    print(count)                        # 输出: 1, 2, 3, 4, 5, 6, 7, 8, 9
    count += 1          


# 一般形式: 循环试图去命中匹配
rst = False
items = ["Python", "CPython", "pypy", "pyjion", "Cpython"]
while items:
    item = items.pop()
    if item == "Jython":
        rst = True
        break

if rst is True:
    print("matched")
else:
    print("not match")


# 利用 循环+else 语法, 会获得两个好处: 
# 1. 当没有命中匹配时, 可以再 else 的区域做一些额外的代码处理.
# 2. 将逻辑代入到循环体内, 使编码一气呵成.
items = ["Python", "CPython", "pypy", "pyjion", "Cpython"]
while items:
    item = items.pop()
    if item == "Jython":
        print("matched")
        break
else:
    print("not match")
```

&nbsp;  
**for循环**  
挨个遍历 `列表`、`元祖`、`集合`、`字典` 这种可迭代对象.
```python3

# 一般形式
items = ["Python", "CPython", "pypy", "pyjion", "Cpython"]
for item in items:
    print(item)


# 一般形式: 循环试图去命中匹配
rst = False
items = ["Python", "CPython", "pypy", "pyjion", "Cpython"]
for item in items:
    if item == "Jython":
        rst = True
        break

if rst is True:
    print("matched")
else:
    print("not match")


# 利用 循环+else 语法, 会获得两个好处: 
# 1. 当没有命中匹配时, 可以再 else 的区域做一些额外的代码处理.
# 2. 将逻辑代入到循环体内, 使编码一气呵成.
items = ["Python", "CPython", "pypy", "pyjion", "Cpython"]
for item in items:
    if item == "Jython":
        print("matched")
        break
else:
    print("not match")


# 列表推导式-1
items = ["Python", "CPython", "pypy", "pyjion", "Cpython"]
rst = [True for item in items if item == "Jython"]
if any(rst):
    print("matched")
else:
    print("not matched")


# 列表推导式-2
items = ["Python", "CPython", "pypy", "pyjion", "Cpython"]
rst = [True if item == "Jython" else False for item in items]
if any(rst):
    print("matched")
else:
    print("not matched")
```