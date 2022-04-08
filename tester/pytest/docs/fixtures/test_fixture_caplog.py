import logging


def test_caplog(caplog):
    caplog.set_level(logging.INFO)                  # 设置捕获日志的管道级别
    logging.info("hello world")                     # 日志被读取到caplog对象中
    print(f"\ntest_caplog: {caplog.text}")          # 这里不是实时打印, 而是在用例结束阶段统一打印.
    assert 1 == 1
