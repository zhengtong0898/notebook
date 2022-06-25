### 如何将http请求的入参和响应打印出来

如果习惯使用`curl`, 那么在做`requests`接口请求时, 会期望能看到原始的请求入参以及响应.  
`requests`底层采用的是`python`标准库中的`http`库, 因此在`http`标准库的关键位置注入日志打印即可.  

&nbsp;  
**/usr/lib/python3.8/http/client.py**
```python3
import logging                                                        # 在第一行增加导入logging代码

class HTTPConnection:
    
    def _send_output(self, message_body=None, encode_chunked=False):
        ...
        self.send(msg)                                                # 锁定位置: 大约在1013行的位置.
        logging.debug(f"_send_output:   message: {msg}")              # 注入日志打印代码
        ...
        
        if message_body is not None:
            ...
            for chunk in chunks:
                self.send(chunk)                                      # 锁定位置: 大概在1053行的位置.  
                logging.debug(f"_send_output: parameter: {chunk}")    # 注入日志打印代码
```

&nbsp;  
**inject_http_client.py**
```python3
import requests
import logging
from requests_toolbelt import MultipartEncoder


logging.basicConfig(level=logging.DEBUG, format="")

# 抬高urllib3的日志级别, 让它在debug级别不要打印.
logging.getLogger("urllib3").setLevel(logging.WARNING)


# 常规的json提交
resp = requests.post("https://www.baidu.com", json={"p": "computer"})
print(f"resp.content: {resp.content}")
# 输出
# _send_output:   message: b'POST / HTTP/1.1\r\nHost: www.baidu.com\r\nUser-Agent: python-requests/2.27.1\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nConnection: keep-alive\r\nContent-Length: 17\r\nContent-Type: application/json\r\n\r\n'
# _send_output: parameter: b'{"p": "computer"}'
# resp.content: 忽略结果


# 表单形式的提交
m = MultipartEncoder(fields={"hello": "world"})
resp = requests.post("https://www.baidu.com", headers={"Content-Type": m.content_type}, data=m)
print(f"resp.content: {resp.content}")
# 输出
# _send_output:   message: b'POST / HTTP/1.1\r\nHost: www.baidu.com\r\nUser-Agent: python-requests/2.27.1\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nConnection: keep-alive\r\nContent-Type: multipart/form-data; boundary=a597950ea2be4973ae6f322ee3ac6463\r\nContent-Length: 129\r\n\r\n'
# _send_output: parameter: b'--a597950ea2be4973ae6f322ee3ac6463\r\nContent-Disposition: form-data; name="hello"\r\n\r\nworld\r\n--a597950ea2be4973ae6f322ee3ac6463--\r\n'
# resp.content: 忽略结果

```
