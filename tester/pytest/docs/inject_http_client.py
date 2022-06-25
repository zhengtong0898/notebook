import requests
import logging


logging.basicConfig(level=logging.DEBUG, format="")

# 抬高urllib3的日志级别, 让它在debug级别不要打印.
logging.getLogger("urllib3").setLevel(logging.WARNING)


resp = requests.post("https://www.baidu.com", json={"p": "computer"})
print(f"resp.content: {resp.content}")
