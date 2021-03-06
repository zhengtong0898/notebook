### 单接口用例参数化(不完整)
**httprunner**从`v3.1.3`开始支持基于**pytest**的[两种参数化功能](https://github.com/httprunner/httprunner/pull/952#issuecomment-654259434),  
第一种参数化功能是基于参数键值绑定变量, 可实现业务数据和断言数据一一对应形式的参数化驱动.  
第二种参数化能力是基于穷尽排列组合的方式让用例无死角的驱动, 简称: 笛卡尔积组合.    

&nbsp;  
### 参数化-1(参数键值绑定)
1. `host` 是公共变量, 抽出来放在`module`变量中,  
2. `parameters`是参数化关键字,   
   `username-password-status_code-body_status-body_msg` 采用`-`分割语法，表示声明一组变量名,    
   紧接着是两个列表, 列表中的值数量与上面的变量名数量一致, 且顺序一一对应.  

测试用例(httprunner-2.x语法): [login-api-v2-parameters-kvbind.yml](../apis/login-api-v2-parameters-kvbind.yml)

```yaml


config:
    name: "login parameters v2"
    variables:
        host: "http://127.0.0.1:8888"
    parameters:
        username-password-status_code-body_status-body_msg:
            - ["zhangsan", "zhangsan123", 200, 200, "login success"]
            - ["lisi", "lisi123", 200, 400, "login error"]


name: login
request:
    method: POST
    url: "${host}/login"
    headers:
        User-Agent: HttpRunner/${get_httprunner_version()}
        Content-Type: "application/x-www-form-urlencoded"
    data: "username=${username}&password=${password}"
validate:
    - eq: ["status_code", "${status_code}"]
    - eq: ["body.status", "${body_status}"]
    - eq: ["body.msg", "${body_msg}"]
```
测试用例(httprunner-3.x语法): [login-api-v3-parameters-kvbind.yml](../apis/login-api-v3-parameters-kvbind.yml)

```yaml


config:
    name: "login parameters v3"
    variables:
        host: "http://127.0.0.1:8888"
    parameters:
        username-password-status_code-body_status-body_msg:
            - ["zhangsan", "zhangsan123", 200, 200, "login success"]
            - ["lisi", "lisi123", 200, 400, "login error"]


teststeps:
-
    name: login
    request:
        method: POST
        url: "${host}/login"
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
            Content-Type: "application/x-www-form-urlencoded"
        data: "username=${username}&password=${password}"
    validate:
        - eq: ["status_code", "${status_code}"]
        - eq: ["body.status", "${body_status}"]
        - eq: ["body.msg", "${body_msg}"]


```
转换成.py文件: [login_api_v3_parameters_kvbind_test.py](../apis/login_api_v3_parameters_kvbind_test.py)
```python3
# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/login-api-v3-parameters-cartesian.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginApiV3ParametersCartesian(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username": ["zhangsan", "lisi", "xiaoming"],
                "password": ["zhangsan123", "lisi123", "xiaoming123"],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("login parameters cartesian v3").variables(
        **{"host": "http://127.0.0.1:8888", "status_code": 200}
    )

    teststeps = [
        Step(
            RunRequest("login")
            .post("${host}/login")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .with_data("username=${username}&password=${password}")
            .validate()
            .assert_equal("status_code", "${status_code}")
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginApiV3ParametersCartesian().test_start()

```

&nbsp;  
&nbsp;  
### 参数化-2(笛卡尔积组合)  
采用笛卡尔积组合来覆盖用例, 这个用例有一个特点, 那就是不论录入的参数是什么,   
它的断言点必须是相同的, 或者说干脆就不要有断言点.   

测试用例(httprunner-2.x语法): [login-api-v2-parameters-cartesian.yml](../apis/login-api-v2-parameters-cartesian.yml)

```yaml


config:
    name: "login parameters cartesian v2"
    variables:
        host: "http://127.0.0.1:8888"
        status_code: 200
    parameters:
        username: ["zhangsan", "lisi", "xiaoming"]
        password: ["zhangsan123", "lisi123", "xiaoming123"]


name: login
request:
    method: POST
    url: "${host}/login"
    headers:
        User-Agent: HttpRunner/${get_httprunner_version()}
        Content-Type: "application/x-www-form-urlencoded"
    data: "username=${username}&password=${password}"
validate:
    - eq: ["status_code", "${status_code}"]


# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'zhangsan', 'password': 'zhangsan123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'zhangsan', 'password': 'lisi123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'zhangsan', 'password': 'xiaoming123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'lisi', 'password': 'zhangsan123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'lisi', 'password': 'lisi123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'lisi', 'password': 'xiaoming123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'xiaoming', 'password': 'zhangsan123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'xiaoming', 'password': 'lisi123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'xiaoming', 'password': 'xiaoming123'}

```
测试用例(httprunner-3.x语法): [login-api-v3-parameters-cartesian.yml](../apis/login-api-v3-parameters-cartesian.yml)

```yaml


config:
    name: "login parameters cartesian v3"
    variables:
        host: "http://127.0.0.1:8888"
        status_code: 200
    parameters:
        username: ["zhangsan", "lisi", "xiaoming"]
        password: ["zhangsan123", "lisi123", "xiaoming123"]


teststeps:
-
    name: login
    request:
        method: POST
        url: "${host}/login"
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
            Content-Type: "application/x-www-form-urlencoded"
        data: "username=${username}&password=${password}"
    validate:
        - eq: ["status_code", "${status_code}"]


# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'zhangsan', 'password': 'zhangsan123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'zhangsan', 'password': 'lisi123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'zhangsan', 'password': 'xiaoming123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'lisi', 'password': 'zhangsan123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'lisi', 'password': 'lisi123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'lisi', 'password': 'xiaoming123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'xiaoming', 'password': 'zhangsan123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'xiaoming', 'password': 'lisi123'}
# {'host': 'http://127.0.0.1:8888', 'status_code': 200, 'username': 'xiaoming', 'password': 'xiaoming123'}

```
转换成.py文件: [login_api_v3_parameters_cartesian_test.py](../apis/login_api_v3_parameters_cartesian_test.py)
```python3
# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/login-api-v3-parameters-cartesian.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginApiV3ParametersCartesian(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username": ["zhangsan", "lisi", "xiaoming"],
                "password": ["zhangsan123", "lisi123", "xiaoming123"],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("login parameters cartesian v3").variables(
        **{"host": "http://127.0.0.1:8888", "status_code": 200}
    )

    teststeps = [
        Step(
            RunRequest("login")
            .post("${host}/login")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .with_data("username=${username}&password=${password}")
            .validate()
            .assert_equal("status_code", "${status_code}")
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginApiV3ParametersCartesian().test_start()

```

&nbsp;  
**重点提示**  
> 单个用例不适合参数化, 单个用例就应该是抽象好变量, 然后安静的躺在原地被调用/引用即可.  
