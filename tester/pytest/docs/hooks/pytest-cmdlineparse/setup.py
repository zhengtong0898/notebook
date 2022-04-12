# sample ./setup.py file
from setuptools import setup, find_packages

setup(
    name="pytest-cmdlineparse",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["cmdlineparse=cmdlineparse.plugin"]},
)
