import pytest
import smtplib


@pytest.fixture(scope="module")
def smtp_connection():
    smtp = smtplib.SMTP()
    smtp.connect("smtpdm.aliyun.com")
    return smtp
