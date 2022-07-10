### Hypothesis

**Hypothesis** 是一个`Python`库, 它是一个基于参数类型(Property-Base Testing, 简称PBT)的数据生成器, 它通过抽样式的生成常规值、边界值和极值来验证被测对象的正确性.  

- 字符串类型数据生成: 空字符、ascii、latin-1、unicode、emoji、bytes.  
- 数字类型数据生成: 0, -1, 1, max_i32, -max_i32, Nan 等情况值.  

**Hypothesis** 适用于编写单元测试用例, 可以轻松的提高代码的测试覆盖率.  

**Hypothesis** 适用于可逆场景的测试, 比如说: encode、decode、password、token、convert等.  

**Hypothesis** 和一般的单元测试用例是有差异的, 具体表现如下:  

- 常规的单元测试的表现形式  
  1). 设计一些符合特定场景的静态数据.  
  2). 对被测目标做一些操作, 达到数据或状态的改变.  
  3). 验证数据或状态是否符合预期.  


- 基于参数类型的单元测试的表现形式   
  1). 匹配某种规范的所有数据自动生成.  
  &nbsp; &nbsp; &nbsp;情况一: 无任何业务含义、无任何限制的参数类型的自动数据生成(`hypothesis.strategies`能满足).  
  &nbsp; &nbsp; &nbsp;情况二: 无任何业务含义、有限制范围的参数类型的自动数据生成(`hypothesis.strategies`能满足).  
  &nbsp; &nbsp; &nbsp;情况三: 有特定业务含义、无任何限制的参数类型的自动数据生成(`hypothesis.composite`能满足).  
  &nbsp; &nbsp; &nbsp;情况四: 有特定业务含义、有限制范围的参数类型的自动数据生成(`hypothesis.composite`能满足).  
  2). 对被测目标做一些操作, 达到数据或状态的改变.  
  3). 只能验证具有共性的数据或状态是否符合预期.  
  &nbsp; &nbsp; &nbsp;就像`schemathesis`的默认行为一样, 只对`status`返回值是不是200作为通过的断言依据.  

&nbsp;  
### 什么场景不适合使用Hypothesis?  
前面有提到可逆场景适合使用Hypothesis, 这里来说一下什么场景不适合使用Hypothesis.  
1). 根据不同的值做判断返回True或False的场景, 不适合使用Hypothesis, [案例](./anti_patterns/condition/test_case.py).  


&nbsp;  
### 参考资料  
https://www.youtube.com/watch?v=mkgd9iOiICc  
https://hypothesis.readthedocs.io/en/latest/  
https://www.inspiredpython.com/course/testing-with-hypothesis/testing-your-python-code-with-hypothesis  
https://levelup.gitconnected.com/unit-testing-in-python-property-based-testing-892a741fc119  
https://bytes.yingw787.com/posts/2021/02/02/property_based_testing/  
https://www.youtube.com/watch?v=RPprhDSD5ro&t=1365s  
https://developer.mozilla.org/en-US/docs/Glossary/Fuzzing  
https://en.wikipedia.org/wiki/Fuzzing   
https://baijiahao.baidu.com/s?id=1688756886180018558&wfr=spider&for=pc  
https://www.cnblogs.com/guanhe/p/3484343.html  
https://medium.com/clarityai-engineering/property-based-testing-a-practical-approach-in-python-with-hypothesis-and-pandas-6082d737c3ee  

