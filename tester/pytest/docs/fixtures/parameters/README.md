### 参数化

> **关注点:**   
> pytest.fixture 的 [params](./parametrizing_fixtures/conftest.py#L5) 参数.  
  

- [origin_fixtures](./origin_fixtures)  
  初始状态的代码
  ```shell
  ============================= test session starts ==============================
  platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-0.13.1
  rootdir: notebook/tester/pytest/docs/fixtures/parameters/origin_fixtures, configfile: pytest.ini
  plugins: xdist-2.5.0, allure-pytest-2.9.45, loadinitialconftests-0.0.0, cmdlineparse-0.0.0, forked-1.4.0
  collected 2 items
  
  test_case.py::test_ehlo FAILED                                           [ 50%]
  test_case.py::test_noop FAILED                                           [100%]
  
  =================================== FAILURES ===================================
  ```


- [parametrizing_fixtures](./parametrizing_fixtures)  
  增加参数化的代码
  ```shell
  ============================= test session starts ==============================
  platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-0.13.1
  rootdir: notebook/tester/pytest/docs/fixtures/parameters/parametrizing_fixtures, configfile: pytest.ini
  plugins: xdist-2.5.0, allure-pytest-2.9.45, loadinitialconftests-0.0.0, cmdlineparse-0.0.0, forked-1.4.0
  collected 4 items
  
  test_case.py::test_ehlo[smtpdm.aliyun.com] FAILED                        [ 25%]
  test_case.py::test_noop[smtpdm.aliyun.com] FAILED                        [ 50%]
  test_case.py::test_ehlo[mail.python.org] FAILED                          [ 75%]
  test_case.py::test_noop[mail.python.org] FAILED                          [100%]
  
  =================================== FAILURES ===================================
  ```



&nbsp;  
### 条件参数  

> **关注点:**  
> pytest.fixture 的 `params` 参数期望是一个列表类型的值, 它除了支持字符串、数字这些基础值之外,   
> 还支持解析 pytest.param 成员, 用于标记某个参数是什么标签.  
> `pytest.param(2, marks=pytest.mark.skip)`  
> 这行代码就是一个条件参数，指的是: 当参数值是2时, 采取SKIP策略;  
> 备注: marks可以使用pytest.mark.skipIf来做更进一步的条件限定.  

[样例代码](parametrizing_param/test_case.py)

```python3
# content of test_fixture_marks.py
import pytest


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass

```

输出:
```shell
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-0.13.1
rootdir: notebook/tester/pytest/docs/fixtures/parameters/parametrizing_param
plugins: xdist-2.5.0, allure-pytest-2.9.45, loadinitialconftests-0.0.0, cmdlineparse-0.0.0, forked-1.4.0
collected 3 items

test_case.py::test_data[0] PASSED                                        [ 33%]
test_case.py::test_data[1] PASSED                                        [ 66%]
test_case.py::test_data[2] SKIPPED (unconditional skip / 无条件跳过)       [100%]

========================= 2 passed, 1 skipped in 0.03s =========================
```
