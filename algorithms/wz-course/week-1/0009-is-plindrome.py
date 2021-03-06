import math
from typing import List, Union


class Solution:

    """
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

    你能不将整数转为字符串来解决这个问题吗？

    https://leetcode-cn.com/problems/palindrome-number/
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return str(x) == str(x)[::-1]

    def isPalindrome_2(self, x: int) -> bool:
        if x < 0: return False

        # 计算出当前数值的长度
        x_len = self.length(x)

        # 通过取余法，将int转换成列表
        x_list = self.itol(x, x_len, reverse=True)

        # 将列表值相加
        xx = sum([c for a, b, c in x_list])

        return x == xx

    def length(self, x: int) -> int:
        return int(math.log10(x)) + 1

    def itol(self, x: int, length: int, reverse=False) -> List[Union[int, str]]:
        i_list = []
        iterable = list(range(1, length) if reverse else reversed(range(1, length)))
        iterable_always_reverse = reversed(range(length))

        if reverse: i_list.append((x % 10))
        for i in iterable:
            capacity = 10 ** i
            digit = int((x / capacity)) % 10
            i_list.append(digit)
        if not reverse: i_list.append((x % 10))

        for index, i in enumerate(iterable_always_reverse):
            capacity = 10 ** i
            value = i_list[index]
            i_list[index] = (value, str(value), value * capacity)

        return i_list

    def isPalindrome_3(self, x: int) -> bool:
        """
        %  10  在这里被用作是取最后一位数字的作用
        %      还可以被用作是无限循环取值(有效保护边界取值错误问题), 例如: index % list.size()

        // 10  在这里被用作是持续递增的形式消除最后一个数字.

        假设 x == 1234
            # 第一次循环
            y = (0 * 10) + (1234 % 10)      == 0 + 4            == 4
            x = 1234 // 10                                      == 123

            # 第二次循环
            y = (4 * 10) + (123 % 10)       == 40 + 3           == 43
            x = 123 // 10                                       == 12

            # 第三次循环
            y = (43 * 10) + (12 % 10)       == 430 + 2         == 432
            x = 12 // 10                                       == 1

            # 第四次循环
            y = (432 * 10) + (1 % 10)       == 4320 + 1        == 4321
            x = x // 10                                        == 0
        """
        if x < 0: return False

        y = 0
        while x > 0:
            y = (y * 10) + (x % 10)
            x = x // 10
        return y == x


def test():
    solution = Solution()

    inputs = 121
    expect = True
    result = solution.isPalindrome(x=inputs)
    result = solution.isPalindrome_2(x=inputs)
    assert result == expect

    inputs = -121
    expect = False
    result = solution.isPalindrome(x=inputs)
    result = solution.isPalindrome_2(x=inputs)
    assert result == expect

    inputs = 10
    expect = False
    result = solution.isPalindrome(x=inputs)
    result = solution.isPalindrome_2(x=inputs)
    assert result == expect

    inputs = -101
    expect = False
    result = solution.isPalindrome(x=inputs)
    result = solution.isPalindrome_2(x=inputs)
    assert result == expect

    inputs = 1001
    expect = True
    result = solution.isPalindrome(x=inputs)
    result = solution.isPalindrome_2(x=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
