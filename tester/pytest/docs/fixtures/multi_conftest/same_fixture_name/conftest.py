import pytest


@pytest.fixture
def fixture_a():
    print("\nmulti_conftest.same_fixture_name.conftest.fixture_a")
