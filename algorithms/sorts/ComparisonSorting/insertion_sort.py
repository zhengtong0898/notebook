# 插入排序
# 原理: https://www.bilibili.com/video/BV1Ck4y1B7N4
#      https://www.programiz.com/dsa/insertion-sort
# 参考: https://www.geeksforgeeks.org/insertion-sort/
# 时间复杂度: Average-O(n2)    Worst-O(n2)    Best-O(n)    Space-O(1)    Stability-Yes
import random
from typing import List, Union


def insertion_sort(items: List[Union[int, None]]):
    n = len(items)
    for i in range(1, n):

        # 将 key 提取出来, 它原来所在的地方会被覆盖掉.
        key = items[i]

        # left_index 是插入排序的关键游标.
        # left_index 可用来做持续左移前置游标.
        left_index = i - 1

        while True:

            # 处理越界防护 -> items[left_index]
            if left_index < 0:
                break

            # items[left_index] 是前置值,
            # 隐藏条件: items[:i] 的这些元素都是排过序的.
            # 所以当 key >= 前置值, 表示顺序没问题不需要做任何操作, 跳出当前循环.
            if key >= items[left_index]:
                break

            # key < 前置值, 将前置值右移一位.
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
