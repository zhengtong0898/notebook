

&nbsp;  
### 写最小单元的用例
最小单元的用例指的是单接口用例(不含任何依赖的用例).

&nbsp;  
&nbsp;  
**测试场景-1:**   
输入正确的账号密码，预期返回200状态码.

|步骤|动作|输入|期望|
|:---:|---|---|---|
|1|POST `/login`|{"username": "zhangsan", <br/>&nbsp;"password": "zhangsan123"}|status==200|

测试用例: [login-api-success.yml](./login-api-success.yml)
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



&nbsp;  
&nbsp;  
**测试场景-2:**   
输入错误的账号密码，预期返回400状态码.

|步骤|动作|输入|期望|
|:---:|---|---|---|
|1|POST `/login`|{"username": "lisi", <br/>&nbsp;"password": "lisi123"}|status==400|

测试用例: [login-api-failed.yml](./login-api-failed.yml)
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
