import inspect
import pytest
from typing import List


@pytest.hookimpl
def pytest_load_initial_conftests(
    early_config: pytest.Config,
    args: List[str],
    parser: pytest.Parser
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    early_config.inicfg["log_cli"] = "true"
    early_config.inicfg["log_cli_level"] = "DEBUG"
    early_config.inicfg["log_cli_format"] = "[%(asctime)s] %(message)s"
    early_config.inicfg["log_cli_date_format"] = "%Y-%m-%d %H:%M:%S"
