### 实时的日志输出
默认情况下, pytest在执行用例的过程中, 不会输出任何信息, 而是再执行完毕后统一输出.    
通过将 `log_cli` 相关的参数定义在 `pytest.init` 中, 使其支持实时的日志输出.  

```shell script
source venv/bin/activate
pytest main.py


# 输出
============================= test session starts ===========================
platform darwin -- Python 3.7.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: examples/live_logs, configfile: pytest.ini
collected 1 item                                                                                                                                                                                                                          

main.py::entrypoint 
------------------------------- live log call -------------------------------
2021-06-20 21:34:46 [    INFO] entrypoint: count: 0... (main.py:8)
2021-06-20 21:34:47 [    INFO] entrypoint: count: 1... (main.py:8)
2021-06-20 21:34:48 [    INFO] entrypoint: count: 2... (main.py:8)
2021-06-20 21:34:49 [    INFO] entrypoint: count: 3... (main.py:8)
2021-06-20 21:34:50 [    INFO] entrypoint: count: 4... (main.py:8)
2021-06-20 21:34:51 [    INFO] entrypoint: count: 5... (main.py:8)
2021-06-20 21:34:52 [    INFO] entrypoint: count: 6... (main.py:8)
2021-06-20 21:34:53 [    INFO] entrypoint: count: 7... (main.py:8)
2021-06-20 21:34:54 [    INFO] entrypoint: count: 8... (main.py:8)
2021-06-20 21:34:55 [    INFO] entrypoint: count: 9... (main.py:8)
PASSED                                                                                                                                                                                                                              [100%]

============================ 1 passed in 10.04s =============================
```