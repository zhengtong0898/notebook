from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        1. 由于 nums 是一个已排序的数组, 所以只要保留第一个, 后续相同的都可以删除掉.
        2. 当执行删除动作时 curr_index 不递增, 当没有执行删除动作时 curr_index 需要递增.

        这种写法的缺点:
        使用了 pop(index), 增加了时间复杂度pop(index)==O(n), pop()==O(1), 降低了执行效率.
        """
        curr_index = 0
        last_char = ""
        while curr_index < len(nums):
            if nums[curr_index] != last_char:
                last_char = nums[curr_index]
                curr_index += 1
            else:
                nums.pop(curr_index)
        return len(nums)

    def removeDuplicates_2(self, nums: List[int]) -> int:
        """
        由于 nums 是一个已排序的数组, 所以只要保留第一个, 后续相同的都可以删除掉.
        curr_index 是字符第一次出现的位置,
            如果 next_index 与 curr_index 一样则表示, 有重复的字符, 此时 next_index 递增 1, curr_index 不变.
            如果 next_index 与 curr_index 不同则表示, 无重复的字符,
            此时 next_index 所在的字符需要挪到 curr_index + 1 的位置,
            并且 curr_index 需要递增 1, next_index 需要递增 2.
        """
        curr_index, next_index = 0, 1
        while next_index < len(nums):
            if nums[curr_index] == nums[next_index]:
                next_index += 1
            else:
                curr_index += 1
                nums[curr_index] = nums[next_index]
        return curr_index + 1


def test():
    solution = Solution()

    inputs_1 = [1, 1, 2]
    expect_1 = 2
    expect_2 = [1, 2]
    result = solution.removeDuplicates(nums=inputs_1)
    result = solution.removeDuplicates_2(nums=inputs_1)
    assert result == expect_1
    assert inputs_1[0:2] == expect_2

    inputs_1 = [0,0,1,1,1,2,2,3,3,4]
    expect_1 = 5
    expect_2 = [0,1,2,3,4]
    result = solution.removeDuplicates_2(nums=inputs_1)
    assert result == expect_1
    assert inputs_1[0:5] == expect_2


def main():
    test()


if __name__ == '__main__':
    main()
