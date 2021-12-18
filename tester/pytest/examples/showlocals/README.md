### 异常时打函数本地变量值
关键词: `--showlocals`
```shell script
source venv/bin/activate
pytest --showlocals main.py



# 输出
============================ test session starts ============================
platform darwin -- Python 3.7.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: examples/showlocals, configfile: pytest.ini
collected 1 item                                                                                                                                                                                                                          

main.py::entrypoint 
------------------------------- live log call -------------------------------
2021-06-20 21:53:29 [    INFO] entrypoint: count: 0... (main.py:9)
2021-06-20 21:53:30 [    INFO] entrypoint: count: 1... (main.py:9)
2021-06-20 21:53:31 [    INFO] entrypoint: count: 2... (main.py:9)
2021-06-20 21:53:32 [    INFO] entrypoint: count: 3... (main.py:9)
2021-06-20 21:53:33 [    INFO] entrypoint: count: 4... (main.py:9)
2021-06-20 21:53:34 [    INFO] entrypoint: count: 5... (main.py:9)
2021-06-20 21:53:35 [    INFO] entrypoint: count: 6... (main.py:9)
2021-06-20 21:53:36 [    INFO] entrypoint: count: 7... (main.py:9)
2021-06-20 21:53:37 [    INFO] entrypoint: count: 8... (main.py:9)
2021-06-20 21:53:38 [    INFO] entrypoint: count: 9... (main.py:9)
FAILED                                                                                                                                                                                                                              [100%]

================================= FAILURES ==================================
________________________________ entrypoint _________________________________

    def entrypoint():
        count = 0
        while count < 10:
            temp_var = {"temp": "var"}
            logging.info(f"entrypoint: count: {count}...")
            count += 1
            time.sleep(1)
>       aa(count)

count      = 10
temp_var   = {'temp': 'var'}

main.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
main.py:18: in aa
    bb(variable_b, variable_c)
        variable_a = 10
        variable_b = {'hello': 'world'}
        variable_c = ('godw', 'pppp')
main.py:22: in bb
    cc(vc)
        vb         = {'hello': 'world'}
        vc         = ('godw', 'pppp')
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

final = ('godw', 'pppp')

    def cc(final):
>       assert final == 1
E       AssertionError: assert ('godw', 'pppp') == 1
E         +('godw', 'pppp')
E         -1

final      = ('godw', 'pppp')

main.py:26: AssertionError
----------------------------- Captured log call -----------------------------
INFO     root:main.py:9 entrypoint: count: 0...
INFO     root:main.py:9 entrypoint: count: 1...
INFO     root:main.py:9 entrypoint: count: 2...
INFO     root:main.py:9 entrypoint: count: 3...
INFO     root:main.py:9 entrypoint: count: 4...
INFO     root:main.py:9 entrypoint: count: 5...
INFO     root:main.py:9 entrypoint: count: 6...
INFO     root:main.py:9 entrypoint: count: 7...
INFO     root:main.py:9 entrypoint: count: 8...
INFO     root:main.py:9 entrypoint: count: 9...
========================== short test summary info ==========================
FAILED main.py::entrypoint - AssertionError: assert ('godw', 'pppp') == 1
============================ 1 failed in 10.08s =============================
```