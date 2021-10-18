

def integer_reverse(x: int):
    """
    将一个数字反转过来.
    例如:
    1234 -> 4321
    1122 -> 2211
    """
    result = 0
    while x > 0:
        result = result * 10                # result 整体向左移动一位, 腾挪出个位数.
        result = result + (x % 10)          # 将个位数写入到 result.
        x = x // 10                         # x 整体向右移动一位.

    return result
