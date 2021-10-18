from typing import List


class Solution:

    """
    编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

    https://leetcode-cn.com/problems/zero-matrix-lcci/
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 获取 0 的坐标
        zeroes = []
        for x, row in enumerate(matrix):
            for y, col in enumerate(row):
                if col == 0:
                    zeroes.append((x, y))

        # 将所在行和列清零
        for x, y in zeroes:
            # 行清零
            for col, _ in enumerate(matrix[x]):
                matrix[x][col] = 0
            # 列清零
            for row, _ in enumerate(matrix):
                matrix[row][y] = 0


def test():
    solution = Solution()

    inputs = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    expect = [[1, 0, 1],
              [0, 0, 0],
              [1, 0, 1]]
    solution.setZeroes(matrix=inputs)
    assert inputs == expect

    inputs = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]
    expect = [[0, 0, 0, 0],
              [0, 4, 5, 0],
              [0, 3, 1, 0]]
    solution.setZeroes(matrix=inputs)
    assert inputs == expect


def main():
    test()


if __name__ == '__main__':
    main()
