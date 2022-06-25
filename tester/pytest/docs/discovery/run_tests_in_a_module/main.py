import pytest


"""
在Python和pytest中, 一个py文件就是一个模块(module), 它们是同一个含义没有歧义.

Pytest是如何发现测试用例的?
1. pytest根据提供的路径去加载文件.
2. pytest根据<module test_case.py>.__dict__加载得到两个测试用例方法. 
   (_pytest.python.PyCollector.collect.obj.__dict__)  
3. pytest将测试用例函数封装到FunctionDefinition对象, 该对象的目的是用来存放该函数的相关信息, 例如:
   1). 该函数归属于哪个session, 隐藏信息是可以使用哪些fixture.
   2). 该函数使用了哪些fixtures, 记录在fixturenames属性中.
   3). 该函数的绝对路径, 记录在path属性中.
   4). 该函数的唯一别名, 记录在nodeid属性中.  
   5). 该函数的代码位置, 记录在location属性中.  
   6). 该函数的实际参数, 记录在funcargs属性中.
4. pytest将FunctionDefinition对象封装到Metafunc对象, Metafunc对象用于保存参数化信息.
   当参数化存在时, pytest会生成一组FunctionDefinition对象并返回给执行层.  
"""


if __name__ == '__main__':
    # 运行一个模块(文件)中的所有测试用力.
    pytest.main(["sss/test_case.py"])               # 等同于: pytest sss/test_case.py
