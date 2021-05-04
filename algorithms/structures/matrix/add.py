from typing import List


class Add:
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

    参考:  https://www.programiz.com/python-programming/examples/add-matrix
    """

    def add_v1(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        """ 这是一个已知长度的写法 """

        result: List[List[int]] = [[0, 0, 0],
                                   [0, 0, 0],
                                   [0, 0, 0]]

        for i in range(len(a)):
            for j in range(len(a[0])):
                result[i][j] = a[i][j] + b[i][j]

        return result

    def add_v2(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        """ 这是一个未知长度的写法 """

        len_a, len_b = len(a), len(b)                               # 计算 a 和 b 的长度
        max_i = max(len_a, len_b)                                   # 取一维最大的值
        min_i = min(len_a, len_b)                                   # 取一维最小的值
        max_ab = a if len_a > len_b else b                          # 取一维最大的对象
        result: List[List[int]] = [0] * max_i                       # 填充一维数据

        for i in range(max_i):
            if i < min_i:                                           # 两边都有值得情况下, 进行二维计算和相加.
                len_x, len_y = len(a[i]), len(b[i])
                max_j = max(len_x, len_y)
                min_j = min(len_x, len_y)
                max_xy = a if len_x > len_y else b
                result[i] = [0] * max_j                             # 填充二维数据

                for j in range(max_j):
                    if j < min_j:
                        result[i][j] = a[i][j] + b[i][j]
                    else:
                        result[i][j] = max_xy[i][j]                 
            else:                                                   # 当 i 大于某一边时, 将大得对象得值搬到结果集中.
                result[i] = max_ab[i]

        return result


def test_1():
    a = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    b = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    ad = Add()
    ss = ad.add_v1(a, b)
    assert ss == [[17, 15, 4],
                  [10, 12, 9],
                  [11, 13, 18]]


def test_2():
    a = [[12, 7, 3],
         [4, 5, 6, 7],
         [7, 8, 9],
         [6, 4, 8]]

    b = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9, 10]]

    ad = Add()
    ss = ad.add_v2(a, b)
    assert ss == [[17, 15, 4],
                  [10, 12, 9, 7],
                  [11, 13, 18, 10],
                  [6, 4, 8]]


def main():

    test_1()
    test_2()


if __name__ == '__main__':
    main()
