from typing import List


class TwoSum:

    # 时间复杂度: O(n^2)
    def two_sum_1(self, nums: List[int], target: int) -> List[int]:
        for inum, i in enumerate(nums):
            for jnum, j in enumerate(nums):
                if i + j == target:
                    return [inum, jnum]
        return []

    # 时间复杂度: O(n)
    def two_sum_2(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, i in enumerate(nums):
            ss = target - i
            if ss in hash_map:
                return [hash_map[ss], index]
            hash_map[i] = index
        return []


def main():

    # 准备数据
    data = [2, 7, 11, 15]
    target = 9

    ts = TwoSum()
    assert ts.two_sum_1(data, target) == [0, 1]
    assert ts.two_sum_2(data, target) == [0, 1]


if __name__ == '__main__':
    main()