### Hook-KeyboardInterrupt
重构 `KeyboardInterrupt` 异常表现.
```python
import time
import signal


def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")


# signal.SIGINT
# Default action is to raise KeyboardInterrupt on linux/mac/unix.
# 
# signal.SIGBREAK
# Default action is to raise KeyboardInterrupt on windows.
signal.signal(signal.SIGINT, handler)


def main():
    while True:
        print("sleeping...")
        time.sleep(1)

        
if __name__ == '__main__':
    main()
```
等同于
```python
import time


def handler():
    raise OSError("Couldn't open device!")


def main():
    try:
        while True:
            print("sleeping...")
            time.sleep(1)
    except KeyboardInterrupt:
        handler()


if __name__ == '__main__':
    main()
```

思考和总结:  
两种代码的效果是一样的, 但是在编码过程中它们可能有完全不同的使用场景.  
try ... except 是一种具体位置具体报错的捕获.  
signal 是一种全局式的捕获.  
