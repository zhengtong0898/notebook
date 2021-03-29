from typing import List
import random


# 桶排序--线性表
def bucket_sort_linear(items, bucket_size: int):
    """
    区间分组算法

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
    """
    if not items: return []
    max_value, min_value = max(items), min(items)

    # 创建木桶数量
    buckets = [[] for i in range(bucket_size)]

    # 计算每个木桶的高度
    bucket_high = (max_value - min_value) / bucket_size

    # 将元素分散到正确的木桶.
    for item in items:
        # 计算出当前 item 与 min_value(第0位数据) 的距离
        distance = item - min_value

        # 通过距离可以得出它应该存放在哪个桶内.
        float_index = distance / bucket_high
        int_index = int(float_index)

        # 计算边界:
        #   float_index - int_index > 0 时, 表示含有小数, 即: 它应该存放在整数的那个桶里面.
        #   float_index - int_index == 0 时, 表示没有小数, 即: 它应该存放在整数-1的那个桶的最后一个位置.
        #
        # 边界的特殊情况:
        #   item == min_value 时, distance = 0; float_index = 0; int_index = 0;
        #   这种情况下它不应该是-1, 因为这样会导致它尝试定位到 buckets[-1] 的位置.
        #   所以解决办法有两种:
        #   1. index = (int_index - 1) if float_index - int_index == 0 and item != min_value else int_index
        #   2. index = max((int_index - 1), 0) if float_index - int_index == 0 else int_index
        index = max((int_index - 1), 0) if float_index - int_index == 0 else int_index
        buckets[index].append(item)

    return [v for bucket in buckets for v in sorted(bucket)]


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    assert bucket_sort_linear(collection, 5) == sorted(collection)
