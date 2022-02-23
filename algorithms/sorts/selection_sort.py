# 选择排序
# 原理: https://www.bilibili.com/video/BV14341177bG
# 参考: https://www.geeksforgeeks.org/python-program-for-selection-sort/
#      https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
# 时间复杂度: 平均复杂度-O(n^2), 最坏复杂度-O(n^2), 最佳复杂度-O(n).
import random
from typing import List


def selection_sort(items: List[int]):

    n = len(items)
    for curr_index in range(n):
        min_index = curr_index
        for next_index in range(curr_index+1, n):
            if items[next_index] < items[min_index]:
                min_index = next_index

        items[curr_index], items[min_index] = items[min_index], items[curr_index]


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    sorted_collection = sorted(collection)
    selection_sort(collection)
    assert collection == sorted_collection
