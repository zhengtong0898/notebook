

class Solution:

    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")

    def replaceSpace_2(self, s: str) -> str:
        return "".join(["%20" if i == " " else i for i in s])

    def replaceSpace_3(self, s: str) -> str:
        ss = ""
        index = 0
        while index < len(s):
            if s[index] != " ":
                ss += s[index]
            else:
                ss += "%20"
            index += 1
        return ss


def test():
    solution = Solution()

    inputs = "We are happy."
    expect = "We%20are%20happy."
    result = solution.replaceSpace(s=inputs)
    result = solution.replaceSpace_2(s=inputs)
    result = solution.replaceSpace_3(s=inputs)
    assert result == expect



def main():
    test()


if __name__ == '__main__':
    main()
