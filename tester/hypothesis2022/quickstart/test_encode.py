from src.code import encode, decode
from hypothesis import given
from hypothesis.strategies import text


# 这个代码可以完成100%覆盖率
@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s


# 这个代码可以完成100%覆盖率
def test_decode():
    assert decode(encode("abc")) == "abc"
    assert decode(encode("abb")) == "abb"
    assert decode(encode("")) == ""
