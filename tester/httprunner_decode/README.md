### httprunner框架使用

1. [安装httprunner](https://github.com/httprunner/httprunner/blob/master/docs/installation.md)  
2. [创建httprunner项目](https://github.com/httprunner/httprunner/blob/master/docs/user/scaffold.md)  
3. [前置准备工作](write_case/Prepare.md)
4. [写最小单元的用例](write_case/WriteCase.md)
5. [生成测试报告]()
6. [优化测试报告]()


### httprunner框架源码分析

1. 如果是两个用例，那`httprunner/runner.py::HttpRunner`中的`test_start`是被触发两次吗?



### 问题清单  

1. TConfig.verify 是做什么用的?
2. TRequest.verify 是不验证https的意思吗?
3. 如何访问response的值?
4. 如何访问response.headers的值?
5. 如何访问session.headers的值?
6. 如何访问session.params的值?
7. 如何访问session.body的值?
8. 如何访问session对象?
9. 运行结果保存在哪里?