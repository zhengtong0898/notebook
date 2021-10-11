

class Solution:

    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]


def test():
    solution = Solution()

    inputs_1 = "abcdefg"
    inputs_2 = 2
    expect = "cdefgab"
    result = solution.reverseLeftWords(s=inputs_1, n=inputs_2)
    assert result == expect



def main():
    test()


if __name__ == '__main__':
    main()
