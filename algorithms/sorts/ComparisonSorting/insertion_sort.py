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
        left_index = i - 1

        # 如果key的值小于左侧的值, key所在的位置将会被前一个值覆盖掉, 前一个值和它所在的位置是一个空槽.
        # 如果key的值持续小于左侧的之, 那么将空槽前一个值放入空槽位置, 并且置空空槽前一个位置的值.
        while left_index >= 0 and key < items[left_index]:
            items[left_index + 1] = items[left_index]
            items[left_index] = None                        # 最佳实践的算法是可以省略掉这一步的.
            left_index -= 1
        items[left_index + 1] = key


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    sorted_collection = sorted(collection)
    insertion_sort(collection)
    assert collection == sorted_collection
