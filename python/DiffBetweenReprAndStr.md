### repr和str的区别

- repr   
  适合在调试正则表达式、观测接口返回值时使用, debug分析文本的特殊字符内容时使用.
- str  
  适合做标准输出和日志输出时使用.   

```
ss = "he's a dog"
print([repr(ss)])                 # 输出: ['"he\'s a dog"']
print([str(ss)])                  # 输出: ["he's a dog"]
```
