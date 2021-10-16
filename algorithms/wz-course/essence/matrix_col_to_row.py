s = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]


# 获取列: 列固定, 遍历行
def get_column(index):
    result = [[0] * len(i) for i in s]
    for col in range(len(s)):                       # [col] 以列为主
        for row in range(len(s)):                   # [row] 以行为辅
            result[col][row] = s[row][col]          # [row][col] 内核逻辑: 列固定, 遍历行
    return result[index]


# 列转行
def swap_row_and_col():
    ss = list(zip(*s))
    return ss


def main():
    assert get_column(0) == [1, 1, 1, 1, 1]
    assert get_column(1) == [2, 2, 2, 2, 2]
    assert get_column(2) == [3, 3, 3, 3, 3]
    assert get_column(3) == [4, 4, 4, 4, 4]
    assert get_column(4) == [5, 5, 5, 5, 5]

    assert swap_row_and_col() == [(1, 1, 1, 1, 1),
                                  (2, 2, 2, 2, 2),
                                  (3, 3, 3, 3, 3),
                                  (4, 4, 4, 4, 4),
                                  (5, 5, 5, 5, 5)]


if __name__ == '__main__':
    main()