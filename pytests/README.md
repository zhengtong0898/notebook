### 术语
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
  测试套件是一个测试用例集合, 通过`suite`可以将不同的用例组合在一起, 从而达成某个目标或任务。  
