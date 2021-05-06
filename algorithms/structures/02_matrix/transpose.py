from typing import List


class Transpose:
    """
    一个 m x n 的矩阵,
    转置之后是,
    一个 n x m 的矩阵.

    例如:
    [[ 1,  2,  3,  4],
     [ 5,  6,  7,  8],
     [ 9, 10, 11, 12]]

    转置后是
    [[ 1,  5,  9],
     [ 2,  6, 10],
     [ 3,  7, 11],
     [ 4,  8, 12]]

    python 中的 zip 就是一个标准的矩阵转置函数, 可以模仿zip的表现来做实现.

    参考:  https://github.com/python/cpython/blob/master/Doc/tutorial/datastructures.rst#nested-list-comprehensions
    """

    def zip(self, items: List[List[int]]) -> List[List[int]]:
        return list(zip(*items))

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        result: List[List[int]] = []
        row_len = len(matrix[0])                      # 获取行(n)长度
        for n in range(row_len):

            transposed_row = []                       # n x m
            for m in matrix:
                if m[n:n+1]:
                    transposed_row.append(m[n])
            transposed_row = tuple(transposed_row)

            if n > 0 and len(result[-1]) > len(transposed_row):
                continue

            result.append(transposed_row)

        return result


def test_1():

    items = [[1,  2,  3,  4],
             [5,  6,  7,  8],
             [9, 10, 11, 12]]

    transpose = Transpose()
    ss_1 = transpose.zip(items)
    ss_2 = transpose.transpose(items)
    assert ss_1 == ss_2


def test_2():

    items = [[1,  2,  3,  4],
             [5,  6,  7,  8],
             [9, 10, 11]]

    transpose = Transpose()
    ss_1 = transpose.zip(items)
    ss_2 = transpose.transpose(items)
    assert ss_1 == ss_2


def main():

    test_1()
    test_2()


if __name__ == '__main__':
    main()
