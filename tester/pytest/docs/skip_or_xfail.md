### 当用例失败时是用skip还是xfail?  

> 参考:  
> https://docs.pytest.org/en/6.2.x/skipping.html  

当明确的知道某些平台存在限制会导致测试用例失败时, 使用`@pytest.mark.skip`.  
当明确的知道某个Bug会导致测试用例失败时, 使用`@pytest.mark.xfail`, [测试用例](./marks/test_xfail_xpass.py).    
