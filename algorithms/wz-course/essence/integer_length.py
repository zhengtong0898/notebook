import math


def integer_length(x: int) -> int:
    """
    获取一个数字的长度, 例如:
    1    == 1
    10   == 2
    100  == 3
    1000 == 4
    """
    return int(math.log10(x)) + 1
