from typing import List


class Solution:

    """
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

    不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-string
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = ""
        curr_index = 0
        last_index = len(s) - 1
        while curr_index < last_index:
            tmp = s[curr_index]
            s[curr_index] = s[last_index]
            s[last_index] = tmp
            curr_index += 1
            last_index -= 1

    def reverseString_2(self, s: List[str]) -> None:
        curr_index = 0
        last_index = len(s) - 1
        while curr_index < last_index:
            s[curr_index], s[last_index] = s[last_index], s[curr_index]
            curr_index += 1
            last_index -= 1

    def reverseString_3(self, s: List[str]) -> None:
        s = s[::-1]


def test():
    solution = Solution()

    result = ["h", "e", "l", "l", "o"]
    solution.reverseString_2(s=result)
    assert result == ["o", "l", "l", "e", "h"]

    result = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString_2(s=result)
    assert result == ["h", "a", "n", "n", "a", "H"]

    result = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ",
              "a", " ", "c", "a", "n", "a", "l", ":", " ", "P", "a", "n", "a", "m", "a"]
    expect = ["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ", "a",
              " ", ",", "n", "a", "l", "p", " ", "a", " ", ",", "n", "a", "m", " ", "A"]
    solution.reverseString_2(s=result)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
