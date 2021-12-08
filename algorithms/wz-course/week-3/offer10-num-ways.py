

class Solution:

    """
    剑指 Offer 10- II. 青蛙跳台阶问题（简单）

    一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

    示例-1
    输入：n = 2
    输出：2

    示例-2
    输入：n = 7
    输出：21

    示例-3
    输入：n = 0
    输出：1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.cache = {}

    def numWays(self, n: int) -> int:
        """
        解题思路
        当 n = 0 时, 有 1 种跳法
        第一种: 0

        当 n = 1 时, 有 1 种跳法
        第一种: 1

        当 n = 2 时, 有 2 种跳法
        第一种: 1 + 1
        第二种: 2

        当 n = 3 时, 有 3 种跳法
        第一种: 1 + 1 + 1
        第二种: 1 + 2
        第三种: 2 + 1

        当 n = 4 时, 有 5 种跳法
        第一种: 1 + 1 + 1 + 1
        第二种: 1 + 1 + 2
        第三种: 1 + 2 + 1
        第四种: 2 + 1 + 1
        第五种: 2 + 2

        当 n = 5 是, 有 8 种跳法
        第一种: 1 + 1 + 1 + 1 + 1
        第二种: 1 + 1 + 1 + 2
        第三种: 1 + 1 + 2 + 1
        第四种: 1 + 2 + 1 + 1
        第五种: 1 + 2 + 2
        第六种: 2 + 1 + 1 + 1
        第七种: 2 + 1 + 2
        第八种: 2 + 2 + 1

        从结果导向来看, 1, 1, 2, 3, 5, 8 可以得出这是一个 fibonacci 数列, 可以使用递归来解题.

        关于更多的 fibonacci 的Debug, 参考这里:
        https://github.com/zhengtong0898/notebook/blob/main/algorithms/wz-course/essence/recursion_complex.py
        """
        if n == 0: return 1
        if n <= 3: return n
        if self.cache.get(n): return self.cache[n]
        self.cache[n] = self.numWays(n - 1) + self.numWays(n - 2)
        return self.cache[n] % 1000000007


def main():
    ss = Solution().numWays(7)
    assert ss == 21

    ss = Solution().numWays(0)
    assert ss == 1

    ss = Solution().numWays(2)
    assert ss == 2


if __name__ == '__main__':
    main()
