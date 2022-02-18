import pytest


code = pytest.main(["example.py", "-s", "--alluredir=allure-results"])
print(f"code: {code}")
