
### PluginManager 类对象的介绍  

**PluginManager**是一个插件管理类, 主要的作用是 `添加接口规范`、`注册插件(增)`、`移除插件(删)`、`获取插件(查)`、`执行插件`.  

`接口规范`: *PluginManager.add_hookspecs* 将会`self.hook: _HookRelay`对象中创建具体的方法`_HookCaller`规范.  
`注册插件`: *PluginManager.register* 将所有的`实现`写入到对应的`_HookCaller.wrappers`列表中, 关系是1：N.  
`移除插件`: *PluginManager.unregister* 将所有的`实现`从`_HookCaller.wrappers`列表中移除.  
`获取插件`: *get_plugins*、*get_plugin*、*is_registered*、*has_plugin*、*parse_hookspec_opts*、*parse_hookimpl_opts*.  
`执行插件`: *PluginManager._hookexec* 执行`所有规范`下的所有`实现`.   

```python3
class PluginManager:
    """Core :py:class:`.PluginManager` class which manages registration
    of plugin objects and 1:N hook calling.

    You can register new hooks by calling :py:meth:`add_hookspecs(module_or_class)
    <.PluginManager.add_hookspecs>`.
    You can register plugin objects (which contain hooks) by calling
    :py:meth:`register(plugin) <.PluginManager.register>`.  The :py:class:`.PluginManager`
    is initialized with a prefix that is searched for in the names of the dict
    of registered plugin objects.

    For debugging purposes you can call :py:meth:`.PluginManager.enable_tracing`
    which will subsequently send debug information to the trace helper.
    """

    def __init__(self, project_name):
        self.project_name = project_name
        self._name2plugin = {}
        self._plugin2hookcallers = {}
        self._plugin_distinfo = []
        self.trace = _tracing.TagTracer().get("pluginmanage")
        self.hook = _HookRelay()
        self._inner_hookexec = _multicall

    def _hookexec(self, hook_name, methods, kwargs, firstresult):
        """
        # called from all hookcaller instances.
        # enable_tracing will set its own wrapping function at self._inner_hookexec
        """

    def register(self, plugin, name=None):
        """Register a plugin and return its canonical name or ``None`` if the name
        is blocked from registering.  Raise a :py:class:`ValueError` if the plugin
        is already registered."""

    def parse_hookimpl_opts(self, plugin, name):
        """"""

    def unregister(self, plugin=None, name=None):
        """unregister a plugin object and all its contained hook implementations
        from internal data structures."""

    def set_blocked(self, name):
        """block registrations of the given name, unregister if already registered."""

    def is_blocked(self, name):
        """return ``True`` if the given plugin name is blocked."""

    def add_hookspecs(self, module_or_class):
        """add new hook specifications defined in the given ``module_or_class``.
        Functions are recognized if they have been decorated accordingly."""

    def parse_hookspec_opts(self, module_or_class, name):
        """"""

    def get_plugins(self):
        """return the set of registered plugins."""

    def is_registered(self, plugin):
        """Return ``True`` if the plugin is already registered."""

    def get_canonical_name(self, plugin):
        """Return canonical name for a plugin object. Note that a plugin
        may be registered under a different name which was specified
        by the caller of :py:meth:`register(plugin, name) <.PluginManager.register>`.
        To obtain the name of an registered plugin use :py:meth:`get_name(plugin)
        <.PluginManager.get_name>` instead."""

    def get_plugin(self, name):
        """Return a plugin or ``None`` for the given name."""

    def has_plugin(self, name):
        """Return ``True`` if a plugin with the given name is registered."""

    def get_name(self, plugin):
        """Return name for registered plugin or ``None`` if not registered."""

    def _verify_hook(self, hook, hookimpl):
        """"""

    def check_pending(self):
        """Verify that all hooks which have not been verified against
        a hook specification are optional, otherwise raise :py:class:`.PluginValidationError`."""

    def load_setuptools_entrypoints(self, group, name=None):
        """Load modules from querying the specified setuptools ``group``.

        :param str group: entry point group to load plugins
        :param str name: if given, loads only plugins with the given ``name``.
        :rtype: int
        :return: return the number of loaded plugins by this call.
        """

    def list_plugin_distinfo(self):
        """return list of distinfo/plugin tuples for all setuptools registered
        plugins."""

    def list_name_plugin(self):
        """return list of name/plugin pairs."""

    def get_hookcallers(self, plugin):
        """get all hook callers for the specified plugin."""

    def add_hookcall_monitoring(self, before, after):
        """add before/after tracing functions for all hooks
        and return an undo function which, when called,
        will remove the added tracers.

        ``before(hook_name, hook_impls, kwargs)`` will be called ahead
        of all hook calls and receive a hookcaller instance, a list
        of HookImpl instances and the keyword arguments for the hook call.

        ``after(outcome, hook_name, hook_impls, kwargs)`` receives the
        same arguments as ``before`` but also a :py:class:`pluggy._callers._Result` object
        which represents the result of the overall hook call.
        """

    def enable_tracing(self):
        """enable tracing of hook calls and return an undo function."""

    def subset_hook_caller(self, name, remove_plugins):
        """Return a new :py:class:`._hooks._HookCaller` instance for the named method
        which manages calls to all registered plugins except the
        ones from remove_plugins."""

```