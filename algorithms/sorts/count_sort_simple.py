# 计数排序
# 原理:      https://www.bilibili.com/video/BV1ML411n7ox
# 参考:      https://www.geeksforgeeks.org/counting-sort/?ref=lbp
#           https://www.programiz.com/dsa/counting-sort
#           https://github.com/TheAlgorithms/Python/blob/master/sorts/counting_sort.py
#           https://www.cs.usfca.edu/~galles/visualization/CountingSort.html
# 时间复杂度: Average-O(n+k)    Average-O(n+k)     Average-O(n+k)    Space-O(max)    Stability-No
# 困难程度:   Easy


def count_sort(items):
    max_value, min_value = int(max(items)), int(min(items))  # 像桶排序一样, 计算出最大值和最小值
    count_size: int = int(max_value - min_value) + 1         # 像桶排序一样, 计算出计数列表的有效范围
    count_items = [0 for _ in range(count_size)]             # 像桶排序一样, 创建一个跟有效范围一样长度的列表.

    for i in range(0, len(items)):
        index = items[i] - min_value                         # 两个实际值相减, 得出相对的索引位置.
        count_items[index] += 1                              # 因此采用递增来记录相同值的次数.

    ordered_items = []                                       # 创建一个空的有序列表.
    for index, times in enumerate(count_items):              # 这里采用全新生成的数值重写到ordered_items列表中.
        for _ in range(times):                               # 排序是没有问题的, 而且还特别简单.
            ordered_items.append(min_value + index)          # 但需要注意的是, 这种写法无法证明它是稳定的排序.

    return ordered_items


if __name__ == '__main__':
    # collection = random.sample(range(-50, 50), 50)
    collection = [2, 5, 1, 2, 2, 5, 1, 1]
    sorted_collection = sorted(collection)
    assert count_sort(collection) == sorted_collection
