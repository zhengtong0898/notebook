from typing import List
from queue import Queue
from collections import deque


class Solution:

    """
    Offer59-I. 滑动窗口的最大值

    给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
    提示: 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

    示例-1:
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    解释:
      滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        解题思路
        https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/dong-hua-yan-shi-dan-diao-dui-lie-jian-z-unpy/

        Python 的 Queue (FIFO: 先进先出)只有四个有效操作方法:
            get:        从队列左侧移除并返回元素(采取堵塞策略).
            put:        将元素添加到队列最右侧.
            empty:      检查队列是否为空.
            qsize:      返回队列中有几个元素

            特殊方法:
            get_nowait: 从队列左侧移除并返回元素(默认采取堵塞策略, 提供参数支持非堵塞策略),
                        非堵塞策略是为了提高并发承载能力.

        Python 的 deque (双向队列, 支持通过索引下标随机访问)有多个有效操作方法:
            pop:        从队列右侧移除并返回元素.
            popleft:    从队列左侧移除并返回元素, 对应 Queue.get.

            append:     将元素添加到队列最右侧, 对应 Queue.put.
            appendleft  将元素添加到队列最左侧.

            insert:     将元素插入到指定的队列下标位置.
            index:      根据索引编号来访问具体位置的值.

        从题解的动画、和java解题的代码来看，
        有一个 "获取最左侧元素但又不移除该元素: peek" 动作,
        Queue 数据结构并不支持 peek 动作, 但 deque 支持.
        所以单调队列方式的话, 使用 deque 更合适,

        这段代码并没有通过全部测试用例.
        """
        result = [0] * (len(nums) - k + 1)
        dq = deque()
        for curr, curr_value in enumerate(nums):

            # 符合条件处理单调队列
            while dq and dq[-1] < curr_value:
                dq.pop()

            # 单调队列添加
            dq.append(curr_value)

            # 计算窗口左边界
            front = curr - k - 1
            if dq[0] < front:
                dq.popleft()

            if front + 1 >= k:
                result[front] = nums[dq.popleft()]

        return result

    def maxSlidingWindow_slow(self, nums: List[int], k: int) -> List[int]:
        """
        解题思路
        维护一个offset 与 k 保持相同距离, 使用切片, 取最大值.

        356ms, 在 python3 提交中击败了 17.59% 的用户, 有点慢了.
        """
        result = []
        offset = 0
        while k <= len(nums):
            max_value = max(nums[offset:k])
            result.append(max_value)
            offset += 1
            k += 1
        return result

    def maxSlidingWindow_withoutK(self, nums: List[int], k: int) -> List[int]:
        """
        脑子不好使, 居然没将 k 考虑进来, 写了个固定式....
        这是一个失败案例.
        """
        result = []
        prev_2, prev_1, curr = 0, 1, 2
        while curr < len(nums):
            max_value = max([nums[prev_2], nums[prev_1], nums[curr]])
            result.append(max_value)
            prev_2 += 1
            prev_1 += 1
            curr += 1
        return result


def main():
    k = 3
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    ss = Solution().maxSlidingWindow(nums=nums, k=k)
    assert ss == [3, 3, 5, 5, 6, 7]


if __name__ == '__main__':
    main()
