import pytest


@pytest.fixture(scope="module")
def fixture_a(request):
    return "fixture_a_rst"


def fixture_b():

    return "fixture_b_rst"
