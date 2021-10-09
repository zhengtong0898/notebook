

class Solution:

    def reverseWords(self, s: str) -> str:
        s_list = (s
                  .strip()                      # 移除左右空格
                  .split(" "))                  # 按空格切割成数组
        s_list = [i for i in s_list if i]       # 移除空的元素
        return " ".join(reversed(s_list))

    def reverseWords_2(self, s: str) -> str:
        """
        split:
            param： sep
            The delimiter according which to split the string.
            根据 sep 限定符来切割字符串.

            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
            sep 的默认值是 None, 意思是根据 whitespace 进行切割, 并且移除列表中的空的元素.
        """
        return " ".join(s.split(sep=None)[::-1])


def test():
    solution = Solution()

    inputs = "the sky is blue"
    expect = "blue is sky the"
    result = solution.reverseWords(s=inputs)
    assert result == expect

    inputs = "  hello world!  "
    expect = "world! hello"
    result = solution.reverseWords(s=inputs)
    assert result == expect

    inputs = "I am a student. "
    expect = "student. a am I"
    result = solution.reverseWords(s=inputs)
    assert result == expect

    inputs = "a good   example"
    expect = "example good a"
    result = solution.reverseWords(s=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
