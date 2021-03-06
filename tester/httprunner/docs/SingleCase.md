
&nbsp;  
### 单接口用例
最小单元的用例指的是单接口用例(不含任何依赖的用例).

&nbsp;  
&nbsp;  
**测试场景-1:**   
输入正确的账号密码，预期返回200状态码.

|步骤|动作|输入|期望|
|:---:|---|---|---|
|1|POST `/login`|{"username": "zhangsan", <br/>&nbsp;"password": "zhangsan123"}|status==200|

测试用例(httprunner-2.x语法): [login-api-v2-success.yml](../apis/login-api-v2-success.yml)
```yaml


name: login
request:
    method: POST
    url: http://127.0.0.1:8888/login
    headers:
        User-Agent: HttpRunner/${get_httprunner_version()}
        Content-Type: "application/x-www-form-urlencoded"
    data: "username=zhangsan&password=zhangsan123"
validate:
    - eq: ["status_code", 200]
    - eq: ["body.status", 200]
    - eq: ["body.msg", "login success"]

```

测试用例(httprunner-3.x语法): [login-api-v3-success.yml](../apis/login-api-v3-success.yml)

```yaml


config:
    name: "login module variable"


teststeps:
-
    name: login
    request:
        method: POST
        url: http://127.0.0.1:8888/login
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
            Content-Type: "application/x-www-form-urlencoded"
        data: "username=zhangsan&password=zhangsan123"
    validate:
        - eq: ["status_code", 200]
        - eq: ["body.status", 200]
        - eq: ["body.msg", "login success"]

```



&nbsp;  
&nbsp;  
**测试场景-2:**   
输入错误的账号密码，预期返回400状态码.

|步骤|动作|输入|期望|
|:---:|---|---|---|
|1|POST `/login`|{"username": "lisi", <br/>&nbsp;"password": "lisi123"}|status==400|

测试用例(httprunner-2.x语法): [login-api-v2-failed.yml](../apis/login-api-v2-failed.yml)
```yaml


name: login
request:
    method: POST
    url: http://127.0.0.1:8888/login
    headers:
        User-Agent: HttpRunner/${get_httprunner_version()}
        Content-Type: "application/x-www-form-urlencoded"
    data: "username=lisi&password=lisi123"
validate:
    - eq: ["status_code", 200]
    - eq: ["body.status", 400]
    - eq: ["body.msg", "login error"]

```

测试用例(httprunner-3.x语法): [login-api-v3-failed.yml](../apis/login-api-v3-failed.yml)

```yaml


config:
    name: "login v3"


teststeps:
-
    name: login
    request:
        method: POST
        url: http://127.0.0.1:8888/login
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
            Content-Type: "application/x-www-form-urlencoded"
        data: "username=lisi&password=lisi123"
    validate:
        - eq: ["status_code", 200]
        - eq: ["body.status", 400]
        - eq: ["body.msg", "login error"]

```


&nbsp;  
&nbsp;  
**测试场景-3:**   
`测试场景-1`和`测试场景-2`采取的策略是按实际值来硬编测试用例.  
当前场景采取的策略是将可变部分抽象出来, 使其升华为一个测试用例模板,  
将下面yml文件转换成代码的话, 它就如同定义了一个 login-api-variables-local 函数,    
这个函数要求提供6个参数, 同时这个函数为每个参数提供了默认值, 所以不提供参数也能运行.  



测试用例(httprunner-2.x语法): [login-api-v2-variables-local.yml](../apis/login-api-v2-variables-local.yml)  
```yaml

name: login
variables:
    host: "http://127.0.0.1:8888"
    username: "zhangsan"
    password: "zhangsan123"
    status_code: 200
    body_status: 200
    body_msg: "login success"
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
测试用例(httprunner-3.x语法): [login-api-v3-variables-local.yml](../apis/login-api-v3-variables-local.yml)  
```yaml


config:
    name: "login v3"


teststeps:
-
    name: login
    variables:
        host: "http://127.0.0.1:8888"
        username: "zhangsan"
        password: "zhangsan123"
        status_code: 200
        body_status: 200
        body_msg: "login success"
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


&nbsp;  
&nbsp;  
**测试场景-4:**   
将本地变量换成模块变量   
这个例子的例子在 httprunner-v3.1.6 版本中是无法运行的,   
我提了个 [Bug](https://github.com/httprunner/httprunner/issues/1137) 并附上了一个 [Fix PR](https://github.com/httprunner/httprunner/pull/1138) 来解决这个问题.  

测试用例: [login-api-v2-variables-module.yml](../apis/login-api-v2-variables-module.yml)

```yaml

config:
    name: "module variable"
    variables:
        host: "http://127.0.0.1:8888"
        username: "zhangsan"
        password: "zhangsan123"
        status_code: 200
        body_status: 200
        body_msg: "login success"


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

测试用例: [login-api-v3-variables-module.yml](../apis/login-api-v3-variables-module.yml)

```yaml


config:
    name: "module variable"
    variables:
        host: "http://127.0.0.1:8888"
        username: "zhangsan"
        password: "zhangsan123"
        status_code: 200
        body_status: 200
        body_msg: "login success"


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


&nbsp;  
**重点提示**  
> 单个用例不适合参数化, 单个用例就应该是抽象好变量, 然后安静的躺在原地被调用/引用即可.  


&nbsp;  
**总结**   
httprunner提供了variables让用例可以升华成测试模板.   
硬编测试用例, 不如将测试用例制作成模板.   
