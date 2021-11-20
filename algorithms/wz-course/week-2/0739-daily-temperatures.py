from typing import List


class Solution:

    """
    739. 每日温度

    请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。
    如果气温在这之后都不会升高，请在该位置用 0 来代替。

    示例-1
    输入: temperatures = [73,74,75,71,69,72,76,73]
    输出: [1,1,4,2,1,1,0,0]

    示例-2
    输入: temperatures = [30,40,50,60]
    输出: [1,1,1,0]

    示例-3
    输入: temperatures = [30,60,90]
    输出: [1,1,0]

    https://leetcode-cn.com/problems/daily-temperatures/
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        思路:
        正常思维是说采用双指针, curr 和 curr+1, curr+2, curr+3, ... 这种方式一直比较下去.
        这种解题思路的时间复杂度是O(n^2).

        要想将时间复杂度下降到 O(n), 就得换一种稍微逆向的思路才能行得通.
        也是采用双指针, 第一个指针是遍历 temperatures 时的 curr指针, 第二个指针是保存在 stack 中的prev指针.
        当 stack 为空时, curr指针会被压入到stack栈顶.
        当 stack 不为空时, 就会使用 temperatures[stack[-1]] 与 curr_temp 进行比较.
        当 stack 栈中存在多个值时, 栈尾到栈顶所对应的值是递减的, 栈顶到栈尾所对应的值是递增的, 即: 后入栈的元素总比栈顶元素小.

        loop - 比较当前元素与栈顶元素的大小:
            如果栈顶元素 >= 当前元素: 入栈(stack.append(curr))
            如果栈顶元素 <  当前元素: 满足出栈条件, 将索引位置移除栈顶(prev), 连续温度升高天数 = curr - prev.

        总结:
        这种逆向比较的方式，它主要的特点是缩短了比较范围.
        """
        stack = []
        result = [0] * len(temperatures)
        for curr, curr_temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < curr_temp:   # 当 stack 不为空时, 才能进入循环.
                prev = stack.pop()
                result[prev] = curr - prev                         # prev 是对应与 temperatures 的索引位置,
                                                                   # 写入 result[prev] 也是与 temperatures 的位置一一对应.

            stack.append(curr)                                     # 当 stack 为空时, 将 curr指针压入stack栈顶.
        return result

    def dailyTemperatures_v2(self, temperatures: List[int]) -> List[int]:
        """
        时间复杂度: O(n^2)
        超出时间限制
        """
        result = [0] * len(temperatures)
        for curr, curr_temp in enumerate(temperatures):
            for dump, dump_temp in enumerate(temperatures[curr+1:]):
                if dump_temp > curr_temp:
                    result[curr] = dump+1
                    break
        return result

    def dailyTemperatures_v3(self, temperatures: List[int]) -> List[int]:
        """
        思路:
        使用双指针: curr, dump
        curr: 当前遍历位置
        dump: 用于探测连续高温天数, dump 位置的初始是 curr + 1

        时间复杂度: O(n^2)
        超出时间限制
        """
        result = []
        for curr, curr_temp in enumerate(temperatures):
            count = 1
            dump = curr + count
            while dump < len(temperatures):
                dump_temp = temperatures[dump]
                if dump_temp > curr_temp: break
                dump += 1
                count += 1
            else:
                count = 0
            result.append(count)

        return result


def main():
    ss = Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
    assert ss == [1, 1, 4, 2, 1, 1, 0, 0]
    ss = Solution().dailyTemperatures(temperatures=[30, 40, 50, 60])
    assert ss == [1, 1, 1, 0]
    ss = Solution().dailyTemperatures(temperatures=[30, 60, 90])
    assert ss == [1, 1, 0]




if __name__ == '__main__':
    main()