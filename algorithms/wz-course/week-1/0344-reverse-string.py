from typing import List


class Solution:

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
