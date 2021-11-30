### 字符串格式化技巧
1. 百分比语法
```
ss = "python2 is %s language" % "programing" 
print(ss)                                           # 输出: python2 is programing language
```

2. 字符串内置方法: format
```
# 示例-1
ss = "python3 is {} language"
print(ss.format("programing"))                      # 输出: python3 is programing language

# 示例-2
ss = "{language} is {typo} language"
print(ss.format(language="shell", typo="script"))   # 输出: shell is script language
```

3. 字符串插值法: f-string   
   这个是 Python3.6 新增的的新语法
```
language = "pypy"
typo = "programing"
ss = f"{language} is {typo} language"
print(ss)                                           # 输出: pypy is programing language
```

4. 将数字变量集成到字符串中
```
pencel_price = 5
ss = f"pencel price: {pencel_price} RMB"
print(ss)                                           # 输出: pencel price: 5 RMB
```

5. 控制浮点数的小数个数
```
pi = 3.1415926
ss = f"pi: {pi:.2f}"                                # 仅保留两位小数点(四舍五入)
print(ss)                                           # 输出: pi: 3.14
```

6. 控制变量对齐
```
# 示例-1
# :< 左对齐 , 对应的内置方法是 ljust
language = "cpython"
ss = f"{language:<20} is programing language"
print(ss)                                           # 输出: cpython              is programing language


# 示例-2
# :> 右对齐 , 对应的内置方法是 rjust
language = "cpython"
ss = f"{language:>20} is programing language"
print(ss)                                           # 输出:              cpython is programing language


# 示例-3
# :^ 居中对齐 , 对应的内置方法是 center
language = "cpython"
ss = f"{language:^20} is programing language"
print(ss)                                           # 输出:       cpython        is programing language


# 高级示例
# :*< 左对齐, 右侧使用*代替空格
language = "cpython"
ss = f"{language:*<20} is programing language"
print(ss)                                           # 输出: cpython************* is programing language
```
