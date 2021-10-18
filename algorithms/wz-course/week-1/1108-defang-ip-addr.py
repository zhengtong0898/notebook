

class Solution:

    """
    给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
    所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。

    https://leetcode-cn.com/problems/defanging-an-ip-address/
    """

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
