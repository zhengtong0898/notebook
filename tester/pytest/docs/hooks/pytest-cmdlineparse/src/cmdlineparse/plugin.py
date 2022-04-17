import inspect
import pytest
from typing import List


class CmdLineParse:

    @pytest.hookimpl
    def pytest_cmdline_parse(
        pluginmanager: pytest.PytestPluginManager,
        args: List[str]
    ):
        print(f"{inspect.currentframe().f_code.co_name}")
