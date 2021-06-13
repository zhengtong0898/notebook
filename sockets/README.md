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

    maxline = 65536
    sock = socket.socket()
    address = ("192.168.1.3", 80)
    sock.connect(address)
    sock.sendall(ss)
    fp = sock.makefile("rb")
    total_size = 0

    # response status
    oneline = fp.readline(maxline + 1)
    oneline = str(oneline, encoding="latin-1")
    version, status, reason = oneline.split(sep=None, maxsplit=2)
    total_size += len(oneline)

    # response headers
    headers = []
    content_length = 0
    pattern = re.compile(rb"Content-Length: (\d+)\r\n")
    while True:
        oneline = fp.readline(maxline + 1)
        headers.append(oneline)
        total_size += len(oneline)

        matched = re.match(pattern, oneline)
        if isinstance(matched, re.Match):
            content_length = int(matched[1])

        if oneline in (b"\r\n", b"\n", b""):
            break

    if not content_length:
        return

    # response content
    while True:
        oneline = fp.readline(65536)
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

    total_size = 0
    sock = socket.socket()
    address = ("192.168.1.3", 80)
    sock.connect(address)
    sock.sendall(ss)

    # read oneline
    def readline():
        data = b""
        while True:
            data += sock.recv(1)
            if data[-2:] == b"\r\n" or data[-1:] == b"\n":
                yield data

    # response status
    oneline = next(readline())
    oneline = str(oneline, encoding="latin-1")
    version, status, reason = oneline.split(sep=None, maxsplit=2)

    # response headers
    headers = []
    content_length = 0
    pattern = re.compile(rb"Content-Length: (\d+)\r\n")
    while True:
        oneline = next(readline())
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
        oneline = next(readline())
        total_size += len(oneline)
        print(time.time(), len(oneline), oneline)
        if total_size >= content_length:
            break

```