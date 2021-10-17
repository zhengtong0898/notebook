import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        """
        时间复杂度是: O(3n) -> O(n)
        """
        letter_list = re.findall(r"[a-zA-Z0-9]", s)             # 1 * n
        letter_str = "".join(letter_list).lower()               # 1 * n

        curr_index, last_index = 0, len(letter_str) - 1         # 1 * n
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
        时间复杂度: O(2n) -> O(n)
        """
        s = ''.join(filter(str.isalnum, s)).lower()             # 1 * n
        return s == s[::-1]                                     # 1 * n

    def isPalindrome_3(self, s: str) -> bool:
        """
        时间复杂度: O(n)
        """
        curr_index, last_index = 0, len(s) - 1
        while curr_index < last_index:

            if not self.is_alpha(s[curr_index]):
                curr_index += 1
                continue

            if not self.is_alpha(s[last_index]):
                last_index -= 1
                continue

            if self.lower(s[curr_index]) != self.lower(s[last_index]):
                return False

            curr_index += 1
            last_index -= 1

        return True

    def is_alpha(self, s: str) -> bool:
        if "a" <= s <= "z": return True
        if "A" <= s <= "Z": return True
        if "0" <= s <= "9": return True
        return False

    def lower(self, s: str) -> str:
        if "a" <= s <= "z": return s
        if "0" <= s <= "9": return s
        return chr(ord(s) + 32)                        # 将大写转换成小写



def test():
    solution = Solution()

    inputs = "A man, a plan, a canal: Panama"
    expect = True
    result = solution.isPalindrome(s=inputs)
    result = solution.isPalindrome_3(s=inputs)
    assert result == expect

    inputs = "race a car"
    expect = False
    result = solution.isPalindrome(s=inputs)
    result = solution.isPalindrome_3(s=inputs)
    assert result == expect

    inputs = "ab_a"
    expect = True
    result = solution.isPalindrome(s=inputs)
    result = solution.isPalindrome_3(s=inputs)
    assert result == expect

    inputs = "OP"
    expect = False
    result = solution.isPalindrome(s=inputs)
    result = solution.isPalindrome_3(s=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
