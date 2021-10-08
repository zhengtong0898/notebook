

class Solution:

    def defangIPaddr(self, address: str) -> str:
        result = []
        for i in address:
            if i != ".":
                result.append(i)
            else:
                result.append("[.]")
        return "".join(result)

    def defangIPaddr_2(self, address: str) -> str:
        return "".join([i if i != "." else "[.]" for i in address])

    def defangIPaddr_3(self, address: str) -> str:
        return "[.]".join(address.split("."))

    def defangIPaddr_4(self, address: str) -> str:
        return address.replace('.', '[.]')


def test():
    solution = Solution()

    result = solution.defangIPaddr(address="1.1.1.1")
    assert result == "1[.]1[.]1[.]1"

    result = solution.defangIPaddr(address="255.100.50.0")
    assert result == "255[.]100[.]50[.]0"


def main():
    test()


if __name__ == '__main__':
    main()
