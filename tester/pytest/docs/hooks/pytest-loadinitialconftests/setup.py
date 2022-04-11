# sample ./setup.py file
from setuptools import setup, find_packages

setup(
    name="pytest-loadinitialconftests",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["loadinitialconftests=loadinitialconftests.plugin"]},
)
