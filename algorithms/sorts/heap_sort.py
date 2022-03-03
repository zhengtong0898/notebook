# 桶排序
# 原理: https://www.cs.usfca.edu/~galles/visualization/HeapSort.html
# 参考: https://github.com/TheAlgorithms/Python/blob/master/sorts/heap_sort.py
#      https://www.programiz.com/dsa/heap-sort
# 时间复杂度: Average-O(n*log n)    Average-O(n*log n)     Average-O(n*log n)    Space-O(1)    Stability-No
import random


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == '__main__':
    # collection = random.sample(range(0, 10), 10)
    collection = [1, 12, 9, 5, 6, 10]
    sorted_collection = sorted(collection)
    assert heap_sort(collection) == sorted_collection
