# 冒泡排序
# 原理: https://www.bilibili.com/video/BV1Zz4y1D7ZE/?spm_id_from=trigger_reload
# 参考: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# 时间复杂度: 平均复杂度-O(n^2), 最坏复杂度-O(n^2), 最佳复杂度-O(n).
import random
from typing import List


def bubble_sort(items: List[int]):
    n = len(items)

    for i in range(0, n - 1):

        # 当 x = 0 时, 表示已经有0个排好序.
        # 当 x = 1 时, 表示已经有1个排好序, 因此少循环一次是合理的.
        # 当 x = 2 时, 表示已经有2个排好序, 因此少循环两次是合理的, 以此类推.
        for j in range(0, n - i - 1):
            curr_index = j
            next_index = j + 1
            if items[curr_index] > items[next_index]:
                items[curr_index], items[next_index] = items[next_index], items[curr_index]


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    sorted_collection = sorted(collection)
    bubble_sort(collection)
    assert collection == sorted_collection
