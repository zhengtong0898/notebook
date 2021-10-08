from typing import List


class Solution:

    # 这里虽然是只有一个循环, 但是由于使用了两个游标,
    # 并且这两个游标存在层级关系, 所以这个算法的时间复杂度其实是 n * (n-1) == O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_1 = 0
        pos_2 = 1
        num_len = len(nums)
        while True:
            if (nums[pos_1] + nums[pos_2]) == target:
                return [pos_1, pos_2]

            pos_2 += 1
            if pos_1 >= num_len:
                return [-1, -1]

            if pos_2 >= num_len:
                pos_1 += 1
                pos_2 = pos_1 + 1
                continue

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


def test():
    solution = Solution()
    result = solution.twoSum(nums=[2,5,5,11], target=10)
    assert result == [0, 1]


def main():
    test()


if __name__ == '__main__':
    main()
