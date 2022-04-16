import pytest
import pathlib
from typing import Union, List


# 1: 只能在插件中运行
# class CmdLineParse:
#
#     @pytest.hookimpl
#     def pytest_cmdline_parse(
#         pluginmanager: pytest.PytestPluginManager,
#         args: List[str]
#     ):
#         print("hello world!")


# 2: 只能在插件中运行
# @pytest.hookimpl
# def pytest_load_initial_conftests(
#     early_config: pytest.Config,
#     args: List[str],
#     parser: pytest.Parser
# ) -> None:
#     pass


# 3
def pytest_addhooks(pluginmanager: "PytestPluginManager") -> None:
    pass


# 4
def pytest_addoption(
    parser: pytest.Parser,
    pluginmanager: pytest.PytestPluginManager
) -> None:
    pass


# 5
# def pytest_plugin_registered(plugin, manager):
#     pass


# 6
def pytest_cmdline_main(config: pytest.Config):
    pass


def pytest_configure(config: "Config") -> None:
    pass


def pytest_sessionstart(session: pytest.Session):
    pass


def pytest_collection(session: pytest.Session):
    pass


# TODO: 这里没有触发.
# def pytest_ignore_collect(
#     collection_path: pathlib.Path,
#     path: "LEGACY_PATH",
#     config: pytest.Config
# ):
#     return None


def pytest_collect_file(
    file_path: pathlib.Path,
    path: "LEGACY_PATH",
    parent: pytest.Collector
):
    return None


def pytest_pycollect_makemodule(
    module_path: pathlib.Path,
    path: "LEGACY_PATH",
    parent
):
    return None


def pytest_pycollect_makeitem(
    collector: Union["Module", "Class"],
    name: str,
    obj: object
):
    return None


def pytest_generate_tests(metafunc: "Metafunc"):
    return None


# TODO: 这里没有触发.
# def pytest_make_parametrize_id(config, val, argname):
#     return None


# TODO: 这里没有触发.
# def pytest_markeval_namespace(config: pytest.Config):
#     return None


def pytest_collection_modifyitems(
    session: pytest.Session,
    config: pytest.Config,
    items: List[pytest.Item]
):
    return None


def pytest_collection_finish(session: pytest.Session):
    return None


def pytest_sessionfinish(session, exitstatus):
    pass


def pytest_unconfigure(config: pytest.Config):
    pass
