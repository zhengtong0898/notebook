# 客户端获取响应数据
### socket.makefile
```python
import time
import re
import socket


def socket_makefile():
    # protocol: 'HTTP/1.1'
    # api:      '/'
    # method:   'GET'
    ss = b"GET http://192.168.1.3/ HTTP/1.1\r\n"   \
         b"Host: 192.168.1.3\r\n"                  \
         b"User-Agent: python-requests/2.25.1\r\n" \
         b"Accept-Encoding: gzip, deflate\r\n"     \
         b"Accept: */*\r\n"                        \
         b"Connection: keep-alive\r\n\r\n"

    maxline = 65535
    total_size = 0
    sock = socket.socket()
    address = ("192.168.1.3", 80)
    sock.connect(address)
    sock.sendall(ss)
    fp = sock.makefile("rb")

    # 重点:
    # fp.readline() 工作原理, 从缓存中提取内容,
    # 当遇到 '\r\n' 或 '\n' 时, 返回已读取的内容, 这段内容被视为是一行数据.
    #
    # fp.readline() 有一个 size 参数, 当提供 size 参数时, 会出现两种情况.
    # 情况一: 提供的 size 值小于 '一行' 数据.
    #        假设 size = 10; '一行'的长度 = 30;
    #        则 fp.readline(size=10) 返回的是 10 个字符长度的结果.
    #
    # 情况二: 提供的 size 值大于 '一行' 数据.
    #        假设 size = 50; '一行'的长度 = 30;
    #        则 fp.readline(size=50) 返回的是 30 个字符长度的结果,
    #        因为它遇到 '\r\n' 或 '\n' 时, 就会强行返回结果.
    #
    # 补充说明:
    # fp.readline() 如果不提供任何参数, 那么它将会一直读取(堵塞的形式),
    # 直到读取到 '\r\n' 或 '\n', 最坏的情况就是程序堵死.
    oneline = fp.readline(maxline)
    oneline = str(oneline, encoding="latin-1")
    version, status, reason = oneline.split(sep=None, maxsplit=2)

    # response headers
    headers = []
    content_length = 0
    pattern = re.compile(rb"Content-Length: (\d+)\r\n")
    while True:
        oneline = fp.readline(maxline)
        headers.append(oneline)

        matched = re.match(pattern, oneline)
        if isinstance(matched, re.Match):
            content_length = int(matched[1])

        if oneline in (b"\r\n", b"\n", b""):
            break

    if not content_length:
        return

    # response content
    while True:
        oneline = fp.readline(maxline)
        total_size += len(oneline)
        print(time.time(), len(oneline), oneline)
        if total_size >= content_length:
            break

```

&nbsp;  
&nbsp;  
### socket.recv
```shell script
import time
import re
import socket


def socket_recv():
    ss = b"GET http://192.168.1.3/ HTTP/1.1\r\n"   \
         b"Host: 192.168.1.3\r\n"                  \
         b"User-Agent: python-requests/2.25.1\r\n" \
         b"Accept-Encoding: gzip, deflate\r\n"     \
         b"Accept: */*\r\n"                        \
         b"Connection: keep-alive\r\n\r\n"

    maxline = 65535
    total_size = 0
    sock = socket.socket()
    address = ("192.168.1.3", 80)
    sock.connect(address)
    sock.sendall(ss)

    # read oneline
    def readline(size=None):
        data = b""
        while True:
            data += sock.recv(1)

            if size is not None and len(data) >= size:
                yield data

            if data[-2:] == b"\r\n" or data[-1:] == b"\n":
                yield data

    # response status
    oneline = next(readline(maxline))
    oneline = str(oneline, encoding="latin-1")
    version, status, reason = oneline.split(sep=None, maxsplit=2)

    # response headers
    headers = []
    content_length = 0
    pattern = re.compile(rb"Content-Length: (\d+)\r\n")
    while True:
        oneline = next(readline(maxline))
        headers.append(oneline)

        matched = re.match(pattern, oneline)
        if isinstance(matched, re.Match):
            content_length = int(matched[1])

        if oneline in (b"\r\n", b"\n", b""):
            break

    if not content_length:
        return

    # response content
    while True:
        oneline = next(readline(maxline))
        total_size += len(oneline)
        print(time.time(), len(oneline), oneline)
        if total_size >= content_length:
            break

```