# 基数排序
# 原理:      https://www.bilibili.com/video/BV1A54y1D7Kd
# 参考:      https://www.geeksforgeeks.org/radix-sort/
#           https://www.programiz.com/dsa/radix-sort
#           https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
# 时间复杂度: Average-O(n+k)    Average-O(n+k)     Average-O(n+k)    Space-O(max)    Stability-Yes
# 困难程度:   Medium


def count_sort(items, int_cursor):
    n = len(items)

    count = [0] * 10                                   # 有效计数范围是 0 - 9
    ordered = [0] * n                                  # 创建一个空的有序列表, 长度与原始列表长度一致.

    for i in range(0, n):                              # 将 items 中的每个元素按相同索引位置进行分桶.
        index = items[i] // int_cursor                 # 当 items[i] == 6240, 6240 % 10 得到 0.
        count[index % 10] += 1                         # 当 items[i] == 6240,  624 % 10 得到 4.
                                                       # 当 items[i] == 6240,   62 % 10 得到 2.
                                                       # 当 items[i] == 6240,    6 % 10 得到 6.

    for i in range(1, 10):
        count[i] += count[i - 1]                       # 推算出实际值(从右往左)的索引位置, 这里无法言传只能debug去感受.

    i = n - 1
    while i >= 0:                                      # 从右往左遍历
        index = items[i] // int_cursor                 # 剔除已经计算过的数值.
        layer_int = index % 10                         # 获取到具体那一层的数字.
        ordered_index = count[layer_int] - 1           # 由于索引是从0开始, 所以这里要-1
        ordered[ordered_index] = items[i]              # 将数值写入到已排序的那个位置.
        count[layer_int] -= 1                          # 写入后-1, 表示下一个相同的数值应该写在当前位置的前一个位置.
        i -= 1                                         # i递减1是从右往左进一位, 为下一次循环做准备.

    for i in range(0, len(items)):                     # 将 ordered 写入到 items 原始列表中.
        items[i] = ordered[i]


def radix_sort(arr):
    int_cursor = 1                                     # 标记数字的游标, 采取 * 10 的进位法, 锁定个位、十位、百位等索引位置.
    while (max(arr) / int_cursor) > 1:
        count_sort(arr, int_cursor)                    # 对所标记的索引位置的数字进行排序.
        int_cursor *= 10                               # 进位.


if __name__ == '__main__':
    # collection = random.sample(range(-50, 50), 50)
    collection = [6420, 5365, 7534, 7910, 1779, 3142, 2385, 3930]
    sorted_collection = sorted(collection)
    radix_sort(collection)
    assert collection == sorted_collection
