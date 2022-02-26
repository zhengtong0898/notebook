# 快速排序-递归版本
# 原理: https://www.bilibili.com/video/BV1at411T75o?from=search&seid=16200417356150128649
# 参考: https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py
# 时间复杂度: Average-O(n*log n)    Worst-O(n2)    Best-O(n*log n)    Space-O(log n)    Stability-No
import random


def quick_sort(items: list) -> list:
    # 递归保护边界取值异常
    if len(items) < 2:
        return items

    # 取第一个值做 pivot.
    pivot = items.pop()
    left, right = [], []

    # 将元素按 pivot 值来划分.
    # 小于 pivot 的值全部放置到 left 列表中.
    # 大于 pivot 的值全部放置到 right 列表中.
    for item in items:
        (right if item > pivot else left).append(item)

    # 递归处理左边的列表
    left_result = quick_sort(left)

    # 递归处理右边的列表
    right_result = quick_sort(right)

    return left_result + [pivot] + right_result


if __name__ == '__main__':
    collection = random.sample(range(-30, 30), 30)
    sorted_collection = sorted(collection)
    assert quick_sort(collection) == sorted_collection
    # collection = [2, -1, 6, -10, -8, -4, -9, 8, 4, -3]
    # quick_sort(collection)
