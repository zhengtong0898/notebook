# content of test_tmp_path.py
CONTENT = "content"


def test_create_file(tmp_path):
    print(f"\n临时目录: {tmp_path.absolute()}")
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1


"""
执行结果

============================= test session starts ==============================
collecting ... collected 1 item

test_fixture_tmp_path.py::test_create_file PASSED                        [100%]
临时目录: /tmp/pytest-of-zt/pytest-9/test_create_file0


============================== 1 passed in 0.03s ===============================
"""