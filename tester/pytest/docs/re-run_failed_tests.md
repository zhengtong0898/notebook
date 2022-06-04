### pytest如何重跑失败用例
失败重跑这件事是有门道的, 如果仅仅是简单的重跑失败用例, 那么`--last-failed`参数就已经足够了.  
但如果想要知道`pytest`提供了哪些情况下可以支持什么样的重跑能力, 就可以参考下面这个表格.  

|参数|描述|测试案例|
|---|---|---|
|`pytest --last-failed`|仅重跑失败用例, 不跑那些已经成功的用例.|[测试案例](cmdlines/last-failed)|
|`pytest --failed-first`|先跑失败用例, 再跑剩下的其他用例.|[测试案例](cmdlines/failed-first)|
|`pytest --failed-first --last-failed-no-failures all`|当上一次执行没有失败用例时, 执行所有用例.<br>(`--failed-first`是固定搭配)|[测试案例](cmdlines/last-failed-no-failures/main.py#L9)|
|`pytest --failed-first --last-failed-no-failures none`|当上一次执行没有失败用例时, 不执行任何用例.<br>(`--failed-first`是固定搭配)|[测试案例](cmdlines/last-failed-no-failures/main.py#L12)|
|`pytest --new-first`|按`最后修改时间`(最新的在最前面)排序来执行用例.|[测试案例](cmdlines/new-first/main.py)|
|`pytest -x`|当出现失败用例时, 不再执行后续用例, 退出pytest.|[测试案例](cmdlines/exit-immediately/main.py)|
|`pytest --stepwise`|||
|`pytest --stepwise-skip`|||

