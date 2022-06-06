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
|`pytest --last-failed -x`|(组合参数)<br>全量用例执行完毕后, 仅重跑失败用例, <br>当出现失败用例时, 不再执行后续用例, 退出pytest.<br>当用例执行成功后, 该用例从last-failed集合中移除.<br>当用例执行失败后, 失败的和未执行的失败用例继续保留. |[测试案例](cmdlines/last-failed-with-x/main.py)|
|`pytest --stepwise`|执行全量用例时, 遇到失败用例会立即停止`pytest`程序.<br>此时`stepwise`维护了自己的缓存机制`cache/stepwise`, <br>用于标记失败用例.<br>重跑`stepwise`时, 仅重跑失败用例和后续的未执行用例.|[测试案例](cmdlines/stepwise/main.py)|
|`pytest --stepwise-skip`|执行所有用例, <br>当遇到第一个失败用例时对它进行忽略,<br>当遇到第二个失败用例时立即停止pytest程序.<br>记录当前失败位置是第二个失败用例的位置.<br><br>再次执行, 从第二个失败用例位置开始执行.<br>当再次出现第一个失败用例失败时, 忽略.<br>当再次出现第二个失败用例失败时, 立即停止pytest程序.<br>即: 永远忽略第一个失败用例.|[测试案例](cmdlines/stepwise-skip/main.py)|

