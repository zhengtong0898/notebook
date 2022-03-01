# 快速排序-分割版本
# 原理: https://www.bilibili.com/video/BV1at411T75o?from=search&seid=16200417356150128649
# 参考: https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py
# 时间复杂度: Average-O(n*log n)    Worst-O(n2)    Best-O(n*log n)    Space-O(log n)    Stability-No
import random


def partition(start, end, array):
    """
    该函数的作用是, 根据 pivot 的值来移动元素,
    将小于 pivot 的值放在列表的左侧,
    将大于 pivot 的值放在列表的右侧,
    最后将 pivot 的值放在 start 和 end 游标相交的地方.
    最终的 pivot 就是整个列表中唯一可以确定是排好序的位置.
    """

    # why: 这里为什么要 pivot_index = start 而不是直接  pivot_index = 0 ?
    # ans: 因为 partition 函数不知道外部传入进来的start是什么, 所以不能直接写 0.
    #
    # why: 这里为什么要 pivot = array[pivot_index] 而不是直接  pivot = array[start] ?
    # ans: 其实是可以的, 因为代码在这里时是处于初始阶段, start游标还没有被改动.
    pivot_index = start
    pivot = array[pivot_index]

    # 这个循环试图找出start和end游标交叉的点.
    while start < end:

        # 代码含义1: start  < len(array)    是为了防止后面的 array[start] 取值超出边界.
        # 代码含义2: pivot >= array[start]  表示 pivot 还没有到位置交换的时机, start游标右移一位, 静待start和end相交.
        while start < len(array) and pivot >= array[start]:
            start += 1

        # 代码含义1: pivot < array[end]     表示 pivot 还有向左移动的空间, end游标左移一位, 静待start和end相交.
        while pivot < array[end]:
            end -= 1

        # 代码含义1: start < end            表示它们两还没有相交.
        # 代码含义2: a, b = b, a            表示将 左侧大于pivot的值 与 右侧小于pivot的值 进行 位置交换.
        if start < end:
            array[start], array[end] = array[end], array[start]

    # why: 这里为什么是 end 和 pivot_index 这两个游标值交换, 而不是 start 和 pivot_index 这两个游标值交换呢?
    # ans: 已知 start游标对应的值 一定是大于 pivot 的, 所以不可以用 start 和 pivot_index 这两个游标交换.
    # 情况: 交换位置后, end位置左侧的所有元素都小于 pivot, end位置右侧的所有元素都大于 pivot.
    # 重点: pivot所在的位置就是一个排好序的位置, 每次循环其实有效的排序就是pivot.
    array[end], array[pivot_index] = array[pivot_index], array[end]

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
    # collection = [5, 4, 3, 2, 1]
    # collection = [4, 16, 8, 9, 10, 1, 2]
    sorted_collection = sorted(collection)
    quick_sort(0, len(collection) - 1, collection)
    assert collection == sorted_collection
    # collection = [2, -1, 6, -10, -8, -4, -9, 8, 4, -3]
    # quick_sort(collection)
