# 桶排序
# 原理: https://www.cs.usfca.edu/~galles/visualization/HeapSort.html
# 参考: https://github.com/TheAlgorithms/Python/blob/master/sorts/heap_sort.py
#      https://www.programiz.com/dsa/heap-sort
#      https://zhuanlan.zhihu.com/p/153216919
#      https://baike.baidu.com/item/%E5%A0%86/20606834
# 时间复杂度: Average-O(n*log n)    Average-O(n*log n)     Average-O(n*log n)    Space-O(1)    Stability-No
import random


"""
什么是堆?
堆通常是一个可以被看做一棵完全二叉树的数组对象.  

什么是二叉树?  
二叉树是每个节点最多有两个子树的有序树.  

什么是满二叉树?  
一棵树的所有节点都有两个子节点.

什么是完全二叉树?  
判断一棵树是否是完全二叉树，也可以将节点逐一放到数组中，若中间没有缝隙(不产生空余的存储位置)，那么就是完全二叉树了.    

什么是非完全二叉树?  
将节点逐一放到数组中，若中间有缝隙(不产生空余的存储位置)，那么就是非完全二叉树了.  


堆排序

一个列表可以被看作是二叉树.  
(列表长度 // 2) - 1  ==  node(最后一个非叶节点位置).  
列表最后一个元素      ==  leaf(最后一个叶子节点位置).  

通过 leaf 和 node 比较, 将大元素移动到 node 位置, 小元素移动到 leaf 位置.
反复循环这个过程, 完成整棵树的排序, 使顶部元素总是大于子元素.  


"""


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
