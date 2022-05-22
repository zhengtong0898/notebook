

def test_same_fixture_name_in_diff_levels(fixture_a, request):
    """
    ============================= test session starts ==============================
    platform linux -- Python 3.8.10, pytest-7.1.0, pluggy-1.0.0
    rootdir: /home/zt/PycharmProjects/learn_staff/tester/pytest/docs/fixtures/multi_conftest
    plugins: allure-pytest-2.9.45
    collected 1 item

    same_fixture_name/subdir/test_fixture_order_with_same_fixture_name.py
    multi_conftest.same_fixture_name.conftest.fixture_a
    .

    ============================== 1 passed in 0.02s ===============================
    """
    pass


def test_same_fixture_name_in_diff_levels2(fixture_a, request):
    pass


def test_same_fixture_name_in_diff_levels3(fixture_a, request):
    pass
