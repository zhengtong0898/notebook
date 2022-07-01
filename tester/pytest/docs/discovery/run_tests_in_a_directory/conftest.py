from pathlib import Path
from _pytest import nodes


def pytest_collect_file(file_path: Path, parent: nodes.Collector):
    print("sss")
