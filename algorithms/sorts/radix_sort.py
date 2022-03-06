# 基数排序
# 原理:      https://www.bilibili.com/video/BV1A54y1D7Kd
# 参考:      https://www.geeksforgeeks.org/radix-sort/
#           https://www.programiz.com/dsa/radix-sort
#           https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
# 时间复杂度: Average-O(n+k)    Average-O(n+k)     Average-O(n+k)    Space-O(max)    Stability-Yes
# 困难程度:   Medium


def count_sort(arr, int_cursor):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * n

    # initialize count array as 0
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // int_cursor
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // int_cursor
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    int_cursor = 1                                     # 标记数字的游标, 采取 * 10 的进位法, 锁定个位、十位、百位等索引位置.
    while (max(arr) / int_cursor) > 1:
        count_sort(arr, int_cursor)                    # 对所标记的索引位置的数字进行排序.
        int_cursor *= 10                               # 进位.


if __name__ == '__main__':
    # collection = random.sample(range(-50, 50), 50)
    collection = [2, 5, 1, 2, 2, 5, 1, 1]
    sorted_collection = sorted(collection)
    radix_sort(collection)
    assert collection == sorted_collection
