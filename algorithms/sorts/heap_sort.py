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
    # index   是非叶子节点的最后一个节点的游标.
    # largest 用于标记三个节点中最大的那个节点(父节点以及它的两个子节点)
    largest = index

    # 末梢节点的两个叶节点.
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # 一颗完全二叉树,
    # 它的末梢节点可能会缺失两个叶节点.
    # 它的末梢节点可能会缺失右侧叶节点.
    #
    # left_index < heap_size                     为了防止后面的 unsorted[left_index] 取值超出边界.
    # unsorted[left_index] > unsorted[largest]   当左侧叶子节点 大于 父节点 时, 将 largest 标记到 左侧叶节点的位置.
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    # right_index < heap_size                    为了防止后面的 unsorted[right_index] 取值超出边界.
    # unsorted[right_index] > unsorted[largest]  当右侧叶子节点 大于 父节点 时, 将 largest 标记到 右侧叶节点的位置.
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    # largest != index                           表示父节点并不是最大的那个元素,
    #                                            最大值元素与父节点交换位置, 使每个分支的父节点都是最大的元素.
    #
    # heapify(unsorted, largest, heap_size)      以 largest 作为父节点继续下探比较它的两个子节点, 继续比对和排序.
    #                                            重点: 当 index 是非叶子节点的最后一个节点游标(n-1层最右节点)时, 有效的下探次数是0次.
    #                                                 当 index 是非叶子节点的n-2层时, 有效的下探次数是1次.
    #                                                 当 index 是非叶子节点的n-3层时, 有效的下探次数是2次, 以此类推.
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)

    # 当这个循环执行结束的时候, 将会得出一个大顶堆.
    # 这个循环是从最后一个非叶子节点开始从下往上逐一排序, 最终形成一个大顶堆.
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    # 当这个循环执行结束的时候, 将会得出一个已排序的列表.
    for i in range(n - 1, 0, -1):
        # 由于大顶堆的顶点是最大的那个元素(列表的第0个元素), 每遍历一次就将 0 和 i 交换位置, 意思是将最大的那个元素放到列表相对的最右侧.
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        # 这里每次都从列表的头部重新生成一个新的大顶堆.
        heapify(unsorted, 0, i)

    return unsorted


if __name__ == '__main__':
    # collection = random.sample(range(0, 10), 10)
    collection = [1, 12, 9, 5, 6, 10]
    sorted_collection = sorted(collection)
    assert heap_sort(collection) == sorted_collection
