### pytest如何发现一个目录中的测试用例

1. 在`pytest.main()`的实现(入口)函数中, `config = _prepareconfig(args, plugins)` 负责处理参数和路径收集.  
   
```python3
# _pytest/config/__init__.py
def get_config(
    args: Optional[List[str]] = None,
    plugins: Optional[Sequence[Union[str, _PluggyPlugin]]] = None,
) -> "Config":
    # subsequent calls to main will create a fresh instance
    pluginmanager = PytestPluginManager()                # 初始化pluginmanager

    config = Config(                                     # 初始化 config 对象.
        pluginmanager,                                   # 将pluginmanager对象聚合到config对象中.
        invocation_params=Config.InvocationParams(       # 处理参数对象
            args=args or (),                             # 编程入口pytest.main提供的运行时参数.  
            plugins=plugins,                             # 编程入口pytest.main提供的plugins对象.
            dir=Path.cwd(),                              # 获取当前路径
        ),
    )

    if args is not None:
        # Handle any "-p no:plugin" args.
        pluginmanager.consider_preparse(args, exclude_only=True)

    for spec in default_plugins:                         # 导入预先准备好的plugins
        pluginmanager.import_plugin(spec)

    return config
```

2. 在`Session.collect`方法中遍历指定目录下的所有文件, 提取测试用例代码文件.
   当文件名符合`['test_*.py', '*_test.py', '__init__.py']`正则规则时， 表示该文件是一个有效的测试用例文件.
```python3
# _pytest/main.py
class Session:
    
    ...
    
    def collect(self) -> Iterator[Union[nodes.Item, nodes.Collector]]:
        from _pytest.python import Package

        # node_cache1: key是 __init__.py 路径, value是List[<Package 目录>] 对象.
        # node_cache2: key是 (type(<Module 文件名>), str), value是<Module 文件名> 对象
        # 这两个变量的目的去将文件区分是模块还是包, 不同的对象会作用不同scope的fixture.
        node_cache1: Dict[Path, Sequence[nodes.Collector]] = {}
        node_cache2: Dict[Tuple[Type[nodes.Collector], Path], nodes.Collector] = {}

        # 由于这两个变量是暂不追溯这两个变量的作用.
        matchnodes_cache: Dict[Tuple[Type[nodes.Collector], str], CollectReport] = {}
        pkg_roots: Dict[str, Package] = {}

        # self._initial_parts: 多个目录参数(从config.invocation_param里面取).
        for argpath, names in self._initial_parts:
            self.trace("processing argument", (argpath, names))
            self.trace.root.indent += 1

            # doctestmodules 配置参数为True时, 表示需要执行以文档形式编写的测试用例.
            # doctestmodules 配置参数为False时, 表示不需要执行以文档形式编写的测试用例.  
            # 这里的条件句的含义是: 当未开启doctestmodules参数时, 执行条件句内的代码块.  
            if not self.config.getoption("doctestmodules", False):
                pm = self.config.pluginmanager
                for parent in (argpath, *argpath.parents):
                    if not pm._is_in_confcutdir(argpath):
                        break

                    # 如果指定的目录中包含__init__.py则表示这个目录是一个Package对象.
                    # 将这个Package对象存储在 node_cache1 变量(集合)中.
                    if parent.is_dir():
                        pkginit = parent / "__init__.py"
                        if pkginit.is_file() and pkginit not in node_cache1:
                            col = self._collectfile(pkginit, handle_dupes=False)
                            if col:
                                if isinstance(col[0], Package):
                                    pkg_roots[str(parent)] = col[0]
                                node_cache1[col[0].path] = [col[0]]

            # 当指定的路径是一个目录时, 这个条件块代码生效.
            if argpath.is_dir():
                assert not names, f"invalid arg {(argpath, names)!r}"

                seen_dirs: Set[Path] = set()
                for direntry in visit(str(argpath), self._recurse):
                    if not direntry.is_file():
                        continue

                    path = Path(direntry.path)
                    dirpath = path.parent

                    # 当指定的目录是一个Package对象时, 不收集该目录下的测试用例.
                    if dirpath not in seen_dirs:
                        # Collect packages first.
                        seen_dirs.add(dirpath)
                        pkginit = dirpath / "__init__.py"
                        if pkginit.exists():
                            for x in self._collectfile(pkginit):
                                yield x
                                if isinstance(x, Package):
                                    pkg_roots[str(dirpath)] = x
                    if str(dirpath) in pkg_roots:
                        # Do not collect packages here.
                        continue

                    # self._collectfile(path) 做了一件重要的事情: 遍历指定目录下的所有文件.
                    # 触发 _pytest/python.py 的 pytest_collect_file 钩子函数, 该函数
                    # 通过正则匹配['test_*.py', '*_test.py', '__init__.py'],
                    # 如果文件名满足这个正则匹配, 则将该文件封装成<Module>对象.
                    for x in self._collectfile(path):
                        key2 = (type(x), x.path)
                        if key2 in node_cache2:
                            yield node_cache2[key2]
                        else:
                            node_cache2[key2] = x
                            yield x

            # 当指定的路径是一个文件时, 这个条件块代码生效.
            else:
                assert argpath.is_file()

                if argpath in node_cache1:
                    col = node_cache1[argpath]
                else:
                    collect_root = pkg_roots.get(str(argpath.parent), self)
                    col = collect_root._collectfile(argpath, handle_dupes=False)
                    if col:
                        node_cache1[argpath] = col

                matching = []
                work: List[
                    Tuple[Sequence[Union[nodes.Item, nodes.Collector]], Sequence[str]]
                ] = [(col, names)]
                while work:
                    self.trace("matchnodes", col, names)
                    self.trace.root.indent += 1

                    matchnodes, matchnames = work.pop()
                    for node in matchnodes:
                        if not matchnames:
                            matching.append(node)
                            continue
                        if not isinstance(node, nodes.Collector):
                            continue
                        key = (type(node), node.nodeid)
                        if key in matchnodes_cache:
                            rep = matchnodes_cache[key]
                        else:
                            rep = collect_one_node(node)
                            matchnodes_cache[key] = rep
                        if rep.passed:
                            submatchnodes = []
                            for r in rep.result:
                                # TODO: Remove parametrized workaround once collection structure contains
                                # parametrization.
                                if (
                                    r.name == matchnames[0]
                                    or r.name.split("[")[0] == matchnames[0]
                                ):
                                    submatchnodes.append(r)
                            if submatchnodes:
                                work.append((submatchnodes, matchnames[1:]))
                        else:
                            # Report collection failures here to avoid failing to run some test
                            # specified in the command line because the module could not be
                            # imported (#134).
                            node.ihook.pytest_collectreport(report=rep)

                    self.trace("matchnodes finished -> ", len(matching), "nodes")
                    self.trace.root.indent -= 1

                if not matching:
                    report_arg = "::".join((str(argpath), *names))
                    self._notfound.append((report_arg, col))
                    continue

                # If __init__.py was the only file requested, then the matched
                # node will be the corresponding Package (by default), and the
                # first yielded item will be the __init__ Module itself, so
                # just use that. If this special case isn't taken, then all the
                # files in the package will be yielded.
                if argpath.name == "__init__.py" and isinstance(matching[0], Package):
                    try:
                        yield next(iter(matching[0].collect()))
                    except StopIteration:
                        # The package collects nothing with only an __init__.py
                        # file in it, which gets ignored by the default
                        # "python_files" option.
                        pass
                    continue

                yield from matching

            self.trace.root.indent -= 1
```