

def integer_divmod(x: int):
    """
    获取一个数字的最后一个值, 即: 个位数的那个值.
    例如:
    1    % 10 = 1
    12   % 10 = 2
    123  % 10 = 3
    1234 % 10 = 4
    """
    return x % 10
