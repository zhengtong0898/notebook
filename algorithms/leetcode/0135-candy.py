from typing import List


# 题目链接
# https://leetcode-cn.com/problems/candy/
class Candy:

    def candy(self, ratings: List[int]) -> int:
        result = [1 for i in ratings]

        # range: 从1开始的原因是需要前置占位, 这样可以减少一次条件(边界值)判断.
        #        每次比较都是用 i(前置索引) 和 i-1(当前索引).
        for next_index in range(1, len(ratings)):                                                 # from left to right
            current_index = next_index - 1

            # 如果前置索引值大于当前索引值
            if ratings[next_index] > ratings[current_index]:
                # 将当前索引值 + 1 后, 写入给前置索引.
                result[next_index] = result[current_index] + 1

        # range: 从最后一个元素开始迭代到第0个元素.
        #        len(ratings) - 1, 是因为索引是从0开始, 否则将会越界.
        for current_index in range(len(ratings) - 1, 0, -1):                                      # from right to left
            previous_index = current_index - 1

            # 如果前置索引值大于当前索引值
            if ratings[previous_index] > ratings[current_index]:
                # 在不影响前面的结果的情况下, 取最大的一个值, 写入给前置索引.
                result[previous_index] = max(result[previous_index], result[current_index] + 1)

        return sum(result)


def test_1():
    # 准备数据
    ratings = [1, 0, 2]                  # [2, 1, 2]               = 5

    c = Candy()
    assert 5 == c.candy(ratings)


def test_2():
    # 准备数据
    ratings = [1, 2, 2]                  # [1, 2, 1]               = 4

    c = Candy()
    assert 4 == c.candy(ratings)


def test_3():
    # 准备数据
    ratings = [1, 0, 4, 3, 2, 1, 0]      # [2, 1, 5, 4, 3, 2, 1]   = 18

    c = Candy()
    assert 18 == c.candy(ratings)


def test_4():
    # 准备数据
    ratings = [1, 0, 4, 5, 6, 8, 7]      # [2, 1, 2, 3, 4, 5, 1]   = 18

    c = Candy()
    assert 18 == c.candy(ratings)


def main():

    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
