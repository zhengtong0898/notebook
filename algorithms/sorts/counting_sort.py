# 计数排序
# 原理:      https://www.bilibili.com/video/BV1ML411n7ox
# 参考:      https://www.geeksforgeeks.org/counting-sort/?ref=lbp
#           https://www.programiz.com/dsa/counting-sort
#           https://github.com/TheAlgorithms/Python/blob/master/sorts/counting_sort.py
#           https://www.cs.usfca.edu/~galles/visualization/CountingSort.html
# 时间复杂度: Average-O(n+k)    Average-O(n+k)     Average-O(n+k)    Space-O(max)    Stability-yes
# 困难程度:   Easy


def count_sort(items):
    # 遍历获得列表中最大和最小的值.
    max_value, min_value = int(max(items)), int(min(items))

    # 有效的计数范围
    count_size: int = int(max_value - min_value) + 1
    count_items = [0 for _ in range(count_size)]

    # 创建一个与items一样长度的列表, 初始值全部是0, 用于排序.
    ordered_items = [0 for _ in range(len(items))]

    # items[i] - min_value 得到的最小索引是0, 得到的最大索引是len(items) - 1,
    #                      在这个索引位置上 += 1, 相同的数值会持续递增.
    for i in range(0, len(items)):
        count_items[items[i] - min_value] += 1

    # Change count_items[i] so that count_items[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_items)):
        count_items[i] += count_items[i - 1]

    # Build the output character itemsay
    for i in range(len(items) - 1, -1, -1):
        ordered_items[count_items[items[i] - min_value] - 1] = items[i]
        count_items[items[i] - min_value] -= 1

    # Copy the output itemsay to items, so that items now
    # contains sorted characters
    for i in range(0, len(items)):
        items[i] = ordered_items[i]

    return items


# Driver program to test above function
collection = [2, 5, 1, 2, 2, 5, 1, 1]
ans = count_sort(collection)
print("Sorted character array is " + str(ans))

