import sys


if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def test_main():
    for dist in list(importlib_metadata.distributions()):
        # dist.entry_points: List[importlib.metadata.EntryPoint]
        # importlib.metadata.EntryPoint 是一个元组对象, 它内置了name, value, group三个属性;
        # 这个对象实例化的时候是读取插件包中的setup.py中的name和entry_points; 关键属性: name, value, group;
        # 当我们执行 entry_point.name 操作时, 实际上是读取 entry_point[0] 的值.
        for entry_point in dist.entry_points:
            print(f"name: {entry_point[0]}; value: {entry_point[1]}; group: {entry_point[2]}")


"""
group == console_scripts 表示对应的name是一个可执行命令.

输出结果

============================= test session starts ==============================
collecting ... collected 1 item

test_importlib_distribution.py::test_main PASSED                         [100%]

name: alias; value: setuptools.command.alias:alias; group: distutils.commands
name: bdist_egg; value: setuptools.command.bdist_egg:bdist_egg; group: distutils.commands
name: bdist_rpm; value: setuptools.command.bdist_rpm:bdist_rpm; group: distutils.commands
name: build_clib; value: setuptools.command.build_clib:build_clib; group: distutils.commands
name: build_ext; value: setuptools.command.build_ext:build_ext; group: distutils.commands
name: build_py; value: setuptools.command.build_py:build_py; group: distutils.commands
name: develop; value: setuptools.command.develop:develop; group: distutils.commands
name: dist_info; value: setuptools.command.dist_info:dist_info; group: distutils.commands
name: easy_install; value: setuptools.command.easy_install:easy_install; group: distutils.commands
name: egg_info; value: setuptools.command.egg_info:egg_info; group: distutils.commands
name: install; value: setuptools.command.install:install; group: distutils.commands
name: install_egg_info; value: setuptools.command.install_egg_info:install_egg_info; group: distutils.commands
name: install_lib; value: setuptools.command.install_lib:install_lib; group: distutils.commands
name: install_scripts; value: setuptools.command.install_scripts:install_scripts; group: distutils.commands
name: rotate; value: setuptools.command.rotate:rotate; group: distutils.commands
name: saveopts; value: setuptools.command.saveopts:saveopts; group: distutils.commands
name: sdist; value: setuptools.command.sdist:sdist; group: distutils.commands
name: setopt; value: setuptools.command.setopt:setopt; group: distutils.commands
name: test; value: setuptools.command.test:test; group: distutils.commands
name: upload_docs; value: setuptools.command.upload_docs:upload_docs; group: distutils.commands
name: convert_2to3_doctests; value: setuptools.dist:assert_string_list; group: distutils.setup_keywords
name: dependency_links; value: setuptools.dist:assert_string_list; group: distutils.setup_keywords
name: eager_resources; value: setuptools.dist:assert_string_list; group: distutils.setup_keywords
name: entry_points; value: setuptools.dist:check_entry_points; group: distutils.setup_keywords
name: exclude_package_data; value: setuptools.dist:check_package_data; group: distutils.setup_keywords
name: extras_require; value: setuptools.dist:check_extras; group: distutils.setup_keywords
name: include_package_data; value: setuptools.dist:assert_bool; group: distutils.setup_keywords
name: install_requires; value: setuptools.dist:check_requirements; group: distutils.setup_keywords
name: namespace_packages; value: setuptools.dist:check_nsp; group: distutils.setup_keywords
name: package_data; value: setuptools.dist:check_package_data; group: distutils.setup_keywords
name: packages; value: setuptools.dist:check_packages; group: distutils.setup_keywords
name: python_requires; value: setuptools.dist:check_specifier; group: distutils.setup_keywords
name: setup_requires; value: setuptools.dist:check_requirements; group: distutils.setup_keywords
name: test_loader; value: setuptools.dist:check_importable; group: distutils.setup_keywords
name: test_runner; value: setuptools.dist:check_importable; group: distutils.setup_keywords
name: test_suite; value: setuptools.dist:check_test_suite; group: distutils.setup_keywords
name: tests_require; value: setuptools.dist:check_requirements; group: distutils.setup_keywords
name: use_2to3; value: setuptools.dist:assert_bool; group: distutils.setup_keywords
name: use_2to3_exclude_fixers; value: setuptools.dist:assert_string_list; group: distutils.setup_keywords
name: use_2to3_fixers; value: setuptools.dist:assert_string_list; group: distutils.setup_keywords
name: zip_safe; value: setuptools.dist:assert_bool; group: distutils.setup_keywords
name: PKG-INFO; value: setuptools.command.egg_info:write_pkg_info; group: egg_info.writers
name: dependency_links.txt; value: setuptools.command.egg_info:overwrite_arg; group: egg_info.writers
name: depends.txt; value: setuptools.command.egg_info:warn_depends_obsolete; group: egg_info.writers
name: eager_resources.txt; value: setuptools.command.egg_info:overwrite_arg; group: egg_info.writers
name: entry_points.txt; value: setuptools.command.egg_info:write_entries; group: egg_info.writers
name: namespace_packages.txt; value: setuptools.command.egg_info:overwrite_arg; group: egg_info.writers
name: requires.txt; value: setuptools.command.egg_info:write_requirements; group: egg_info.writers
name: top_level.txt; value: setuptools.command.egg_info:write_toplevel_names; group: egg_info.writers
name: 2to3_doctests; value: setuptools.dist:Distribution._finalize_2to3_doctests; group: setuptools.finalize_distribution_options
name: keywords; value: setuptools.dist:Distribution._finalize_setup_keywords; group: setuptools.finalize_distribution_options
name: parent_finalize; value: setuptools.dist:_Distribution.finalize_options; group: setuptools.finalize_distribution_options
name: py.test; value: pytest:console_main; group: console_scripts
name: pytest; value: pytest:console_main; group: console_scripts
name: allure_pytest; value: allure_pytest.plugin; group: pytest11
name: pip; value: pip._internal.cli.main:main; group: console_scripts
name: pip3; value: pip._internal.cli.main:main; group: console_scripts
name: pip3.8; value: pip._internal.cli.main:main; group: console_scripts
name: wheel; value: wheel.cli:main; group: console_scripts
name: bdist_wheel; value: wheel.bdist_wheel:bdist_wheel; group: distutils.commands
name: eggsample; value: eggsample.host:main; group: console_scripts


============================== 1 passed in 0.04s ===============================
"""