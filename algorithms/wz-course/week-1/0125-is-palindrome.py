import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        letter_list = re.findall(r"[a-zA-Z0-9]", s)
        letter_str = "".join(letter_list).lower()

        curr_index, last_index = 0, len(letter_str) - 1
        while curr_index < last_index:
            a = letter_str[curr_index]
            b = letter_str[last_index]
            if a != b:
                return False
            curr_index += 1
            last_index -= 1

        return True

    def isPalindrome_2(self, s: str) -> bool:
        """
        filter 第一个参数是函数: str.isalnum, 第二个参数是 s 字符串.
        filter 会将 s 的每个元素, 都执行一次 str.isalnum(s[i]),
        filter 根据返回的值是True时, 提取当前 s[i] 的值.
        """
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


def test():
    solution = Solution()

    inputs = "A man, a plan, a canal: Panama"
    expect = True
    result = solution.isPalindrome(s=inputs)
    assert result == expect

    inputs = "race a car"
    expect = False
    result = solution.isPalindrome(s=inputs)
    assert result == expect

    inputs = "ab_a"
    expect = True
    result = solution.isPalindrome(s=inputs)
    assert result == expect

    inputs = "OP"
    expect = False
    result = solution.isPalindrome(s=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
