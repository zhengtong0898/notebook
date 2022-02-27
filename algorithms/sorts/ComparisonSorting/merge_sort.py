# 归并排序
# 原理: https://www.bilibili.com/video/BV1et411N7Ac
# 参考: https://www.geeksforgeeks.org/merge-sort/
#      https://www.programiz.com/dsa/merge-sort
# 时间复杂度: Average-O(n log n)    Worst-O(n2)    Best-O(n*log n)    Space-O(log n)    Stability-No
import random


def merge_sort(items):

    if len(items) <= 1:
        return None

    # Finding the mid of the array
    mid = len(items) // 2

    # Dividing the array elements
    left = items[:mid]

    # into 2 halves
    right = items[mid:]

    # Sorting the first half
    merge_sort(left)

    # Sorting the second half
    merge_sort(right)

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        items[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        items[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    collection = random.sample(range(0, 20), 10)
    sorted_collection = sorted(collection)
    merge_sort(collection)
    assert collection == sorted_collection
