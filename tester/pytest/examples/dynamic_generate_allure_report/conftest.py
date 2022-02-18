import pytest
import delegator


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_logfinish(nodeid, location):

    yield

    job_id = 10
    target_dir = f"/usr/share/nginx/html/{job_id}"                                        # get target-dir from jenkins

    communicate = delegator.run(f"allure generate --clean -o {target_dir}")
    print(f"\n communicate: {communicate} \n")
