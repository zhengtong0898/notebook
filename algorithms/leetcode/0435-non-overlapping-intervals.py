from typing import List, Tuple


# 题目链接
# https://leetcode-cn.com/problems/non-overlapping-intervals/
class NonOverlappingIntervals:

    def non_overlapping_intervals_lcen(self, intervals: List[List[int]]) -> int:
        """ 时间复杂度: O(NlogN) """

        # end 是上一个元素的末位值
        # counter 时移除总数
        end, counter = 0, 0

        # 按每个元素末位成员来排序.
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        # first 是当前元素的首位值
        # second 时当前元素的末位值
        for first, second in sorted_intervals:

            # 若 当前元素的首位值 大于等于 上一个元素的末位值时, 无重叠.
            if first >= end:
                end = second

            # 重叠情况, 记录移除次数.
            else:
                counter += 1

        return counter

    def non_overlapping_intervals_me(self, intervals: List[List[int]]) -> int:
        """
        思路:
        1. 常规排序
        2. 根据当前元素和下一个元素相比较, 试图将最小的那个留下进行下一次比较.

        python 的 sort() 方法采用 Timsort, 时间复杂度: https://qr.ae/pGNXpz
        最差复杂度: O(NlogN)
        最好复杂度: O(n)
        均摊复杂度: O(NlogN)

        所以当前程序的时间复杂度是: O(NlogN + N)
        """
        removes = set()
        intervals.sort()
        for next_index in range(1, len(intervals)):
            current_index = next_index - 1
            current_interval = intervals[current_index]
            next_interval = intervals[next_index]

            if current_interval == next_interval:
                removes.add(current_index)
                continue

            if current_interval[0] == next_interval[0]:
                removes.add(current_index if current_interval[1] > next_interval[1] else next_index)
                continue

            if current_interval[1] > next_interval[0]:
                removes.add(current_index)

        return len(removes)


def test_1():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    noi = NonOverlappingIntervals()
    assert noi.non_overlapping_intervals_me(intervals) == 1
    assert noi.non_overlapping_intervals_lcen(intervals) == 1


def test_2():
    intervals = [[1, 2], [1, 2], [1, 2]]
    noi = NonOverlappingIntervals()
    assert noi.non_overlapping_intervals_me(intervals) == 2
    assert noi.non_overlapping_intervals_lcen(intervals) == 2


def test_3():
    intervals = [[1, 2], [2, 3]]
    noi = NonOverlappingIntervals()
    assert noi.non_overlapping_intervals_me(intervals) == 0
    assert noi.non_overlapping_intervals_lcen(intervals) == 0


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
