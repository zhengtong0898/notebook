from typing import List


class Solution:

    """
    84. 柱状图中最大的矩形

    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。

    示例-1:
    输入：heights = [2,1,5,6,2,3]
    输出：10
    解释：最大的矩形为图中红色区域，面积为 10

    示例-2:
    输入： heights = [2,4]
    输出： 4

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        heights.append(0) 这个前置操作, 是为了消除更多的 if 判断条件.
        为了让所有情况得到统一的闭环, 代码开始处理之前, 先增加一个前置操作: heights.append(0).
        这个步骤解决的问题是: 当排列顺序是 [1, 2, 3, 4, 5] 这种递增时无法触发的场景, 最后被一个 0 全部收割.

        stack = [-1]
        给 stack 设定初始值, 在 while 进入循环的条件中可以省略掉 stack is True 条件.
        给 stack 设定初始值, 初始值之所以是 -1, 是因为 0 被添加到 heights 的最后一个元素, -1 是该值的对应索引.
        We instantiate the stack with -1 as a reference to the 0 that we added to height.
        我们使用 -1 来实例化 stack 是用来与 heights.append(0) 作为一一对应的依据.

        h = heights[prev],            # heights[prev] 是相邻柱子中高的那个, 所以定义为 h 是合理且正确的.
        w = curr - 1 - stack[-1],     # curr - 1 是右边界, stack[-1] 是左边界, 两个边界相减得出 width.

        参考: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms/492440
        """
        heights.append(0)
        stack = [-1]
        result = 0
        for curr, curr_value in enumerate(heights):
            while stack and heights[stack[-1]] > curr_value:
                prev = stack.pop()
                h = heights[prev]
                w = curr - stack[-1] - 1
                result = max(result, h * w)
            stack.append(curr)
        heights.pop()
        return result

    def largestRectangleArea_v2(self, heights: List[int]) -> int:
        """
        思路:
        单调栈解法

        ss = Solution().largestRectangleArea(heights=[1, 2, 3, 4, 5])
        assert ss == 9
        解题失败
        """
        stack = []
        largest = None
        horizon = 0
        area_horizon = None
        for curr, curr_value in enumerate(heights):

            if not curr_value:
                horizon = curr

            while stack:
                prev = stack.pop()
                prev_value = heights[prev]
                area_rectangle = min(prev_value, curr_value) * 2       # 相邻两列的组合最大有效面积
                area_vertical = max(prev_value, curr_value)            # 相邻两列的单列最大有效面积
                area_largest = max(area_rectangle, area_vertical)      # 两种相邻的面积, 取最大一个作为有效面积.
                largest = max(largest or 0, area_largest)              # 相邻最大面积 和 历史最大面积, 去最大一个作为有效面积

                area_horizon = min(heights[horizon:curr+1])            # 获取横向组合的最大有效面积
                area_horizon = area_horizon * (curr - horizon + 1)     # 获取横向组合的最大有效面积

            stack.append(curr)

        if largest is None:
            prev = stack.pop()
            largest = heights[prev]

        if area_horizon:
            largest = max(largest, area_horizon)

        return largest


def main():
    ss = Solution().largestRectangleArea(heights=[2, 1, 5, 6, 2, 3])
    assert ss == 10
    ss = Solution().largestRectangleArea(heights=[2, 4])
    assert ss == 4
    ss = Solution().largestRectangleArea(heights=[5, 4, 3, 2, 1])
    assert ss == 9
    ss = Solution().largestRectangleArea(heights=[1])
    assert ss == 1
    ss = Solution().largestRectangleArea(heights=[0, 9])
    assert ss == 9
    ss = Solution().largestRectangleArea(heights=[2, 1, 2])
    assert ss == 3
    ss = Solution().largestRectangleArea(heights=[3, 3, 3, 4, 5])
    assert ss == 9


if __name__ == '__main__':
    main()
