from typing import List


class Solution:

    """
    从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。
    2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。


    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def isStraight(self, nums: List[int]) -> bool:
        # 双指针/双索引
        curr_index, next_index = 0, 1

        # 字母数字映射表
        all_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
                   10: 10, 11: 11, 12: 12, 13: 13, "A": 1, "J": 11, "Q": 12, "K": 13}

        # 如果有4个0、5个0, 则表示顺子
        if nums.count(0) >= 4:
            return True

        # 0 可以变成任何数, 所以先把 0 取出来.
        zero_size = len([i for i in nums if i == 0])
        nums = sorted([all_map[i] for i in nums if i != 0])

        while next_index < len(nums):
            a = nums[curr_index]
            b = nums[next_index]

            if a + 1 != b:

                # 0 可以变成任何数
                if zero_size:
                    zero_size -= 1

                    for i in range(next_index, len(nums)):
                        nums[i] -= 1

                    continue

                return False

            curr_index += 1
            next_index += 1
        return True

    def isStraight_2(self, nums: List[int]) -> bool:
        # 如果有4个0、5个0, 则表示顺子
        if nums.count(0) >= 4:
            return True

        # 0 可以变成任何数, 所以先把 0 取出来.
        nums.sort()
        zero_size = nums.count(0)

        # 双指针/双索引
        curr_index, next_index = 0 + zero_size, 1 + zero_size

        while next_index < len(nums):
            a = nums[curr_index]
            b = nums[next_index]

            if a + 1 != b:

                # 0 可以变成任何数
                if zero_size:
                    zero_size -= 1

                    for i in range(next_index, len(nums)):
                        nums[i] -= 1

                    continue

                return False

            curr_index += 1
            next_index += 1
        return True


def test():
    solution = Solution()

    inputs = [1, 2, 3, 4, 5]
    expect = True
    result = solution.isStraight(nums=inputs)
    result = solution.isStraight_2(nums=inputs)
    assert result == expect

    inputs = [0, 0, 1, 2, 5]
    expect = True
    result = solution.isStraight(nums=inputs)
    result = solution.isStraight_2(nums=inputs)
    assert result == expect

    inputs = [12, 1, 8, 12, 12]
    expect = False
    result = solution.isStraight(nums=inputs)
    result = solution.isStraight_2(nums=inputs)
    assert result == expect

    inputs = [9, 0, 6, 0, 10]
    expect = True
    result = solution.isStraight(nums=inputs)
    result = solution.isStraight_2(nums=inputs)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()


