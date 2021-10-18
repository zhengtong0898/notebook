from typing import List


class Solution:
    """
    你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，
    长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

    返回的长度需要从小到大排列。

    https://leetcode-cn.com/problems/diving-board-lcci/

    已知条件:
    1. 只有两个对象, longer 和 shorter.
    2. shorter <= longer.
    3. 0 <= k <= 100000.

    输入：
    shorter = 1
    longer = 2
    k = 3
    输出： [3,4,5,6]
    解释：
    可以使用 3 次 shorter，得到结果 3；使用 2 次 shorter 和 1 次 longer，得到结果 4 。以此类推，得到最终结果。
    """
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        """
        如果 k = 3, 则: 3 可以分成 1 和 2; 3也可以分成 2 和 1;
        这已经是所有组合的可能, 所以按照这个方式来编码.
        """
        if k <= 0: return []
        if shorter == longer: return [shorter * k]
        result = [shorter * k, longer * k]

        power_shorter = 1
        while k > power_shorter:
            power_longer = k - power_shorter
            result.append((power_shorter * shorter) + (power_longer * longer))
            power_shorter += 1

        result.sort()
        return result


def test():
    solution = Solution()

    shorter = 1
    longer = 1
    k = 3
    expect = [3, 4, 5, 6]
    result = solution.divingBoard(shorter=shorter, longer=longer, k=k)
    assert result == expect

    shorter = 1
    longer = 1
    k = 0
    expect = []
    result = solution.divingBoard(shorter=shorter, longer=longer, k=k)
    assert result == expect

    shorter = 1
    longer = 1
    k = 100000
    expect = [100000]
    result = solution.divingBoard(shorter=shorter, longer=longer, k=k)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
