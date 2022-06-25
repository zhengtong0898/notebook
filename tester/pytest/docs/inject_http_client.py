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