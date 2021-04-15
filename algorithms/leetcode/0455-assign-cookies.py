from typing import List


# 题目链接
# https://leetcode-cn.com/problems/assign-cookies/
class AssignCookies:

    def assign_cookie(self, greed: List[int], size: List[int]):
        """

        :param greed: 胃口值(每个元素对应一个小孩子的胃口值)
        :param size: 饼干尺寸(每个元素对应一个饼干的尺寸)
        :return: 最多能满足几个小孩子的胃口
        """

        greed.sort()
        size.sort()

        # min_v = min(g[-1], s[-1]):  这样写是不对的,
        # return min_v
        #
        # 解释
        # g = [1,2,3,4,5], s = [2,3,4,9]
        # g[-1] = 5, s[-1] = 9, min_v = 5,
        # 这里并没有满足胃口值是5的饼干,
        # 只有 4 是满足的.

        child_flag = 0
        cookie_flag = 0

        while cookie_flag < len(size) and child_flag < len(greed):

            # s[cookie_flag]: 饼干尺寸
            # g[child_flag]: 小孩子胃口值
            can_feed = size[cookie_flag] >= greed[child_flag]

            # 当饼干能喂饱小孩子时, move child_flag
            if can_feed:
                child_flag += 1

            # 当饼干不能喂饱小孩子时, move cookie_flag, 因为这个饼干不满足条件, 需比较下一个.
            # 当饼干能喂饱小孩子时, move cookie_flag, 因为这个饼干已经被分配走了, 需比较下一个.
            cookie_flag += 1

        return child_flag


def test_1():
    # 准备数据
    greed = [1, 2, 3]           # 三个小孩子
    size = [1, 1]               # 两个饼干, 尺寸都是1

    # 运行
    ac = AssignCookies()
    ss = ac.assign_cookie(greed, size)

    # 断言
    assert ss == 1


def test_2():
    # 准备数据
    greed = [1, 2]              # 两个小孩子
    size = [1, 2, 3]            # 三个饼干, 三个不同尺寸

    # 运行
    ac = AssignCookies()
    ss = ac.assign_cookie(greed, size)

    # 断言
    assert ss == 2


def test_3():
    # 准备数据
    greed = [1, 2, 3, 4, 5]     # 五个小孩子
    size = [2, 9]               # 两个饼干, 两个不同尺寸

    # 运行
    ac = AssignCookies()
    ss = ac.assign_cookie(greed, size)

    assert ss == 2              # 第一个饼干'2', 可以让第一个小孩子吃饱, 所以分配给第一个小孩子.
                                # 第二个饼干'9', 可以让第二个小孩子吃饱, 所以分配给第二个小孩子.
                                # 所以期望值是能满足2个小孩子.


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
