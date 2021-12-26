### 分层用例

   
[HttpRunner 的测试用例分层机制（适用于 1.X）](https://debugtalk.com/post/HttpRunner-testcase-layer/)  
[HttpRunner 的测试用例分层机制（适用于 2.X）](https://debugtalk.com/post/HttpRunner-testcase-layer-2x/)  

&nbsp;  
**总结:**  
下面四个环节的抽象和组合, 就是所谓的分层用例.  

- 单API用例(`RunRequest`).  
   将参数抽象成变量, 交给父用例来驱动.   


- 测试用例参数化(`RunTestCase`).  
  通过提供参数清单来驱动单API的参数化.    


- 测试用例模板(`RunTestCase`).   
  将通用的步骤抽象成一个规模较小的测试用例模板, 简化父用例的编写过程.  


- 流程性测试用例(`RunTestCase`).   
  通过引用单API用例、引用测试用例模板、硬编API用例，完成测试场景的覆盖.  
