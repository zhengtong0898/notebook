### 流程性用例(提取) 
写流程性用例时避免不了步骤和步骤之间会产生依赖, 也就是说下一个步骤必须依赖当前步骤的返回数据才能执行.  
`httprunner`提供了`extract`关键字可以将`session变量`声明为`modulel变量`, 举例:  

测试用例: 

```yaml


config:
    name: "testcases module variable"


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
        host: "http://127.0.0.1:8888"
        username: "zhangsan"
        password: "zhangsan123"
        status_code: 200
        body_status: 200
        body_msg: "login success"
    extract:                                      # 将值提取出来, 赋给foo变量.
        foo: "body.msg"                           # 此时foo变量是一个module变量, 下一个API用例可见.    
    validate:
        - eq: ["status_code", "${status_code}"]
        - eq: ["body.status", "${body_status}"]
        - eq: ["body.msg", "${body_msg}"]

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
        username: "${foo}"                        # 当前API用例可调用foo变量.  
        status_code: 200
        body_status: 200
        body_msg: "user ${username} create success."
    validate:
        - eq: ["status_code", "${status_code}"]
        - eq: ["body.status", "${body_status}"]
        - eq: ["body.msg", "${body_msg}"]

```



> **备注**  
> 上面的样例代码, 两个单接口API串联在一起, 这种是典型的非引用案例,   
> 即: 不是分层结构, 不具备复用能力.  
> 
> `httprunner`为这种串联硬编用例提供了将`本地变量`声明为`模块变量`的能力.  
> 在同一个用例文件内, `模块变量`对于所有的步骤来说都是可见的.  
>
> 需要注意的是:   
> 如果存在分层情况, 则模块变量在父层是不可见的, 只有将变量`export`出去后父层就可见了.  
