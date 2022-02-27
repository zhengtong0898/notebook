# 归并排序
# 原理: https://www.bilibili.com/video/BV1et411N7Ac
# 参考: https://www.geeksforgeeks.org/merge-sort/
#      https://www.programiz.com/dsa/merge-sort
# 时间复杂度: Average-O(n log n)    Worst-O(n2)    Best-O(n*log n)    Space-O(log n)    Stability-No
import random


def merge_sort(items):

    if len(items) <= 1:
        return None

    # 对半除数
    # 左侧数量要么 == 右侧数量
    # 左侧数量要么 == 右侧数量 - 1
    mid = len(items) // 2

    # 切割成 left 和 right 两个列表
    left = items[:mid]
    right = items[mid:]

    # 递归
    #
    # 情况-1: 初期阶段 -> 层层递进
    # 持续对半除，直到 len(left) == 1, len(right) == 1, 停止递进, 进入下面的 while 代码.
    #
    # 情况-2: 中期阶段 -> 层层回归
    # len(left) 可能会 > 1 , 隐藏条件: 此时 left 列表时一个有序列表.
    # len(right) 也可能会 > 1 , 隐藏条件: 此时 left 列表时一个有序列表.
    # 对两个有序列表的比较, 就是用两个游标分别标记在两个列表的第0个位置,
    # 比较后将小的提取出来, 然后小的那个列表游标右移一位.
    merge_sort(left)
    merge_sort(right)

    l = r = i = 0                               # l是left的游标; r是right的游标; i是items的游标;

    # items 是两个列表总合的长度;
    # items 会被接下来的代码重写称为一个有序列表;
    while l < len(left) and r < len(right):     # 当 游标l 和 游标r 都没有越界时, 进入循环.
        if left[l] < right[r]:                  # 当 左侧元素 小于 右侧元素 时,
            items[i] = left[l]                  # 将小的元素(左侧元素)写入到items[i]的位置, 即items是一个有序列表.
            l += 1                              # 游标l 右移一步(也就是游标i递增1), 为下一次比较做准备.
        else:                                   # 当 左侧元素 大于 右侧元素 时,
            items[i] = right[r]                 # 将小的元素(右侧元素)写入到items[i]的位置, 即items是一个有序列表.
            r += 1                              # 游标j 右移一步(也就是游标j递增1), 为下一次比较做准备.
        i += 1                                  # 游标i递增1, 为下一次写入做准备.

    # 游标还没有右移到 left 列表的尽头,
    # 将后续所有元素都写入到 items 末端.
    while l < len(left):
        items[i] = left[l]
        l += 1
        i += 1

    # 游标还没有右移到 right 列表的尽头,
    # 将后续所有元素写入到 items 末端.
    while r < len(right):
        items[i] = right[r]
        r += 1
        i += 1


if __name__ == '__main__':
    collection = random.sample(range(0, 20), 10)
    sorted_collection = sorted(collection)
    merge_sort(collection)
    assert collection == sorted_collection
