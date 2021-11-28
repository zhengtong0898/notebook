

class Solution:

    """
    70. 爬楼梯（简单）

    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

    注意：给定 n 是一个正整数。

    示例-1:
    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
          1.  1 阶 + 1 阶
          2.  2 阶

    示例-2:
    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
          1.  1 阶 + 1 阶 + 1 阶
          2.  1 阶 + 2 阶
          3.  2 阶 + 1 阶

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/climbing-stairs
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        """
        Question: 为什么采取递归的 fibonacci 可以计算出所有的排列组合?
        Answer:   标准的 fibonacci 不能计算出所有的排列组合, 因为它的前置数列是 1, 1, 2, 3, 5, 8, 13, 21
                  而当前函数能计算出所有的排列组合, 是因为它减少了一次递归的过程, 所以它的数列是: 1, 2, 3, 5, 8, 13, 21, 34

        衔接上述示例.
        示例-3
        输入: 4
        输出: 5
        解释: 有五种方法可以爬到楼顶.
             1 + 1 + 1 + 1
             1 + 1 + 2
             1 + 2 + 1
             2 + 1 + 1
             2 + 2
        """
        if n == 1:
            return 1

        if n == 2:                  # 标准的 fibonacci 这里是 0, 而当前函数这里是 2, 理论上在所有的分支上都减少了一次递归过层.
            return 2

        if self.cache.get(n):
            return self.cache[n]

        self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]


def test_1():
    ss = Solution().climbStairs(2)
    assert ss == 2


def test_2():
    ss = Solution().climbStairs(3)
    assert ss == 3


def test_3():
    ss = Solution().climbStairs(4)
    assert ss == 5


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
