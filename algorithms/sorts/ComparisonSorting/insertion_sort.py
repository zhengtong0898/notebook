# 插入排序
# 原理: https://www.bilibili.com/video/BV1Ck4y1B7N4
#      https://www.programiz.com/dsa/insertion-sort
# 参考: https://www.geeksforgeeks.org/insertion-sort/
# 时间复杂度: Average-O(n2)    Worst-O(n2)    Best-O(n)    Space-O(1)    Stability-Yes
import random
from typing import List, Union


def insertion_sort(items: List[Union[int, None]]):
    """
    两个循环, 外部循环向右遍历, 内部循环向左遍历.
    """

    n = len(items)
    for i in range(1, n):

        # 将 key 提取出来, 它原来所在的地方会被覆盖掉.
        key = items[i]

        # left_index 是插入排序的关键游标.
        # left_index 可用来做持续左移前置游标.
        left_index = i - 1

        # 代码含义1: left_index >= 0          是为了防止后面的 items[left_index] 取值超出边界.
        # 代码含义2: items[left_index] > key  表示"左大右小"不符合顺序预期, 需要将左侧大的值右移.
        # 隐藏信息:  items[:i]                的元素都是排过序的.
        while left_index >= 0 and items[left_index] > key:
            # 将前置值右移一位.
            items[left_index + 1] = items[left_index]
            # 置空前置值所在的槽位.
            items[left_index] = None
            # 前置游标左移一位, 为下一次比较做准备.
            left_index -= 1

        # 由于前置值所在的槽位已被置空, 这里需要将key吸入到该槽位中来.
        items[left_index + 1] = key


if __name__ == '__main__':
    collection = random.sample(range(0, 20), 20)
    sorted_collection = sorted(collection)
    insertion_sort(collection)
    assert collection == sorted_collection
