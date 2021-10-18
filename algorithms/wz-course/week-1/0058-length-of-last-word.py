

class Solution:

    """
    给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
    单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

    https://leetcode-cn.com/problems/length-of-last-word/
    """

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

    def lengthOfLastWord_2(self, s: str) -> int:
        # 移除两边的空字符
        s = s.strip()

        # 找到最右边的第一个空格
        begin_index = s.rfind(" ") + 1

        return len(s[begin_index:])


def test():
    solution = Solution()

    inputs = "Hello World"
    expect = 5
    result = solution.lengthOfLastWord(s=inputs)
    result = solution.lengthOfLastWord_2(s=inputs)
    assert result == expect

    inputs = "   fly me   to   the moon  "
    expect = 4
    result = solution.lengthOfLastWord(s=inputs)
    result = solution.lengthOfLastWord_2(s=inputs)
    assert result == expect

    inputs = "luffy is still joyboy"
    expect = 6
    result = solution.lengthOfLastWord(s=inputs)
    result = solution.lengthOfLastWord_2(s=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
