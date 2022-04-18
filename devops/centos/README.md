### 文件乱码问题

问题现象
```shell
[user@f2a4d2c8 ~]# cat hello.py
print("你好")
[user@f2a4d2c8 ~]# python3 hello.py
Traceback (most recent call last):
  File "hello.py", line 1, in <module>
    print("\u4f60\u597d")
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

查看当前系统的编码
```shell
[user@f2a4d2c8 ~]# locale
LANG="zh_CN.UTF-8"
LC_CTYPE="zh_CN.UTF-8"
LC_NUMERIC="zh_CN.UTF-8"
LC_TIME="zh_CN.UTF-8"
LC_COLLATE="zh_CN.UTF-8"
LC_MONETARY="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
LC_PAPER="zh_CN.UTF-8"
LC_NAME="zh_CN.UTF-8"
LC_ADDRESS="zh_CN.UTF-8"
LC_TELEPHONE="zh_CN.UTF-8"
LC_MEASUREMENT="zh_CN.UTF-8"
LC_IDENTIFICATION="zh_CN.UTF-8"
LC_ALL=
```

临时解决办法
```shell
[user@f2a4d2c8 ~]# localedef -c -f UTF-8 -i en_US en_US.UTF-8
[user@f2a4d2c8 ~]# export LANG=en_US.UTF-8
[user@f2a4d2c8 ~]# export LC_ALL=en_US.UTF-8
```

持久解决办法
```shell
[user@f2a4d2c8 ~]# echo "localedef -c -f UTF-8 -i en_US en_US.UTF-8" >> ~/.bashrc
[user@f2a4d2c8 ~]# echo "export LANG=en_US.UTF-8" >> ~/.bashrc
[user@f2a4d2c8 ~]# echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc
```

验收
```shell
[user@f2a4d2c8 ~]# python3 hello.py
你好
```
