### unittest terms(术语)
- test case(测试用例)  
  框架使用者视角:  
  &nbsp; &nbsp; &nbsp; &nbsp; `class TestCase`用来组织测试用例.  
  &nbsp; &nbsp; &nbsp; &nbsp; `TestCase.test_`前缀方法用来表示每个独立的测试用例(单元测试).  
  &nbsp; &nbsp; &nbsp; &nbsp; `TestCase.test_`多个方法在一个类中，表示它们是同一个功能模块或性质相同的用例.  
  框架内部视角:  
  &nbsp; &nbsp; &nbsp; &nbsp; 每个`test_`前缀的方法, 都被当作是一个独立的用例来运行, [参考这里](https://github.com/zhengtong0898/source-decode/blob/main/unittest/unittest-1.0/loader.py#L124).  
  &nbsp; &nbsp; &nbsp; &nbsp; 每个`test_`前缀的方法, 都享有共同的类方法和类生命周期方法.
  

- test fixture(测试前后装置)  
  非技术视角:   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试之前，需要先准备一些测试数据(prepare fixture),   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试完毕后, 需要清除对应的测试数据(suffix fixture).      
  技术视角:   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试之前，先执行 TestCase.setUpClass 方法(用于准备测试数据),   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试完毕后, 补充执行 TestCase.tearDownClass 方法(用于清除对应的测试数据).  
  

- test suite(测试套件)  
  测试套件是一个测试用例集合, 通过`suite`可以将不同的用例组合在一起, 从而达成某个目标或任务.   
  

- test runner(测试执行器)   
  负责执行测试用力并汇总结果(默认是纯文本: `TextTestRunner` 和 `TextTestResult`)反馈给用户.    
  也可以使用第三方`runner`, 比如说: `htmltestrunner.HTMLTestRunner` 和 `htmltestrunner._TestResult`.
  

&nbsp;  
&nbsp;  
### [Why writing tests](https://docs.pytest.org/en/stable/fixture.html#what-fixtures-are)
In the simplest terms, a test is meant to look at the result of a particular behavior, and make sure that result aligns with what you would expect. Behavior is not something that can be empirically measured, which is why writing tests can be challenging.  
> 测试就是输入一组数据, 然后断言其结果是否于预期一致.  
> 断言可以分为: 过程断言 和 结果断言.  
> 
> 过程断言: 关注其过程的表现是否符合预期;      
> &nbsp; &nbsp; &nbsp; &nbsp;例如: 一个流程性质的用例需要多个接口配合, 需要为每个接口断言一次或多次.     
> 
> 结果断言: 关注其最终结果的表现是否符合预期.  
> 
> 代码复用, 是动一发而牵全身的典型场景, 由于某个代码的改动,   
> 很多模块中的很多功能都不同程度的出现了问题.  
> 这也就是为什么软件在迭代过程中时常会出现令人不可预期的表现,  
> 自动化的回归测试(单元测试、接口测试、ui自动化测试),  
> 就是为了能在CICD过程中第一时间反映出软件的潜在问题.  


&nbsp;  
### pytest函数匹配规则
```shell
# test_* 前缀的函数, 都会被pytest运行.
# *_test 后悔的函数, 都会被pytest运行.
# entrypoint  函数, 也会被pytest运行.
python_functions = test_* *_test entrypoint
```

&nbsp;  
### pytest.fixture装饰器
使用了pytest.fixture装饰器的函数, 都被视为是一个可以被消费的对象,   
它可以是一个数据集(比如说: 字典类型、列表类型), 也可以是一个对象(比如说: 某个客户端类对象).  

使用了pytest.fixture装饰器的函数, 通常只能当作参数服务于 `test_*` 、`*_test`、`entrypoint` 用例函数.
```
import pytest


@pytest.fixture
def custom_data():
    data = {"custom_key": "custom_value"}
    yield data
    del data


# 默认情况下, pytest 会根据用例定义的参数名, 尝试匹配同名的@pytest.fixture函数.
# 当匹配命中时, 执行 next 触发 yield 返回指定对象.
# 当匹配未命中时, 退出程序并抛出相关的异常信息.
def test_something(custom_data):
    assert type(custom_data) is dict
    assert custom_data == {"custom_key": "custom_value"}

```

使用 pytest.fixture 提供的 name 参数特性, 支持特定字符匹配.
```shell
import pytest


# 当声明了 pytest.fixture 的 name 参数之后,
# 函数名不再起到匹配作用,
# 只能使用 name 参数字符串进行匹配.
@pytest.fixture(name="ass")
def custom_data():
    data = {"custom_key": "custom_value"}
    yield data
    del data


def test_something(ass):
    assert type(ass) is dict
    assert ass == {"custom_key": "custom_value"}

```

pytest.fixture针对score参数:
1. `function`: 当前方法, 每个函数都会触发执行.
2. `class`: 当前类, 每个类和函数都会触发执行.
3. `module`: 当前文件, 当前文件内只触发执行一次.
4. `package`: 当前包, 当前包内只触发执行一次.
5. `session`: 当前程序的完整生命周期只触发执行一次.


fixture针对params参数:  
适合那种相同代码流程, 使用不同参数来驱动重复执行.   
统称: 参数化执行相同流程的用例.  


fixture针对ids参数:     
pytest执行用例时, 默认情况下会将 params 的值打印出来,   
当值比较大时, 控制台的输出会比较乱, 无法直观查看用力执行情况.   
通过使用ids为用例标识一个简单的编号即可.  


  



&nbsp;  
&nbsp;  
### 参考资料
[unittest: terms](https://docs.python.org/3/library/unittest.html)  
[pytest: what fixtures are](https://docs.pytest.org/en/stable/fixture.html#what-fixtures-are)  
[框架比较: 三种最流行的Python测试框架，我该用哪一个？](https://slxiao.github.io/2019/06/03/py-test/)  
[框架比较: Pytest why its more popular than unittest](https://blog.j-labs.pl/2019/02/Pytest-why-its-more-popular-than-unittest)  
[框架比较: unittest vs pytest](https://stackoverflow.com/questions/27954702/unittest-vs-pytest)  

### TODOLIST
mark   
Pytest why its more popular than unittest
