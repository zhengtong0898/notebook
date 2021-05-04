from typing import List


# TODO: 矩阵相乘得使用场景?
#       https://www.programiz.com/python-programming/examples/multiply-matrix
#       https://www.cnblogs.com/ljy-endl/p/11411665.html
#       https://www.zhihu.com/question/21351965?sort=created
class Multiple:

    def multiple(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:

        len_a, len_b = len(a), len(b)
        result = [0] * max(len_a, len_b)                        # 填充一维列表
        for i in range(len_a):                                  # a_row

            len_x, len_y = len(a[i]), len(b[i])
            result[i] = [0] * max(len_x, len_y)                 # 填充二维列表
            for j in range(len_y):                              # b_col

                for k in range(len_b):                          # b_row
                    aitem = a[i][k]                             # 行值
                    bitem = b[k][j]                             # 列值
                    print(aitem, bitem)
                    result[i][j] += aitem * bitem               # 行 * 列 得值得总合.

        return result


def test_1():
    a = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    b = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]

    multip = Multiple()
    ss = multip.multiple(a, b)
    assert ss == [[114, 160, 60, 27],
                  [74, 97, 73, 14],
                  [119, 157, 112, 23]]


def main():

    test_1()


if __name__ == '__main__':
    main()

