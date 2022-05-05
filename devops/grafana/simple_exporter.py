import os
import time
import delegator
from prometheus_client import start_http_server, Gauge, Enum


class AppMetrics:

    def __init__(self, app_port=80, polling_interval_seconds=5):
        self.app_port = app_port
        self.polling_interval_seconds = polling_interval_seconds

        # Prometheus metrics to collect
        self.load_avg_1 = Gauge("load_avg_1", "Load AVG 1 minutes")

    def run_metrics_loop(self):
        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        # 获取cpu加载信息
        resp = delegator.run("awk '{print $1}' /proc/loadavg")
        load_avg_1 = resp.out.rstrip()
        self.load_avg_1.set(load_avg_1)


def main():
    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    app_port = int(os.getenv("APP_PORT", "80"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))

    app_metrics = AppMetrics(
        app_port=app_port,
        polling_interval_seconds=polling_interval_seconds
    )
    start_http_server(exporter_port)
    app_metrics.run_metrics_loop()


if __name__ == "__main__":
    main()
