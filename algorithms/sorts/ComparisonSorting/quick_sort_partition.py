# 快速排序-
# 原理: https://www.bilibili.com/video/BV1at411T75o?from=search&seid=16200417356150128649
# 参考: https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py
# 时间复杂度: Average-O(n*log n)    Worst-O(n2)    Best-O(n*log n)    Space-O(log n)    Stability-No
import copy
import random


# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
    array_copied = copy.deepcopy(array)

    # why: 这里为什么要 pivot_index = start         而不是直接  pivot_index = 0 ?
    # ans: 因为 partition 函数不知道外部传入进来的start是什么, 所以不能直接写 0 .
    #
    # why: 这里为什么要 pivot = array[pivot_index] 而不是直接  pivot = array[start] ?
    # ans: 因为 start 是一个游标, 它的值会发生变化, 所以在在它发生变化之前, 使用 pivot_index 来记录它初始的状态.
    pivot_index = start
    pivot = array[pivot_index]

    # 这个循环试图找出start和end游标交叉的点,
    # 当交叉点出现时意味着: start游标位置的值一定大于 pivot值
    #                   end游标位置的值一定小于 pivot值
    while start < end:

        # 游标start所在位置的值 <= pivot 时, 游标start递增1.
        # 目的: 试图将start右侧邻近的, 并且 <= pivot 的值, 通过游标start递增1的方式记录下来.
        while start < len(array) and array[start] <= pivot:
            start += 1

        # 游标end所在位置的值 > pivot 时, 游标end递减1.
        # 目的: 试图将end左侧邻近的, 并且 > pivot 的值, 通过游标end递减1的方式记录下来.
        while array[end] > pivot:
            end -= 1

        # 此时
        # 1. 游标start所在的位置的值 > pivot
        # 2. 游标end所在的位置的值 < pivot
        # 动作: 将start和end位置的值进行互换.
        # 目的: 试图将小于pivot的值归放置在pivot右侧邻近位置, 以便下次循环时可以继续移动start游标和end游标.
        if start < end:
            array[start], array[end] = array[end], array[start]

    # 将 end游标所在位置的值 与 pivot_index所在位置的值 交换位置.
    # 目的: 交换位置后, end位置左侧的所有元素都小于 pivot, end位置右侧的所有元素都大于 pivot.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # 返回 end 游标, 此时 end 就是一个很分割点, 所以这个函数叫做 partition.
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if start >= end:
        return None

    p = partition(start, end, array)

    quick_sort(start, p - 1, array)
    quick_sort(p + 1, end, array)


if __name__ == '__main__':
    collection = random.sample(range(0, 20), 10)
    collection_copied = copy.deepcopy(collection)
    sorted_collection = sorted(collection)
    quick_sort(0, len(collection) - 1, collection)
    assert collection == sorted_collection
    # collection = [2, -1, 6, -10, -8, -4, -9, 8, 4, -3]
    # quick_sort(collection)
