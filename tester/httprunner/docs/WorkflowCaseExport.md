### 流程性用例(导出) 
写流程性用例时, 如果涉及到分层用例且用例间存在数据依赖关系, 则需要使用`export`导出功能.  
`httprunner`提供了`export`关键字可以将`module变量`返回给父用例并作为父用例的`module变量`, 举例:  

> `export`关键字无法将`session`变量返回给父用例作为父用例的`module`变量.

API测试用例(httprunner-3.x语法): [login-export.yml](../apis/login-export.yml)  

```yaml


config:
    name: "module variable"
    desc: "这里定义的是当前API要求必填的参数"
    variables:
        host: ""
        username: ""
        password: ""
        status_code: ""
        body_status: ""
        body_msg: ""
    export:
        - body2                                                 # export module variable to outer yml

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
    variables:
        good: "good2"                                           # declare session variable
    extract:                                                    
        body2: good                                             # declare module variable
    validate:
        - eq: ["status_code", "${status_code}"]
        - eq: ["body.status", "${body_status}"]
        - eq: ["body.msg", "${body_msg}"]

```


流程性测试用例(httprunner-3.x语法): [create-user-export.yml](../testcases/create-user-export.yml)   

```yaml


config:
    name: "testcases module variable"


teststeps:
-
    name: login
    testcase: apis/login-export.yml             # 这个用例使用 export 将 body2 变量声明为是父用例的 module variable
                                                # 所以当前用例的所有步骤, 不需要做任何处理, 都可以直接使用body2变量.
    variables:
        host: "http://127.0.0.1:8888"
        username: "zhangsan"
        password: "zhangsan123"
        status_code: 200
        body_status: 200
        body_msg: "login success"

-
    name: "create user"
    request:
        method: POST
        url: "${host}/user"
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
            Content-Type: "application/x-www-form-urlencoded"
        data: "username=${username}"
    variables:
        host: "http://127.0.0.1:8888"
        username: "${body2}"                    # 这里使用子用例export出来的变量.                
        status_code: 200
        body_status: 200
        body_msg: "user ${username} create success."
    validate:
        - eq: ["status_code", "${status_code}"]
        - eq: ["body.status", "${body_status}"]
        - eq: ["body.msg", "${body_msg}"]

```
&nbsp;  
**结论:**  
导出的变量在父用例用可以直接调用, 这是从使用的角度来看是便捷的,   
但是从维护的角度来看不知道这个变量从哪里来有点莫名其妙不利于维护.  


&nbsp;  
&nbsp;  
### 父用例导出变量  
`httprunner`允许父用例直接导出子用例中的`module variable`作为当前用例的`module variable`,  
后续的步骤都可以直接使用这个变量, 从使用的角度来看是便捷的, 从维护的角度来看也是直观的.  

```yaml


config:
    name: "module variable"
    desc: "这里定义的是当前API要求必填的参数"
    variables:
        host: ""
        username: ""
        password: ""
        status_code: ""
        body_status: ""
        body_msg: ""
                                                                # remove export syntax

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
    variables:
        good: "good2"                                           # declare session variable
    extract:                                                    
        body2: good                                             # declare module variable
    validate:
        - eq: ["status_code", "${status_code}"]
        - eq: ["body.status", "${body_status}"]
        - eq: ["body.msg", "${body_msg}"]

```


流程性测试用例(httprunner-3.x语法): [create-user-export.yml](../testcases/create-user-export.yml)   

```yaml


config:
    name: "testcases module variable"


teststeps:
-
    name: login
    testcase: apis/login-export.yml             # 这个用例使用 export 将 body2 变量声明为是父用例的 module variable
                                                # 所以当前用例的所有步骤, 不需要做任何处理, 都可以直接使用body2变量.
    variables:
        host: "http://127.0.0.1:8888"
        username: "zhangsan"
        password: "zhangsan123"
        status_code: 200
        body_status: 200
        body_msg: "login success"
    export:
        - body2                                 # export module variable from subcase.

-
    name: "create user"
    request:
        method: POST
        url: "${host}/user"
        headers:
            User-Agent: HttpRunner/${get_httprunner_version()}
            Content-Type: "application/x-www-form-urlencoded"
        data: "username=${username}"
    variables:
        host: "http://127.0.0.1:8888"
        username: "${body2}"                    # 这里使用子用例export出来的变量.                
        status_code: 200
        body_status: 200
        body_msg: "user ${username} create success."
    validate:
        - eq: ["status_code", "${status_code}"]
        - eq: ["body.status", "${body_status}"]
        - eq: ["body.msg", "${body_msg}"]

```