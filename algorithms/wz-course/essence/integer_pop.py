

def integer_pop(x: int):
    """
    移除一个数的个位数, 留下剩下的值.

    1234 // 10 = 123
    123  // 10 = 12
    12   // 10 = 1
    1    // 10 = 0
    """
    return x // 10
