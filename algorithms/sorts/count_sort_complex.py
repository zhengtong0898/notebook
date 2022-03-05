# 计数排序
# 原理:      https://www.bilibili.com/video/BV1KU4y1M7VY
# 参考:      https://www.geeksforgeeks.org/counting-sort/?ref=lbp
#           https://www.programiz.com/dsa/counting-sort
#           https://github.com/TheAlgorithms/Python/blob/master/sorts/counting_sort.py
#           https://www.cs.usfca.edu/~galles/visualization/CountingSort.html
# 时间复杂度: Average-O(n+k)    Average-O(n+k)     Average-O(n+k)    Space-O(max)    Stability-yes
# 困难程度:   Easy
import random


def count_sort(items):
    max_value, min_value = int(max(items)), int(min(items))  # 像桶排序一样, 计算出最大值和最小值
    count_size: int = int(max_value - min_value) + 1         # 像桶排序一样, 计算出计数列表的有效范围
    count_items = [0 for _ in range(count_size)]             # 像桶排序一样, 创建一个跟有效范围一样长度的列表.

    ordered_items = [0 for _ in range(len(items))]           # 创建一个有序列表, 长度与原始列表一致.

    for i in range(0, len(items)):
        index = items[i] - min_value                         # 两个实际值相减, 得出相对的索引位置.
        count_items[index] += 1                              # 因此采用递增来记录相同值的次数.

    for i in range(1, len(count_items)):
        count_items[i] += count_items[i - 1]                 # 推算出实际值(从右往左)的索引位置, 这里无法言传只能debug去感受.

    for i in range(len(items) - 1, -1, -1):
        count_index = items[i] - min_value                   # 得出count_items的索引位置
        stable_index = count_items[count_index] - 1          # 得出items[i]的相对位置, 这就是该算法被称为稳定的关键步骤.
        ordered_items[stable_index] = items[i]               # 从原列表中的值写入, 而不是重新计算一个相同的值来写入.
        count_items[items[i] - min_value] -= 1               # 写入后通过递减1来表示下一次相同值应该写入到左侧索引位置.

    # TODO: 为什么这里要讲数据拷贝给items?
    #       感觉有点多余, 因为如果像C语言那样将变更作用在原数组中, 那么则不需要返回items.
    #       如果这里返回items, 那么跟直接返回sorted并没有太大的区别.
    # Copy the output array to items, so that items now
    # contains sorted characters.
    # for i in range(0, len(items)):
    #     items[i] = ordered_items[i]
    #
    # return items

    return ordered_items


if __name__ == '__main__':
    # collection = random.sample(range(-50, 50), 50)
    collection = [2, 5, 1, 2, 2, 5, 1, 1]
    sorted_collection = sorted(collection)
    assert count_sort(collection) == sorted_collection

