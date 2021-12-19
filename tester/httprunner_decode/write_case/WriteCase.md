

&nbsp;  
### 写用例

&nbsp;  
**测试场景-1:**

|步骤|动作|输入|期望|
|:---:|---|---|---|
|1|POST `/login`|{"username": "zhangsan", <br/>&nbsp;"password": "zhangsan123"}|登录成功|
|2|GET `/dashboard`|-|访问成功|

测试用例: [login.yml](./login.yml)




&nbsp;  
&nbsp;  
**测试场景-2:**
1. POST /login 登录失败.
2. GET /dashboard 访问失败.

|步骤|动作|输入|期望|
|:---:|---|---|---|
|1|POST `/login`|{"username": "zhangsan", <br/>&nbsp;"password": "zhangsan123"}|登录成功|
|2|GET `/dashboard`|-|访问成功|
