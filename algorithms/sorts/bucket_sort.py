# 桶排序
# 思想: 参考下面 bucket_sort 的描述.
# 原理: https://www.bilibili.com/video/av55573441
# 参考: https://github.com/TheAlgorithms/Python/blob/master/sorts/bucket_sort.py
#      https://www.geeksforgeeks.org/bucket-sort-2/
# 时间复杂度: Average-O(n)    Worst-O(n^2)     Best-O(n+k)    Space-O(n+k)    Stability-Yes
import random


# 桶排序--线性表
def bucket_sort(items) -> list:
    """
    桶排序, 也是区间分组算法.

    假设: [29,37,3,9,21,25,43,49,100]
    假设: bucket_size = 5;
    那么数据将会按这个区间分组保存到这5个bucket中.
     0-20       20-40      40-60      60-80      80-100
                 29
      2          21         43
      9          25         49                    100
    bucket1    bucket2    bucket3    bucket4    bucket5

    假设数组是: [29,37,3,9,21,25,43,49,101,500]
    假设: bucket_size = 5;
     0-100     100-200    200-300    300-400    400-500
      49
      43
      25
      21
      9
      3
      37
      29         101                              500
    bucket1    bucket2    bucket3    bucket4    bucket5

    上面两个假设由于 bucket_size 都是一个固定值, 所以很多时候会导致偏差严重,
    为了解决这个问题, 就需要动态的创建桶数量.
    """
    if not items:
        return []

    # 遍历获得列表中最大和最小的值.
    # 目的: 为了让桶在有效的范围.
    max_value, min_value = max(items), min(items)

    # 桶数量
    bucket_size: int = int(max_value - min_value) + 1

    # 按桶数量创建数量相同的空列表, 每个列表都代表一个桶.
    # 目的: 用于将各个区间的值放入对应的列表中.
    buckets = [[] for i in range(bucket_size)]

    # 将元素分散到正确的木桶.
    for item in items:
        # 计算出当前 item 与 min_value(第0位数据) 的距离
        distance = item - min_value

        # 通过距离可以得出它应该存放在哪个桶内.
        index = int(distance) // bucket_size

        # 将元素写入到对应的桶中.
        buckets[index].append(item)

    # 上面这些代码只是将数据分门别类放在不同的桶里面, 没有任何排序效果, 这里还是要调用 sorted 来排序.
    return [v for bucket in buckets for v in sorted(bucket)]


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    sorted_collection = sorted(collection)
    assert bucket_sort(collection) == sorted_collection
