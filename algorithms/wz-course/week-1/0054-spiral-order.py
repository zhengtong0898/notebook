from typing import List


class Solution:

    """
    给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

    https://leetcode-cn.com/problems/spiral-matrix/
    """

    def spiralOrder(self, matrix: List[List[int]], result: List[int]) -> List[int]:

        # 当前程序处理失败的场景
        # if matrix == [[7],[9],[6]]: return [7,9,6]
        #
        # if matrix == [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]: return [1,2,3,4,5,6,7,8,9,10]
        #
        # if matrix == [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]:
        #     return [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
        #
        # if matrix == [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]: return [2,3,4,7,10,13,16,15,14,11,8,5,6,9,12]
        #
        # if matrix == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]:
        #     return [1,2,3,4,8,12,16,20,19,18,17,13,9,5,6,7,11,15,14,10]
        #
        # if matrix == [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]]:
        #     return [1,2,3,4,5,6,12,18,24,30,29,28,27,26,25,19,13,7,8,9,10,11,17,23,22,21,20,14,15,16]
        #
        # if matrix == [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]:
        #     return [1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2]
        # if matrix == [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],
        #
        #               [31,32,33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],
        #               [61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],[81,82,83,84,85,86,87,88,89,90],
        #               [91,92,93,94,95,96,97,98,99,100]]:
        #     return [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,
        #             21,11,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,23,
        #             24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,34,35,36,37,47,57,67,66,65,64,54,44,
        #             45,46,56,55]

        m, n = len(matrix), len(matrix[0])
        result.extend(matrix[0][:])
        if m < 2: return result
        if n < 1: return result

        matrix_rotate = matrix[:]
        for i in range(1, 4):
            matrix_rotate = self.reverse_rotate(matrix_rotate)
            if matrix_rotate[0] == matrix[0]: continue
            result.extend(matrix_rotate[0][1:])
            if n < 2: return result

        result.pop()
        matrix_shorter = [i[1:len(i) -1] for i in matrix[1:m-1]]
        if matrix_shorter:
            return self.spiralOrder(matrix=matrix_shorter, result=result)

    def reverse_rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix_reversed_row = [i[::-1] for i in matrix]
        return [list(i) for i in zip(*matrix_reversed_row)]

    def spiralOrder_2(self, matrix: List[List[int]]) -> List[int]:
        tmp=[]
        while matrix:
            tmp += list(matrix[0])
            zipped = list(zip(*matrix[1:]))                         # 将列转行
            matrix = zipped[::-1]                                   # 将行反向排序
        return tmp

    def spiralOrder_3(self, matrix: List[List[int]]) -> List[int]:
        tmp=[]
        while matrix:
            tmp += list(matrix[0])
            matrix_reversed_row = [i[::-1] for i in matrix[1:]]     # 将每一行内的元素反向排序
            matrix = list(zip(*matrix_reversed_row))                # 将列转行
        return tmp


def test():
    solution = Solution()

    inputs = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    expect = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    expect = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]
    expect = [5, 1, 9, 11, 10, 7, 16, 12, 14, 15, 13, 2, 4, 8, 6, 3]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    expect = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[2, 3, 4],
              [5, 6, 7],
              [8, 9, 10],
              [11, 12, 13],
              [14, 15, 16]]
    expect = [2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5, 6, 9, 12]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
              [17, 18, 19, 20]]
    expect = [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30]]
    expect = [1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 29, 28, 27, 26, 25, 19,
              13, 7, 8, 9, 10, 11, 17, 23, 22, 21, 20, 14, 15, 16]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[1,11],
              [2,12],
              [3,13],
              [4,14],
              [5,15],
              [6,16],
              [7,17],
              [8,18],
              [9,19],
              [10,20]]
    expect = [1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect

    inputs = [[1,2],[3,4]]
    expect = [1, 2, 4, 3]
    result = []
    solution.spiralOrder(matrix=inputs, result=result)
    result = solution.spiralOrder_2(matrix=inputs)
    result = solution.spiralOrder_3(matrix=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
