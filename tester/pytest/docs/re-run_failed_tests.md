### pytest如何重跑失败用例
失败重跑这件事是有门道的, 如果仅仅是简单的重跑失败用例, 那么`--last-failed`参数就已经足够了.  
但如果想要知道更多, 那么就需要静下心、深呼吸、调整好

|参数|描述|测试案例|
|---|---|---|
|`pytest --last-failed`|仅重跑失败用例, 不跑那些已经成功的用例.|[测试案例](cmdlines/last-failed)|
|`pytest --failed-first`|先跑失败用例, 再跑剩下的其他用例.|[测试案例](cmdlines/failed-first)|
|`pytest --last-failed-no-failures all`|||
|`pytest --last-failed-no-failures none`|||
|`pytest --new-first`|||
|`pytest --stepwise`|||
|`pytest --stepwise-skip`|||
|`pytest -x`|||
