

class Solution:

    """
    面试题 08.01. 三步问题 （简单）

    三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
    实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

    示例-1
    输入：n = 3
    输出：4
    说明: 有四种走法

    示例-2
    输入：n = 5
    输出：13

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.cache = {}

    def waysToStep(self, n: int) -> int:
        """
        解题思路

        当 n = 0 时, 有 1 种走法.
        第一种: 0

        当 n = 1 时, 有 1 种走法.
        第一种: 1

        当 n = 2 时, 有 2 种走法.
        第一种: 1 + 1
        第二种: 2

        当 n = 3 时, 有 4 种走法.
        第一种: 1 + 1 + 1
        第二种: 1 + 2
        第三种: 2 + 1
        第四种: 3

        1. 这种求排列组合的,da一感觉就是可以用递归来解.
        2. 上台阶的方式有3中, 意味着有三种不同的路径可以尝试, 从递归树的角度来看, 就是三个分支.
        打脸了, 单纯的套递归代码解不了这道题, 下面这个代码是错误的.
        TODO: 看了很多题解都是动态规划来解，这道题留给后面掌握动态规划后再来解.
        """
        if n == 0: return 1
        if n <= 2: return n
        if self.cache.get(n): return self.cache[n]
        self.cache[n] = self.waysToStep(n - 1) + self.waysToStep(n - 2) + self.waysToStep(n - 3)
        return self.cache[n]
