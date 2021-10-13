

class Solution:

    """
    字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
    给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

    示例 1:
        输入:
        first = "pale"
        second = "ple"
        输出: True
        说明: second 只要插入一个 a 就与 first 一致, 所以满足一次编辑要求。

    示例 2:
        输入:
        first = "pales"
        second = "pal"
        输出: False
        说明: second 需要插入两个字符才能与 first 一致，所以不满足一次编辑要求。
    """

    def oneEditAway(self, first: str, second: str) -> bool:
        # 相同则返回失败: 因为不需要做任何操作
        if first == second: return True

        # 两数之间的字符长度不得大于1.
        first_len, second_len = len(first), len(second)
        if abs(first_len - second_len) > 1: return False

        # 任何一个为空都返回True.
        if not first or not second: return True

        # 将字符转换成列表，然后排序
        first_list, second_list = list(first), list(second)

        # 统计不同的字符数量
        diff_count = 0
        # 选最小的遍历保证不会报错.
        longer_list = first_list if first_len > second_len else second_list
        shorter_list = second_list if longer_list == first_list else first_list
        longer_index, shorter_index = 0, 0
        while shorter_index < len(shorter_list):
            if longer_list[longer_index] != shorter_list[shorter_index]:
                diff_count += 1
                if len(longer_list[longer_index:]) != len(shorter_list[shorter_index:]):
                    longer_index += 1
                else:
                    longer_index += 1
                    shorter_index += 1
            else:
                longer_index += 1
                shorter_index += 1

        # 两个字符串相等的情况，不同的字符不得大于或等于2.
        if first_len == second_len and diff_count > 1: return False

        # 两个字符串不相等的情况，如果仍然存在不同字符，则不符合预期.
        if first_len != second_len and diff_count > 1: return False

        return True

    def oneEditAway_2(self, first: str, second: str) -> bool:
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        l1 = len(first)
        l2 = len(second)
        if l1>l2:
            s1 = first
            s2 = second
        else:
            s1 = second
            s2 = first
        k = len(s2)
        for i in range(0,len(s2)):
            if s1[i] != s2[i]:
                k = i
                break

        return s1[k+1:]==s2[k:] or s1[k+1:]==s2[k+1:]

    def oneEditAway_3(self, first: str, second: str) -> bool:
        # 计算两个字符串的长度
        first_len, second_len = len(first), len(second)
        # 将两个字符串标记为长和短两个维度
        longer, shorter = (first, second) if first_len > second_len else (second, first)
        # 选最小的遍历保证不会报错.
        # 例如: shorter = ""; longer = "a" 时,
        #      for i in range(shorter_len) 就不会报错,
        #      因为压根就不会进入循环体内.
        shorter_len = len(shorter)

        # 重点在这里
        # 当 shorter = "" 时, index = 0;
        # 当 shorter = "abcd", longer = "abcde" 时, index = 3;
        # 当 shorter = "bcd", longer = "abcd" 时, index = 3, 但是在循环体内会将 index 重置为 0;
        # 当 shorter = "abdd", longer = "abcd" 时, index = 3, 但是在循环体内会将 index 重置为 2;
        index = shorter_len
        for i in range(shorter_len):
            if longer[i] != shorter[i]:
                index = i
                break

        # 当 first = "pale", second = "ple" 时,
        # index = 1,
        # longer = first = "pale",
        # longer[index+1:] == shorter[index:]    =   longer[2:] == shorter[1:]      =    "le" == "le"     =  True
        #
        # 当 first = "pales", second = "pal" 时,
        # index = 3
        # longer = first = "pales",
        # longer[index+1:] == shorter[index:]    =   longer[4:] == shorter[3:]      =    "s" == ""         =  False
        # longer[index+1:] == shorter[index+1:]  =   longer[4:] == shorter[4:]      =    "s" == ""         =  False
        #
        # 当 first = "", second = "a" 时,
        # index = 0,
        # longer = second = "a",
        # longer[index+1:] == shorter[index:]    =   longer[1:] == shorter[0:]      =    "" == ""         =  True
        if longer[index+1:] == shorter[index:]: return True           # 这里的覆盖点是: 多出来的1个字符时有效.(insert/append)
        if longer[index+1:] == shorter[index+1:]: return True         # 这里的覆盖点是: 相同字符长度但有1个字符不同.(replace)
        return False


def test():
    solution = Solution()

    first = "pale"
    second = "ple"
    expect = True
    result = solution.oneEditAway_3(first=first, second=second)
    assert result == expect

    first = "pales"
    second = "pal"
    expect = False
    result = solution.oneEditAway_3(first=first, second=second)
    assert result == expect

    first = ""
    second = ""
    expect = True
    result = solution.oneEditAway(first=first, second=second)
    assert result == expect

    first = ""
    second = "a"
    expect = True
    result = solution.oneEditAway_3(first=first, second=second)
    assert result == expect

    first = "a"
    second = ""
    expect = True
    result = solution.oneEditAway(first=first, second=second)
    assert result == expect

    first = "a"
    second = "ab"
    expect = True
    result = solution.oneEditAway(first=first, second=second)
    assert result == expect

    first = "intention"
    second = "execution"
    expect = False
    result = solution.oneEditAway(first=first, second=second)
    assert result == expect

    first = "sea"
    second = "ate"
    expect = False
    result = solution.oneEditAway(first=first, second=second)
    assert result == expect

    first = "mart"
    second = "karma"
    expect = False
    result = solution.oneEditAway(first=first, second=second)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
