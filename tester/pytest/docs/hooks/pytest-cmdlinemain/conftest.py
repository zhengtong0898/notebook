import pytest


def pytest_cmdline_main(config: pytest.Config):
    print(config)
