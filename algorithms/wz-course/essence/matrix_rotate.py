from typing import List


# 顺序旋转 90 度
def sequence_rotate(matrix: List[List[int]]):
    reverse_row = matrix[::-1]                          # 将行反向排序
    return list(zip(*reverse_row))                      # 将列转行


# 反向旋转 90 度
def reverse_rotate(matrix: List[List[int]]):
    matrix_reversed_row = [i[::-1] for i in matrix]     # 将每一行内的元素反向排序
    return list(zip(*matrix_reversed_row))              # 将列转行


def main():
    inputs = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]

    expect = [(15, 13, 2, 5),
              (14, 3, 4, 1),
              (12, 6, 8, 9),
              (16, 7, 10, 11)]
    result = sequence_rotate(matrix=inputs)
    assert result == expect

    inputs = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]

    expect = [(11, 10, 7, 16),
              (9, 8, 6, 12),
              (1, 4, 3, 14),
              (5, 2, 13, 15)]
    result = reverse_rotate(matrix=inputs)
    assert result == expect


if __name__ == '__main__':
    main()
