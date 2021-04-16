from typing import List


class Candy:

    def candy_v1(self, ratings: List[int]) -> int:
        res = len(ratings) * [1]

        for i in range(1, len(ratings)):                        # from left to right
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings) - 1, 0, -1):                # from right to left
            if ratings[i - 1] > ratings[i]:
                res[i - 1] = max(res[i - 1], res[i] + 1)

        return sum(res)


def test_1():
    # 准备数据
    ratings_v1 = [1, 0, 2]                  # [2, 1, 2]               = 5

    c = Candy()
    assert 5 == c.candy_v1(ratings_v1)


def test_2():
    # 准备数据
    ratings_v1 = [1, 2, 2]                  # [1, 2, 1]               = 4

    c = Candy()
    assert 4 == c.candy_v1(ratings_v1)


def test_3():
    # 准备数据
    ratings_v1 = [1, 0, 4, 3, 2, 1, 0]      # [2, 1, 5, 4, 3, 2, 1]   = 18

    c = Candy()
    assert 18 == c.candy_v1(ratings_v1)


def test_4():
    # 准备数据
    ratings_v1 = [1, 0, 4, 5, 6, 8, 7]      # [2, 1, 2, 3, 4, 5, 1]   = 18

    c = Candy()
    assert 18 == c.candy_v1(ratings_v1)


def main():

    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
