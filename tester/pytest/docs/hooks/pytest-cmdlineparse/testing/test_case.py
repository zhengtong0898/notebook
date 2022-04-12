import logging


def test_main():
    """
    背景
        默认情况下 pytest 是会捕获所有的stdout和stderr输出,
        因此像 print 和 logging 这种指令是不会输出到控制台的.

        想要解决这个问题有两种方式(选任意一种都可以):
        1). 在pytest.ini中定义log_cli、log_cli_level、log_cli_format、log_cli_date_format等配置信息.
        2). 在pytest命令行带上-s参数, 表示关闭输出捕获功能, 例如: pytest -s;
        3). 前面两种是在运行前通过配置来绕过捕获, 第三种是在运行时篡改参数的方式来绕过捕获.

    测试
        当前覆盖的测试场景是3).
        在运行时 通过 pytest_load_initial_conftests hook 来篡改 early_config 对象的配置信息,
        对原本空的 early_config.inicfg 配置增加 log_cli、log_cli_level、log_cli_format、log_cli_date_format等配置信息,
        从而达到绕过捕获.
    """
    logging.debug("this is test for log2")


"""
执行:
cd notebook/tester/pytest/docs/hooks
pip install pytest-loadinitialconftests/
pytest pytest-loadinitialconftests/testing/main.py


输出结果:
============================= test session starts ==============================
collecting ... collected 1 item

main.py::test_main 
-------------------------------- live log call ---------------------------------
[2022-04-12 06:51:27] this is test for log                                         # 关键信息在这里.
PASSED                                                                   [100%]

============================== 1 passed in 0.02s ===============================
"""