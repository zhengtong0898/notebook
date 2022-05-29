### pytest内置的fixture清单

|fixture|插件|路径|文档介绍|
|---|---|---|---|
|cache|内置|_pytest/cacheprovider.py:510|Return a cache object that can persist state between testing sessions.|
|capsys|内置|_pytest/capture.py:878|Enable text capturing of writes to ``sys.stdout`` and ``sys.stderr``.|
|capsysbinary|内置|_pytest/capture.py:895|Enable bytes capturing of writes to ``sys.stdout`` and ``sys.stderr``.|
|capfd|内置|_pytest/capture.py:912|Enable text capturing of writes to file descriptors ``1`` and ``2``.|
|capfdbinary|内置|_pytest/capture.py:929|Enable bytes capturing of writes to file descriptors ``1`` and ``2``.|
|doctest_namespace<br>[session scope]|内置|_pytest/doctest.py:731|Fixture that returns a :py:class:`dict` that will be injected into the namespace of doctests.|
|pytestconfig|内置|_pytest/fixtures.py:1334|Session-scoped fixture that returns the session's :class:`pytest.Config` object.|
|record_property|内置|_pytest/junitxml.py:282|Add extra properties to the calling test.|
|record_xml_attribute|内置|_pytest/junitxml.py:305|Add extra xml attributes to the tag for the calling test.|
|record_testsuite_property<br>[session scope]|内置|_pytest/junitxml.py:343|Record a new ``<property>`` tag as child of the root ``<testsuite>``.|
|tmpdir_factory|内置|_pytest/legacypath.py:295|Return a :class:`pytest.TempdirFactory` instance for the test session.|
|tmpdir|内置|pytest/legacypath.py:302|Return a temporary directory path object which is unique to each test <br>function invocation, created as a sub directory of the base temporary directory.|
|caplog|内置|_pytest/logging.py:487|Access and control log capturing.|
|monkeypatch|内置|_pytest/monkeypatch.py:29|A convenient fixture for monkey-patching.|
|recwarn|内置|_pytest/recwarn.py:29|Return a :class:`WarningsRecorder` instance that records all warnings emitted by test functions.|
|tmp_path_factory<br>[session scope]|内置|_pytest/tmpdir.py:183|Return a :class:`pytest.TempPathFactory` instance for the test session.|
|tmp_path|内置|_pytest/tmpdir.py:198|Return a temporary directory path object which is unique to each test <br>function invocation, created as a sub directory of the base temporary directory.|
|worker_id|xdist|xdist/plugin.py:290|Return the id of the current worker ('gw0', 'gw1', etc) or 'master'<br>if running on the master node.|
|testrun_uid|xdist|xdist/plugin.py:299|Return the unique id of the current test.|

&nbsp;  
### 命令行查看
`pytest`提供了命令行参数, 可以打印出当前目录下有效的fixture清单.  
```shell
$ pytest --fixtures
=================================================== test session starts ===============================================
platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-0.13.1
rootdir: /home/zt/Desktop
plugins: xdist-2.5.0, allure-pytest-2.9.45, loadinitialconftests-0.0.0, cmdlineparse-0.0.0, forked-1.4.0
collected 0 items                                                                                                         
cache -- .../_pytest/cacheprovider.py:510
    Return a cache object that can persist state between testing sessions.

capsys -- .../_pytest/capture.py:878
    Enable text capturing of writes to ``sys.stdout`` and ``sys.stderr``.

capsysbinary -- .../_pytest/capture.py:895
    Enable bytes capturing of writes to ``sys.stdout`` and ``sys.stderr``.

capfd -- .../_pytest/capture.py:912
    Enable text capturing of writes to file descriptors ``1`` and ``2``.

capfdbinary -- .../_pytest/capture.py:929
    Enable bytes capturing of writes to file descriptors ``1`` and ``2``.

doctest_namespace [session scope] -- .../_pytest/doctest.py:731
    Fixture that returns a :py:class:`dict` that will be injected into the
    namespace of doctests.

pytestconfig [session scope] -- .../_pytest/fixtures.py:1334
    Session-scoped fixture that returns the session's :class:`pytest.Config`
    object.

record_property -- .../_pytest/junitxml.py:282
    Add extra properties to the calling test.

record_xml_attribute -- .../_pytest/junitxml.py:305
    Add extra xml attributes to the tag for the calling test.

record_testsuite_property [session scope] -- .../_pytest/junitxml.py:343
    Record a new ``<property>`` tag as child of the root ``<testsuite>``.

tmpdir_factory [session scope] -- .../_pytest/legacypath.py:295
    Return a :class:`pytest.TempdirFactory` instance for the test session.

tmpdir -- .../_pytest/legacypath.py:302
    Return a temporary directory path object which is unique to each test
    function invocation, created as a sub directory of the base temporary
    directory.

caplog -- .../_pytest/logging.py:487
    Access and control log capturing.

monkeypatch -- .../_pytest/monkeypatch.py:29
    A convenient fixture for monkey-patching.

recwarn -- .../_pytest/recwarn.py:29
    Return a :class:`WarningsRecorder` instance that records all warnings emitted by test functions.

tmp_path_factory [session scope] -- .../_pytest/tmpdir.py:183
    Return a :class:`pytest.TempPathFactory` instance for the test session.

tmp_path -- .../_pytest/tmpdir.py:198
    Return a temporary directory path object which is unique to each test
    function invocation, created as a sub directory of the base temporary
    directory.


------------------------------------------- fixtures defined from xdist.plugin ----------------------------------------
worker_id [session scope] -- ../PycharmProjects/learn_staff/venv/lib/python3.8/site-packages/xdist/plugin.py:290
    Return the id of the current worker ('gw0', 'gw1', etc) or 'master'
    if running on the master node.

testrun_uid [session scope] -- ../PycharmProjects/learn_staff/venv/lib/python3.8/site-packages/xdist/plugin.py:299
    Return the unique id of the current test.


================================================== no tests ran in 0.01s ==============================================
pytest_load_initial_conftests

```
