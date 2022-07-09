from hypothesis import given
from hypothesis.strategies import integers


SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def to_roman(number: int):
    numerals = []
    while number >= 1:
        for symbol, value in SYMBOLS.items():
            if value <= number:
                numerals.append(symbol)
                number -= value
                break
    return "".join(numerals)


# tdd test
def test_to_roman():
    pass


# pb test
@given(number=integers(min_value=1, max_value=5000))
def test_to_roman_numeral_simple(number):
    numeral = to_roman(number)
    assert set(numeral) and set(numeral) <= set(SYMBOLS.keys())


# 运行
# 当提供了 --hypothesis-verbosity=debug 命令行参数后, 将会打印每一个生成的样例数据.
# pytest -s --hypothesis-verbosity=debug v1.py::test_to_roman_numeral_simple
