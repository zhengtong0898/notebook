from setuptools import setup, find_packages
"""
参考: 
https://setuptools.pypa.io/en/latest/userguide/entry_point.html

name: 
        类型: str
        实参: 指定包的名称   

install_requires: 
        类型: Union[str, List[str]]
        实参: 指定依赖的安装包
        案例: https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#declaring-dependencies

entry_points:
        概述: 该参数用于动态发现插件, 并且支持生成命令行的可执行文件.  
        类型: Dict[str, Union[str, List[str]]
        实参: 字典的键可以是任意字符串(被视为是一个group), 通常按照框架的约束来定义. 
                 1. setuptools默认情况下支持两个值
                    "console_scripts": 表示生成命令行可执行文件.
                    "gui_scripts": 表示生成图形软件可执行文件.  
                 2. pytest要求字典的键是"pytest11", 表示它是一个pytest的插件.
             字典的值是一个字符串, 字符串里面又是一个键值(被视为是一个key, value),
             当group="console_scripts"时, key表示可执行文件的名称, value表示是执行函数.  
             当group="pytest11"时, key表示插件名称, value表示hookimpl所在的文件.  

packages:
        类型: List[str]
        实参: setuptools会将该列表中的包(包含__init__.py)的文件夹, 全部打包安装到python/lib目录下.
             注: find_packages() 的作用是找到当前目录下的所有包, 返回一个列表.  
"""
ss = find_packages()
print(f"\nss: {ss}")
setup(
    name="eggsample",
    install_requires="pluggy>=0.3,<1.0",
    entry_points={"console_scripts": ["eggsample-zt=eggsample.host:main"]},
    packages=find_packages(),
)
