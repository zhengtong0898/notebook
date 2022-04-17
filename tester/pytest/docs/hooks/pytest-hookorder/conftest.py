import pytest
import pathlib
import inspect
from typing import Union, List, Optional, Tuple, Sequence, Mapping, Dict, Any


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


def pytest_addhooks(pluginmanager: "PytestPluginManager") -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


def pytest_addoption(
    parser: pytest.Parser,
    pluginmanager: pytest.PytestPluginManager
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


def pytest_plugin_registered(plugin, manager):
    print(f"{inspect.currentframe().f_code.co_name}: {plugin}")
    pass


def pytest_cmdline_main(config: pytest.Config):
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


def pytest_configure(config: "Config") -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


def pytest_sessionstart(session: pytest.Session):
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


def pytest_collection(session: pytest.Session):
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


def pytest_collectstart(
    collector: pytest.Collector
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_make_collect_report(
    collector: pytest.Collector
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_collect_file(
    file_path: pathlib.Path,
    path: "LEGACY_PATH",
    parent: pytest.Collector
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_pycollect_makemodule(
    module_path: pathlib.Path,
    path: "LEGACY_PATH",
    parent
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_collectreport(
    report: pytest.CollectReport
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_pycollect_makeitem(
    collector: Union["Module", "Class"],
    name: str,
    obj: object
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_generate_tests(metafunc: "Metafunc"):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_itemcollected(
    item: pytest.Item
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_collection_modifyitems(
    session: pytest.Session,
    config: pytest.Config,
    items: List[pytest.Item]
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_report_collectionfinish(
    config: "Config",
    start_path: pathlib.Path,
    startdir: "LEGACY_PATH",
    items: Sequence["Item"],
) -> Union[str, List[str]]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return ""


def pytest_collection_finish(session: pytest.Session):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtestloop(session: pytest.Session):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtest_protocol(
    item: pytest.Item,
    nextitem: Optional[pytest.Item]
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtest_logstart(
    nodeid: str,
    location: Tuple[str, Optional[int], str]
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtest_setup(
    item: pytest.Item
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtest_makereport(
    item: "Item",
    call: "CallInfo[None]"
) -> Optional["TestReport"]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_report_teststatus(
    report: Union["CollectReport", "TestReport"],
    config: "Config"
) -> Tuple[str, str, Union[str, Mapping[str, bool]]]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return ("", "", "")


def pytest_runtest_logreport(
    report: "TestReport"
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtest_call(
    item: pytest.Item
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_pyfunc_call(
    pyfuncitem: "Function"
) -> Optional[object]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtest_teardown(
    item: pytest.Item,
    nextitem: Optional[pytest.Item]
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_runtest_logfinish(
    nodeid: str,
    location: Tuple[str, Optional[int], str]
):
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


def pytest_sessionfinish(session, exitstatus):
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


def pytest_unconfigure(config: pytest.Config):
    print(f"{inspect.currentframe().f_code.co_name}")
    pass


# TODO: 这里没有触发.
def pytest_ignore_collect(
    collection_path: pathlib.Path,
    path: "LEGACY_PATH",
    config: pytest.Config
):
    return None


# TODO: 这里没有触发.
def pytest_make_parametrize_id(config, val, argname):
    return None


# TODO: 这里没有触发.
def pytest_markeval_namespace(config: pytest.Config):
    return None


# TODO: 这里没有触发.
def pytest_deselected(
        items: Sequence["Item"]
) -> None:
    return None


# TODO: 这里没有触发.
def pytest_report_header(
    config: "Config", start_path: pathlib.Path, startdir: "LEGACY_PATH"
) -> Union[str, List[str]]:
    return ""


# TODO: 这里没有触发.
def pytest_report_to_serializable(
    config: "Config",
    report: Union["CollectReport", "TestReport"],
) -> Optional[Dict[str, Any]]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_report_from_serializable(
    config: "Config",
    data: Dict[str, Any],
) -> Optional[Union["CollectReport", "TestReport"]]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_terminal_summary(
    terminalreporter: "TerminalReporter",
    exitstatus: "ExitCode",
    config: "Config",
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_fixture_setup(
    fixturedef: "FixtureDef[Any]", request: "SubRequest"
) -> Optional[object]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_fixture_post_finalizer(
    fixturedef: "FixtureDef[Any]", request: "SubRequest"
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_warning_recorded(
    warning_message: "warnings.WarningMessage",
    when: "Literal['config', 'collect', 'runtest']",
    nodeid: str,
    location: Optional[Tuple[str, int, str]],
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_assertrepr_compare(
    config: "Config", op: str, left: object, right: object
) -> Optional[List[str]]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_assertion_pass(
    item: "Item",
    lineno: int,
    orig: str,
    expl: str
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_internalerror(
    excrepr: "ExceptionRepr",
    excinfo: "ExceptionInfo[BaseException]",
) -> Optional[bool]:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_keyboard_interrupt(
    excinfo: "ExceptionInfo[Union[KeyboardInterrupt, Exit]]",
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_exception_interact(
    node: Union["Item", "Collector"],
    call: "CallInfo[Any]",
    report: Union["CollectReport", "TestReport"],
) -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_enter_pdb(config: "Config", pdb: "pdb.Pdb") -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None


# TODO: 这里没有触发.
def pytest_leave_pdb(config: "Config", pdb: "pdb.Pdb") -> None:
    print(f"{inspect.currentframe().f_code.co_name}")
    return None
