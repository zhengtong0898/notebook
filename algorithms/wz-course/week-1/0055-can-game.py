from typing import List


class Solution:

    """
    给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

    数组中的每个元素代表你在该位置可以跳跃的最大长度。

    判断你是否能够到达最后一个下标。

    https://leetcode-cn.com/problems/jump-game/
    """

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True

        jumped = 0
        curr_index = 0
        while curr_index <= jumped:
            # 当前位置 + 当前位置的值 == 下一跳的值;
            can_jump = curr_index + nums[curr_index]
            # 所以现在有两个可以选择的值: 1. 已跳的值; 2. 下一跳的值; 比较两个值, 谁大选谁.
            jumped = max(can_jump, jumped)
            # len(nums) - 1 的原因是, jumped 是从 0 开始的;
            # jumped >= len(nums) - 1 表示: 当前位置加上下一跳的值, 抵达了最后一个元素.
            if jumped >= len(nums) - 1:
                return True
            curr_index += 1

        return False

        # cover = 0
        # for index, i in enumerate(nums):
        #     can_jump = nums[index]
        #
        #     cover = max(i + nums[index], cover)
        #     if cover >= len(nums):
        #         return True
        #
        # return False


def test():
    solution = Solution()

    inputs = [2, 3, 1, 1, 4]
    expect = True
    result = solution.canJump(nums=inputs)
    assert result == expect

    inputs = [3, 2, 1, 0, 4]
    expect = False
    result = solution.canJump(nums=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()