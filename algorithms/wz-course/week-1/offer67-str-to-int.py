
class Solution:

    """
    写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

    当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

    该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

    注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

    在任何情况下，若函数不能进行有效的转换时，请返回 0。

    说明：

    假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def strToInt(self, s: str) -> int:
        # 移除空字符
        s = s.strip()

        # 最小单位是1个字符
        if len(s) < 1: return 0

        # 处理非法字符
        if s[0] != "-" and s[0] != "+" and not s[0].isdigit(): return 0

        # 当存在符号时, 最小单位是2个字符
        if s[0] in ("-", "+") and len(s) < 2: return 0

        # 正负数
        negative = s[0] == "-" and s[1].isdigit()
        positive = s[0] == "+" and s[1].isdigit()

        # 移除正负数符号
        s = s[1:] if negative else s
        s = s[1:] if positive else s

        # 切割字符串(处理空格字符)
        s = s.split()[0]

        # 截取前置为数字的字符串.
        ss = ""
        for i in s:
            if not i.isdigit(): break
            ss += i

        # 如果第一个字符不是数字, 则返回 0 表示无效
        if not ss.isdigit(): return 0

        # 转换成数字
        ss = int(ss)

        # 32 为有符号范围
        int_min = int(2 ** (4 * 8) / 2 * -1)
        int_max = int(2 ** (4 * 8) / 2 - 1)

        # 大于 32 位大小的有符号整数, 将会返回最大或最小值
        if negative and (ss * -1) < int_min: return int_min
        if not negative and ss > int_max: return int_max

        return (ss * -1) if negative else ss


def test():
    solution = Solution()

    inputs = "+1"
    expect = 1
    result = solution.strToInt(s=inputs)
    assert result == expect

    inputs = "3.14159"
    expect = 3
    result = solution.strToInt(s=inputs)
    assert result == expect

    inputs = "  -0012a42"
    expect = -12
    result = solution.strToInt(s=inputs)
    assert result == expect

    inputs = ".1"
    expect = 0
    result = solution.strToInt(s=inputs)
    assert result == expect

    inputs = "-   234"
    expect = 0
    result = solution.strToInt(s=inputs)
    assert result == expect

    inputs = ""
    expect = 0
    result = solution.strToInt(s=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
