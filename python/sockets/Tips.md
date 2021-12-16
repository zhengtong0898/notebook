### File descriptor
根据 [Wikipedia](https://en.wikipedia.org/wiki/File_descriptor) 对文件描述符的定义.  

|Integer value|Name|zh_CN|
|---|---|---|
|0|Standard input|标准输入|
|1|Standard output|标准输出|
|2|Standard error|标准错误|

```python
import os


stdout = os.fdopen(fd=1, mode="w", buffering=1)
stdout.write("hello world!")
stdout.flush()


# 输出
# "hello world!"

```


