### unittest terms(术语)
- test case(测试用例)  
  框架使用者视角:  
  &nbsp; &nbsp; &nbsp; &nbsp; `class TestCase`用来组织测试用例.  
  &nbsp; &nbsp; &nbsp; &nbsp; `TestCase.test_`前缀方法用来表示每个独立的测试用例(单元测试).  
  &nbsp; &nbsp; &nbsp; &nbsp; `TestCase.test_`多个方法在一个类中，表示它们是同一个功能模块或性质相同的用例.  
  
  框架内部视角:  
  &nbsp; &nbsp; &nbsp; &nbsp; 每个`test_`前缀的方法, 都被当作是一个独立的用例来运行, [参考这里](https://github.com/zhengtong0898/source-decode/blob/main/unittest/unittest-1.0/loader.py#L124).  
  &nbsp; &nbsp; &nbsp; &nbsp; 每个`test_`前缀的方法, 都享有共同的类方法和类生命周期方法.
  
&nbsp;  
- test fixture(测试前后装置)  
  非技术视角:   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试之前，需要先准备一些测试数据(prepare fixture),   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试完毕后, 需要清除对应的测试数据(suffix fixture).      
  
  技术视角:   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试之前，先执行 TestCase.setUpClass 方法(用于准备测试数据),   
  &nbsp; &nbsp; &nbsp; &nbsp; 执行测试完毕后, 补充执行 TestCase.tearDownClass 方法(用于清除对应的测试数据).  
  
&nbsp;  
- test suite(测试套件)  
  测试套件是一个测试用例集合, 通过`suite`可以将不同的用例组合在一起, 从而达成某个目标或任务.   
  
&nbsp;  
- test runner(测试执行器)   
  负责执行测试用力并汇总结果(默认是纯文本: `TextTestRunner` 和 `TextTestResult`)反馈给用户.    
  也可以使用第三方`runner`, 比如说: `htmltestrunner.HTMLTestRunner` 和 `htmltestrunner._TestResult`.
  
&nbsp;  
&nbsp;  
### [fixture](https://docs.pytest.org/en/stable/fixture.html#what-fixtures-are)
In the simplest terms, a test is meant to look at the result of a particular behavior, and make sure that result aligns with what you would expect. Behavior is not something that can be empirically measured, which is why writing tests can be challenging.  
> 测试就是输入一组数据, 然后断言其结果是否于预期一致.  
> 断言可以分为: 过程断言 和 结果断言.  
> 
> 过程断言: 关注其过程的表现是否符合预期;      
> &nbsp; &nbsp; &nbsp; &nbsp;例如: 一个流程性质的用例需要多个接口配合, 需要为每个接口断言一次或多次.     
> 
> 结果断言: 关注其最终结果的表现是否符合预期.  
> 
> 代码复用, 是动一发而牵全身的典型场景, 由于某个代码的改动,   
> 很多模块中的很多功能都不同程度的出现了问题.  
> 这也就是为什么软件在迭代过程中时常会出现令人不可预期的表现,  
> 自动化的回归测试(单元测试、接口测试、ui自动化测试),  
> 就是为了能在CICD过程中第一时间反映出软件的潜在问题.  

