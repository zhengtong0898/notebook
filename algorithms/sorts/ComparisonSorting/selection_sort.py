# 选择排序
# 原理: https://www.bilibili.com/video/BV14341177bG
#      https://www.programiz.com/dsa/selection-sort
# 参考: https://www.geeksforgeeks.org/python-program-for-selection-sort/
#      https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
# 时间复杂度: Average-O(n^2)    Worst-O(n^2)    Best-O(n^2)    Space-O(1)    Stability-No
import random
from typing import List


def selection_sort(items: List[int]):

    n = len(items)
    for curr_index in range(n):

        # 向右遍历, 找到最小的那个元素.
        min_index = curr_index
        for next_index in range(curr_index+1, n):
            if items[next_index] < items[min_index]:
                min_index = next_index

        # 最小元素的 跟 当前元素交换;
        # 隐藏条件: 当前元素位置左侧(含当前元素)的所有元素都是排过序的.
        items[curr_index], items[min_index] = items[min_index], items[curr_index]


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    sorted_collection = sorted(collection)
    selection_sort(collection)
    assert collection == sorted_collection
