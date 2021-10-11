
class Solution:

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
