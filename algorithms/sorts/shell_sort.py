# 希尔排序
# 原理:  https://www.bilibili.com/video/av94596268
#       https://www.pythonpool.com/shell-sort-python/
#       https://www.programiz.com/dsa/shell-sort
# 参考: https://www.geeksforgeeks.org/python-program-for-shellsort/
# 时间复杂度: Worst-O(n2)     Average-O(nlog n)    Best-O(nlog n)    Space-O(1)    Stability-No
import random


def shell_sort(items):
    n = len(items)
    gap = n // 2

    while gap > 0:

        # range(gap, n) -> 遍历右侧元素.
        # 由于 n // 2, 左侧元素要么等于右侧元素,
        # 要么小于右侧元素, 因此这里选择遍历右侧元素.
        for r_index in range(gap, n):

            r_value = items[r_index]
            l_index = r_index
            while True:

                # 为了保护 items[l_index - gap] 操作, 所以必须加这个条件.
                if l_index < gap:
                    break

                # 与右侧位置相对应的左侧元素 <= r_value 时, 表示左小右大, 排序正确.
                if items[l_index - gap] <= r_value:
                    break

                # 当左大右小时, 代码会来到这里, 执行: 将左侧大的值写入到右侧位置.
                items[l_index] = items[l_index - gap]
                l_index -= gap

            # 如果没有执行位置交换, 那么 l_index 依旧是等于 r_index, 下面这条语句相当于将值复位.
            # 如果已执行位置交换, 那么 l_index 的位置就是左侧对应的位置, 下面这条语句相当于是将右侧小的值写入左侧.
            items[l_index] = r_value

        gap //= 2


if __name__ == '__main__':
    collection = random.sample(range(-50, 50), 50)
    sorted_collection = sorted(collection)
    shell_sort(collection)
    assert collection == sorted_collection
