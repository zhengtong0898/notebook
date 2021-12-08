

class Solution:

    """
    剑指 Offer 10- I. 斐波那契数列 （简单）

    写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

    斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.cache = {}

    def fib(self, n: int) -> int:
        if n < 2: return n
        if self.cache.get(n): return self.cache[n]
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n] % 1000000007


def main():
    ss = Solution().fib(n=2)
    assert ss == 1

    ss = Solution().fib(n=5)
    assert ss == 5


if __name__ == '__main__':
    main()
