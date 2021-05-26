### 术语
- test fixture  
  测试用例的前置和后置装置, 可以从两个视角去理解:  
  非技术视角: 执行测试之前，需要先准备一些测试数据(prepare fixture), 执行测试完毕后, 需要清除对应的测试数据(suffix fixture).    
  技术视角: 执行测试之前，先执行 TestCase.setUpClass 方法(用于准备测试数据), 执行测试完毕后, 补充执行 TestCase.tearDownClass 方法(用于清楚对应的测试数据).