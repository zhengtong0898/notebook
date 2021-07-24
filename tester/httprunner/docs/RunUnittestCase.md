### 如何运行httprunner框架的单元测试用例?

```shell
# 进入httprunner源码的根目录
$ cd httprunner

# 单独运行某个测试用例文件
$ python -m unittest discover -p "utils_test.py"
```