import pytest
import smtplib


@pytest.fixture(scope="module", params=["smtpdm.aliyun.com", "mail.python.org"])
def smtp_connection(request):
    smtp = smtplib.SMTP()
    smtp.connect(request.param)
    yield smtp
    print("finalizing {}".format(smtp))
    smtp.close()

