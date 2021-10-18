from typing import List


class Solution:

    """
    给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

    你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

    https://leetcode-cn.com/problems/rotate-image/
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        # 找规律
        # 第一行
        # [0, 0] -> [0, 3],      [0, 1] -> [1, 3],        [0, 2] -> [2, 3],        [0, 3] -> [3, 3]
        # 第二行
        # [1, 0] -> [0, 2],      [1, 1] -> [1, 2],        [1, 2] -> [2, 2],        [1, 3] -> [3, 2]

        row_size = len(matrix)
        col_size = len(matrix[0])

        # 创建一个临时矩阵, 用于装那些临时被替换的值
        swap_matrix = [[-1001] * col_size for i in range(row_size)]
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                # 旋转到目标位置
                coord = [col_index, row_size - 1 - row_index]
                # 将被替换的值, 先保存到 swap_matrix 相同的位置
                swap_matrix[coord[0]][coord[1]] = matrix[coord[0]][coord[1]]

                # 如果 swap_matrix 相同的位置存在值, 那么就表示该值有效, 使用 swap_matrix 来处理.
                # 如果 swap_matrix 相同的位置是-1001, 那么就表示该位置的值没被替换过, 使用 matrix 来处理.
                if swap_matrix[row_index][col_index] == -1001:
                    matrix[coord[0]][coord[1]] = matrix[row_index][col_index]
                else:
                    matrix[coord[0]][coord[1]] = swap_matrix[row_index][col_index]

    def rotate_2(self, matrix: List[List[int]]) -> None:
        # 假设
        # matrix = [[1, 2, 3],
        #           [4, 5, 6],
        #           [7, 8, 9]]
        #
        #
        # 反转
        # ss = matrix[::-1]
        # 行视角                                  矩阵视角(反转前)         矩阵视角(反转后)
        # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]      [[1, 2, 3],           [[7, 8, 9],
        # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]       [4, 5, 6],            [4, 5, 6],
        #                                         [7, 8, 9]]            [1, 2, 3]]
        #
        # 列转行
        # zip(*ss)
        # 行视角                                  矩阵视角(列转行前)       矩阵视角(列转行后)
        # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]      [[7, 8, 9],           [[7, 4, 1],
        # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]       [4, 5, 6],            [8, 5, 2],
        #                                         [1, 2, 3]]            [9, 6, 3]]
        ss = matrix[::-1]
        matrix[:] = zip(*ss)


def test():
    solution = Solution()

    inputs = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    expect = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]
    solution.rotate_2(matrix=inputs)
    assert inputs == expect

    inputs = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]
    expect = [[15, 13, 2, 5],
              [14, 3, 4, 1],
              [12, 6, 8, 9],
              [16, 7, 10, 11]]
    solution.rotate_2(matrix=inputs)
    assert inputs == expect


def main():
    test()


if __name__ == '__main__':
    main()
