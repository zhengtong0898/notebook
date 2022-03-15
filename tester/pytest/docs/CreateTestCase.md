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


def function_test():                        # pytest无法识别这是一个测试用例.
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

