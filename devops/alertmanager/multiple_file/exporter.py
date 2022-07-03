import os
import pathlib
import time

from prometheus_client import start_http_server, Gauge, Enum


def main():
    # exporter 监听的端口
    exporter_port: int = int(os.getenv("EXPORTER_PORT", "9876"))

    # 数据采集间隔
    polling_interval_seconds: int = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))

    # 定义采集指标
    file_map = {
        "file_1": "file_1.txt",
        "file_2": "file_2.txt",
        "file_3": "file_3.txt",
    }
    file_size_metric = Gauge(
        name="file_size",
        documentation="file size metrics",
        labelnames=["file_map"]
    )

    # 启动exporter服务: prometheus可以通过ip:9876访问到采集的数据.
    start_http_server(exporter_port)

    while True:
        for k, v in file_map.items():
            # 提取数据
            metric = pathlib.Path(v).stat().st_size
            # 写入指标对象
            file_size_metric.labels(k).set(metric)
        # 数据采集间隔
        time.sleep(polling_interval_seconds)


if __name__ == '__main__':
    main()
