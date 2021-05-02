from typing import List


# 题目链接
# https://leetcode-cn.com/problems/non-decreasing-array/
class NonDecreasingArray:

    def non_decreasing_array(self, nums: List[int]) -> bool:
        # 递减数组指的是每个元素都是一个比一个少(并不是递减1的意思).
        # 数组中只要任意一个成员比上一个成员大, 则不是递减数组.
        #
        # 非递减数组定义: nums[i] <= nums[i+1].
        # 理解: 任意两个元素, 只要值规律是 a <= b, 则视为非递归数组(等于不是, 小于也不是).
        count = 0
        for ni in range(1, len(nums)):          # ni == next_index
            ci = ni - 1                         # ci == current_index
            cn, nn = nums[ci], nums[ni]         # cn == current_num ,  nn == next_num

            if cn > nn:                         # current_num > next_num == 递减数组
                count += 1

                if count > 1:                   # 是递减数组
                    return False

                if ci > 0:
                    pn = nums[ci - 1]           # pn == previous_num

                    if nn < pn:                 # nn 即小于 pn 也小于 cn, 这是一个递减数组
                        nums[ni] = cn           # 这里尝试更改 nn 的值; 采用 cn 的值来, 使 nn == cn, 符合非递减数组.

        return True


def test_1():

    nums = [4, 2, 3]
    nda = NonDecreasingArray()
    ss = nda.non_decreasing_array(nums)
    assert ss is True


def test_2():

    nums = [4, 2, 1]
    nda = NonDecreasingArray()
    ss = nda.non_decreasing_array(nums)
    assert ss is False


def main():

    test_1()
    test_2()


if __name__ == '__main__':
    main()

