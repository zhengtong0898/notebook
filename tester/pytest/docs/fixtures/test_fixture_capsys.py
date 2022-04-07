

def test_capsys(capsys):
    """
    使用 capsys.readouterr() 捕获所有标准输出, 写入captured对象.
    """
    print("hello")
    captured = capsys.readouterr()
    stdout, stderr = captured.out, captured.err
    assert stdout == "hello\n"
    assert stderr == ''


def test_capsys_rewrite(capsys):
    """
    使用 capsys.readouterr() 捕获所有标准输出, 写入captured对象.
    然后再使用 sys.stdout.write 在次写入到标准输出, 此时的输出就没有被捕获.
    """
    import sys
    print("good")
    captured = capsys.readouterr()
    stdout, stderr = captured.out, captured.err
    sys.stdout.write(stdout)


def test_capsys_stderr(capsys):
    """
    使用 capsys.readouterr() 捕获所有标准输出, 写入captured对象.
    然后再使用 sys.stdout.write 在次写入到标准输出, 此时的输出就没有被捕获.
    """
    import sys
    print("bad", file=sys.stderr)

    captured = capsys.readouterr()
    stdout, stderr = captured.out, captured.err
    sys.stdout.write(stderr)


"""
输出结果

============================= test session starts ==============================
collecting ... collected 3 items

test_fixture_capsys.py::test_capsys PASSED                               [ 33%]
test_fixture_capsys.py::test_capsys_rewrite PASSED                       [ 66%]
good
test_fixture_capsys.py::test_capsys_stderr PASSED                        [100%]
bad

============================== 3 passed in 0.04s ===============================
"""