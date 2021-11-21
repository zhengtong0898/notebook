from typing import List


class Solution:

    """
    42. 接雨水

    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    示例-1:
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/trapping-rain-water
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def trap(self, height: List[int]) -> int:
        """
        单调栈
        它最大的特点就是单调, 也就是**栈中的元素要么递增, 要么递降,
        如果有新的元素不满足这个特点, 就不断的将栈顶元素出栈, 直到满足为止**, 这就是它最重要的思想.
        要么: 后入栈的元素总比栈顶元素小
        要么: 后入栈的元素总比栈顶元素大

        维护一个单调栈, 单调栈存储的是 "下标",
        满足从栈底到栈顶的下标对应的 "数组 height 中的元素递减".

        这里接雨的方式是, 一层一层的接, 先接最低一层, 然后再接第二层, 一次类推(有点类似俄罗斯方块, 一层一层的消).
        """
        result = 0
        stack = []

        for curr, curr_value in enumerate(height):

            while stack and curr_value > height[stack[-1]]:
                prev = stack.pop()
                if not stack: break
                low_level = height[prev]
                curr_width = curr - stack[-1] - 1                      # 计算出有效宽度
                min_height = min(height[stack[-1]], height[curr])      # 比较两个柱子, 取最小的那个柱子的高度
                curr_height = min_height - low_level                   # 最小的柱子高度 - 最低位置, 得出需要有效填充高度
                result += curr_width * curr_height                     # 有效宽度 * 有效填充高度 = 有效填充面积

            stack.append(curr)

        return result

    def trap_v2(self, height: List[int]) -> int:
        """
        观察:
        当值是非零时, 表示柱子左侧高度.
        当下一个位置的值比当前位置的值小时, 表示可以接水,
        但是能接多少水是未知的, 需要先找到右边的柱子.
        右边的柱子要么跟当前位置一样高, 要么高于当前位置.

        解题思路:
        采取和0739-每日温度一样的策略.
        使用双指针来驱动, curr 和 leftmost.
        leftmost 记录的是最左侧柱子.
        这里接雨的方式是一次性填满整个凹槽.
        """
        result = 0
        leftmost = None
        for curr, curr_value in enumerate(height):
            if leftmost is not None:
                if height[leftmost] >= curr_value:
                    if curr + 1 < len(height):
                        if not (height[curr - 1] < curr_value >= height[curr + 1]):         # 不是小山峰, 跳过
                            continue

                        if curr_value < max(height[curr:]):                                 # 还有更高的山峰, 跳过
                            continue

                prev = leftmost
                leftmost = None
                avg = min(curr_value, height[prev])
                for i in height[prev+1: curr]:
                    if i < avg:
                        result += avg - i

            if leftmost is None and curr_value:
                leftmost = curr

        return result


def main():
    ss = Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert ss == 6
    ss = Solution().trap(height=[4, 2, 0, 3, 2, 5])
    assert ss == 9
    ss = Solution().trap(height=[2, 0, 2])
    assert ss == 2
    ss = Solution().trap(height=[5, 4, 1, 2])
    assert ss == 1


if __name__ == '__main__':
    main()
