from typing import List


# 列转行
def col_to_row_v1(matrix: List[List[int]]):
    ss = list(zip(*matrix))
    return ss


# 列转行
def col_to_row_v2(matrix: List[List[int]]):
    result = [[0] * len(i) for i in matrix]
    for col in range(len(matrix)):                       # [col] 以列为主
        for row in range(len(matrix)):                   # [row] 以行为辅
            result[col][row] = matrix[row][col]          # [row][col] 内核逻辑: 列固定, 遍历行
    return result


def main():
    s = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    result = col_to_row_v1(s)
    assert result == [(1, 1, 1, 1, 1),
                      (2, 2, 2, 2, 2),
                      (3, 3, 3, 3, 3),
                      (4, 4, 4, 4, 4),
                      (5, 5, 5, 5, 5)]

    result = col_to_row_v2(s)
    assert result == [[1, 1, 1, 1, 1],
                      [2, 2, 2, 2, 2],
                      [3, 3, 3, 3, 3],
                      [4, 4, 4, 4, 4],
                      [5, 5, 5, 5, 5]]


if __name__ == '__main__':
    main()
