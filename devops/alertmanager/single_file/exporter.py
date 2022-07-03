import os
import pathlib
import time

from prometheus_client import start_http_server, Gauge, Enum


# exporter 监听的端口
exporter_port: int = int(os.getenv("EXPORTER_PORT", "9876"))

# 数据采集间隔
polling_interval_seconds: int = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))


def main():

    # 定义采集指标
    file_size_metric = Gauge(name="file_size", documentation="file size metrics")

    # 启动exporter服务: prometheus可以通过ip:9876访问到采集的数据.
    start_http_server(exporter_port)

    while True:
        # 提取数据
        metric = pathlib.Path("the_file.txt").stat().st_size
        # 写入指标对象
        file_size_metric.set(metric)
        # 数据采集间隔
        time.sleep(polling_interval_seconds)


if __name__ == '__main__':
    main()
