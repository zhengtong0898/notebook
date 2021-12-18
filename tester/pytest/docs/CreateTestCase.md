### 概述
**pytest**的主要任务之一是识别测试用例文件、识别测试用例函数、识别测试用例类以及识别测试用例方法.  

- **识别测试用例文件**   
  当执行**pytest**命令且不带任何参数时, 它会递归式的扫描当前路径下的所有文件, 当文件名的前缀是以`test_`打头时, 会被视为这是一个测试用例文件.    
  当执行**pytest**命令并指定文件时, 即便文件名没有`test_`前缀, 这个文件也被视为测试用例文件.   
  **备注:** 识别测试用例文件, 是为后续在测试用例文件中识别测试用例而做准备.   


- **识别测试用例函数**    
  当函数名的前缀是以`test_`打头时, 该函数被视为是一个测试用例, 并会被纳入到测试用例集合中等待被**pytest**执行.


- **识别测试用例类**    
  当类名的前缀是以`Test`时, 会被视为是一个测试用例类.   
  **备注:** 识别测试用例类, 是为后续在类中识别测试用例方法而做准备.

  
- **识别测试用例方法**   
  当类方法的前缀是以`test_`打头时, 该方法被视为是一个测试用例, 并会被纳入到测试用例集合中等待被**pytest**执行.  


&nbsp;    
### 写用例
只有遵循上述原则去写用例, **pytest**才能有效的识别.  

**test_simple.py**
```python3


def test_function_a():
    print("test function a")


class Tester:

    def test_zzz(self):
        print("test zzz")

    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")


def function_test():
    print("test function a")


def test_function_b():
    print("test function a")

```

**执行测试**
```shell
$ pytest --verbose test_simple.py
========================================== test session starts ==========================================
platform darwin -- Python 3.8.12, pytest-5.4.3, py-1.11.0, pluggy-0.13.1 -- 
cachedir: .pytest_cache
metadata: {'Python': '3.8.12', 
           'Platform': 'macOS-10.15.5-x86_64-i386-64bit', 
           'Packages': {'pytest': '5.4.3', 'py': '1.11.0', 'pluggy': '0.13.1'}, 
           'Plugins': {'metadata': '1.11.0', 'html': '2.1.1'}, 
           'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk1.8.0_291.jdk/Contents/Home'}
rootdir: /sss
plugins: metadata-1.11.0, html-2.1.1
collected 5 items                                                                                       

test_simple.py::test_function_a PASSED                                                               [ 20%]
test_simple.py::Tester::test_zzz PASSED                                                              [ 40%]
test_simple.py::Tester::test_one PASSED                                                              [ 60%]
test_simple.py::Tester::test_two PASSED                                                              [ 80%]
test_simple.py::test_function_b PASSED                                                               [100%]

=========================================== 5 passed in 0.02s ===========================================
```

