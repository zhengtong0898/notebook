from typing import List
import math


def bucket_sort(items: list, bucket_num: int) -> list:
    if not items: return []
    min_value, max_value = min(items), max(items)

    # 创建木桶
    buckets: List[list] = [[] for i in range(bucket_num)]

    for i in range(len(items)):
        # 区间分组算法
        #
        # 假设: [29,37,3,9,21,25,43,49,100]
        # 假设: bucket_num = 5;  max_value = 100;
        # 那么数据将会按这个区间分组保存到这5个bucket中.
        #  0-20       20-40      40-60      60-80      80-100
        #              29
        #   2          21         43
        #   9          25         49                    100
        # bucket1    bucket2    bucket3    bucket4    bucket5
        #
        # 假设数组是: [29,37,3,9,21,25,43,49,101,500]
        # 假设: bucket_num = 5;  max_value = 500;
        #  0-100     100-200    200-300    300-400    400-500
        #   49
        #   43
        #   25
        #   21
        #   9
        #   3
        #   37
        #   29         101                              500
        # bucket1    bucket2    bucket3    bucket4    bucket5
        index = math.floor((bucket_num * items[i] - 1) / max_value)
        print("index: ", index, "; items[i]: ", items[i])
        buckets[index].append(items[i])

    return [v for bucket in buckets for v in sorted(bucket)]


if __name__ == '__main__':
    collection = [29,37,3,9,21,25,43,49,100]
    assert bucket_sort(collection, 5) == [3, 9, 21, 25, 29, 37, 43, 49, 100]
