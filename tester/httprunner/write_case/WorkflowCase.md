### 流程性用例  
单接口用例应该被当做最小单元的模板, 就像写函数那样把API  
和形参定义好就可以了, 剩下的事情交给流程性用例来组织.  

&nbsp;  
&nbsp;  
**测试用例**

1. 登录
2. 添加lisi用户
3. 获取用户列表, 确认用户已添加
4. 退出


&nbsp;  
&nbsp;  
**自动化测试用例**  
根据测试用例描述, 转换成一个yml用例, 需要做这几件事情.  

1. 创建一个 [login.yml](./login.yml) 单接口用例.  
2. 创建一个 [list-users.yml](./list-users.yml) 单接口用例.
3. 创建一个 [create-user.yml](./create-user.yml) 单接口用例.  
4. 创建一个 [logout.yml](./logout.yml) 单接口用例.  
5. 创建一个 [workflow-create-user.yml](./workflow-create-user.yml) 流程用例.   


&nbsp;  
&nbsp;  
**结论:**   
在单接口用例中，封装好断言点、变量名.  
在流程用例中, 通过变量来驱动单接口用例.  

