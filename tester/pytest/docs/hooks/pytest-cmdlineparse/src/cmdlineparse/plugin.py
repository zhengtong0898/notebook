import pytest
from typing import List


class CmdLineParse:

    @pytest.hookimpl
    def pytest_cmdline_parse(
        pluginmanager: pytest.PytestPluginManager,
        args: List[str]
    ):
        print("hello world!")
