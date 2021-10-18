from typing import List


class Solution:

    """
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

    你可以按任意顺序返回答案。

    https://leetcode-cn.com/problems/two-sum/
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        当前的写法是: A下标 永远小于 B下标.
        最好情况的时间复杂度是: O(1).
        最坏情况的时间复杂度是: O(n^2), 即: (n * (n - 1)) / 2.

        这段代码等同于:
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i + 1, num_len):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        curr_index = 0
        next_index = 1
        num_len = len(nums)
        while curr_index < num_len:
            if (nums[curr_index] + nums[next_index]) == target:
                return [curr_index, next_index]

            next_index += 1
            if next_index >= num_len:
                curr_index += 1
                next_index = curr_index + 1
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

    inputs = [2, 7, 11, 15]
    expect = [0, 1]
    result = solution.twoSum(nums=inputs, target=9)
    assert result == expect

    inputs = [3, 2, 4]
    expect = [1, 2]
    result = solution.twoSum(nums=inputs, target=6)
    assert result == expect

    inputs = [3,3]
    expect = [0, 1]
    result = solution.twoSum(nums=inputs, target=6)
    assert result == expect

    inputs = [2, 5, 5, 11]
    expect = [1, 2]
    result = solution.twoSum(nums=inputs, target=10)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
